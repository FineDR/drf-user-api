from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserTB
from .serializers import UserTBSerializer, LoginSerializer, UserProfileSerializer
import jwt
from django.conf import settings
from rest_framework import status, permissions
from drf_spectacular.utils import extend_schema
from django.http import JsonResponse
from django.contrib.auth import get_user_model

import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
class RegisterView(APIView):
    permission_classes = [AllowAny]
    """
    API for user registration.
    """
    @extend_schema(
        request=UserTBSerializer,
        responses={200: None},
        summary="Register a new user",
        description="Takes email and password to create a new user."
    )

   

    def post(self, request):
        serializer = UserTBSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate Email Verification Token
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relative_link = reverse("verify-email")
            verification_url = f"http://{current_site}{relative_link}?token={str(token)}"

            # Email Content with Descriptive Link
            email_subject = "Verify Your Email Address"
            email_body = (
                f"Hello {user.email},\n\n"
                "Thank you for signing up! Please verify your email address to activate your account.\n\n"
                "Click the button below to confirm your email:\n\n"
                f"[Verify Email]({verification_url})\n\n"
                "If you did not sign up, you can ignore this email.\n\n"
                "Best regards,\nYour Company Team"
            )

            # Send Email
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return Response({"message": "User registered successfully. Please check your email to verify your account."},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmailView(APIView):
    """
    API to verify user email.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get("token")

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = UserTB.objects.get(id=payload["user_id"])
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
            return Response({"message": "Email already verified."}, status=status.HTTP_400_BAD_REQUEST)

        except jwt.ExpiredSignatureError:
            return Response({"error": "Activation link expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    """
    API for user login.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "email": user.email,
                    
                }
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    """
    API for retrieving and updating user profile.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def run_create_superuser(request):
    User = get_user_model()
    email = "admin@gmail.com"
    password = "admin12345"

    if not User.objects.filter(email=email).exists():
        User.objects.create_superuser(
            email=email,
            password=password,
            first_name="Super",
            last_name="Admin",
            middle_name="System",
            phone_number="1234567890",
            role="seller",  # or any role you support
            is_active=True,
        )
        return JsonResponse({"message": "✅ Superuser created successfully."})
    else:
        return JsonResponse({"message": "⚠️ Superuser already exists."})
    


@csrf_exempt
def run_migrations(request):
    try:
        result = subprocess.run(["python", "manage.py", "migrate"], check=True, capture_output=True, text=True)
        return JsonResponse({"message": "✅ Migrations applied", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return JsonResponse({"error": "❌ Migration failed", "details": e.stderr}, status=500)