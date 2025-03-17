from django.urls import path
from .views import RegisterView, VerifyEmailView, UserLoginView, UserProfileView
from .password_reset import ForgotPasswordView,PasswordResetView
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify-email"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<token>/', PasswordResetView.as_view(), name='reset-password'),
]
