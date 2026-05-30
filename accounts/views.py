import random
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile, EmailOTP
from .serializers import SignupSerializer
from .serializers import (
    SignupSerializer,
    VerifyEmailSerializer
)

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    SignupSerializer,
    VerifyEmailSerializer,
    LoginSerializer
)
class SignupView(APIView):

    def post(self, request):

        serializer = SignupSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        role = serializer.validated_data["role"]

        if User.objects.filter(email=email).exists():
            return Response(
                {
                    "detail": "User already exists",
                    "code": "user_exists"
                },
                status=400
            )

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            role=role
        )

        otp = str(
            random.randint(100000, 999999)
        )

        EmailOTP.objects.create(
            user=user,
            otp=otp,
            expires_at=timezone.now()
            + timedelta(minutes=5)
        )

        return Response(
            {
                "message": "Signup successful",
                "otp": otp
            },
            status=status.HTTP_201_CREATED
        )
    
class VerifyEmailView(APIView):

     def post(self, request):

        serializer = VerifyEmailSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        email = serializer.validated_data["email"]
        otp = serializer.validated_data["otp"]

        try:
            user = User.objects.get(
                email=email
            )
        except User.DoesNotExist:

            return Response(
                {
                    "detail": "User not found",
                    "code": "user_not_found"
                },
                status=404
            )

        otp_record = EmailOTP.objects.filter(
            user=user
        ).order_by("-created_at").first()

        if not otp_record:

            return Response(
                {
                    "detail": "OTP not found",
                    "code": "otp_not_found"
                },
                status=400
            )

        if otp_record.is_expired():

            return Response(
                {
                    "detail": "OTP expired",
                    "code": "otp_expired"
                },
                status=400
            )

        if otp_record.otp != otp:

            otp_record.attempts += 1
            otp_record.save()

            return Response(
                {
                    "detail": "Invalid OTP",
                    "code": "invalid_otp"
                },
                status=400
            )

        profile = UserProfile.objects.get(
            user=user
        )

        profile.email_verified = True
        profile.save()

        return Response(
            {
                "message": "Email verified successfully"
            }
        )
     

class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(
            username=email,
            password=password
        )

        if not user:
            return Response(
                {
                    "detail": "Invalid credentials",
                    "code": "invalid_credentials"
                },
                status=400
            )

        profile = UserProfile.objects.get(
            user=user
        )

        if not profile.email_verified:
            return Response(
                {
                    "detail": "Email not verified",
                    "code": "email_not_verified"
                },
                status=400
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "role": profile.role
            }
        )