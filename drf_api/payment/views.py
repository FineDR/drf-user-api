import stripe
from django.conf import settings
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework.generics import get_object_or_404

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class PaymentListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        payments = Payment.objects.filter(rider=request.user)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def post(self, request):
        amount = request.data.get('amount_paid')
        payment_method_id = request.data.get('payment_method_id')

        if not amount or not payment_method_id:
            return Response({"error": "Amount and payment method are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            print(f"Processing payment with amount: {amount}, payment_method_id: {payment_method_id}")

            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),
                currency="usd",
                payment_method=payment_method_id,
                automatic_payment_methods={
                    "enabled": True,
                    "allow_redirects": "never"
                },
            )

            print(f"PaymentIntent created successfully: {intent.id}")

            payment = Payment(
                rider=request.user,
                contract_id=request.data.get('contract'),
                amount_paid=amount,
                payment_date=request.data.get('payment_date'),
                status="Pending",  # Initially set to 'Pending'
                transaction_id=intent.id,
            )
            payment.save()

            return Response({
                "payment": PaymentSerializer(payment).data,
                "status": intent.status,
            }, status=status.HTTP_201_CREATED)

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            print(f"Card error occurred: {err.get('message')}")
            return Response({"error": err.get('message')}, status=status.HTTP_400_BAD_REQUEST)

        except stripe.error.StripeError as e:
            print(f"Stripe error: {e}")
            return Response({"error": "Stripe error occurred, please try again later."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk, rider=request.user)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk, rider=request.user)
        serializer = PaymentSerializer(payment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk, rider=request.user)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentApprovalAPIView(APIView):
    permission_classes = [permissions.IsAdminUser] 

    def put(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)

      
        status = request.data.get("status")
        if status not in ["Approved", "Rejected"]:
            return Response({"error": "Invalid status. Only 'Approved' or 'Rejected' are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        payment.status = status
        payment.save()

        return Response({
            "payment": PaymentSerializer(payment).data,
            "status": payment.status,
        }, status=status.HTTP_200_OK)
