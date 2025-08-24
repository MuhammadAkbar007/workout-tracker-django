from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ("email", "password", "password2", "first_name", "last_name")

    def validate_email(self, value):
        email = value.strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return email

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        # run Django’s validators (uses AUTH_PASSWORD_VALIDATORS in settings.py)
        validate_password(attrs["password2"])
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")  # NOTE: removing from validated_data
        password = validated_data.pop("password")

        user = User.objects.create_user(password=password, **validated_data)  # type: ignore
        return user
