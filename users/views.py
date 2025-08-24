from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, UserSerializer  # type: ignore

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Create the user and also return JWT tokens so the client is logged in immediately.
        """
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(email=response.data["email"])
        refresh = RefreshToken.for_user(user)

        body = {
            "user": UserSerializer(user).data,
            "tokens": {"access": str(refresh.access_token), "refresh": str(refresh)},
        }

        return Response(body, status=status.HTTP_201_CREATED)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh = request.data.get("refresh")
            if not refresh:
                return Response({"detail": "Refresh token required"}, status=400)

            token = RefreshToken(refresh)
            token.blacklist()
            return Response({"detail": "Logged out"}, status=205)
        except Exception:
            return Response({"detail": "Invalid token"}, status=400)
