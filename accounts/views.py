from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from django.contrib.auth import login, logout, authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        full_name = request.data.get("full_name")
        username = request.data.get("username")

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            full_name=full_name
        )

        return Response({
            "message": "User created successfully",
            "user_id": user.id
        }, status=status.HTTP_201_CREATED)




class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if user:
            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "role": user.role
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out"})