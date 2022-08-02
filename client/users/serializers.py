from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, 
        validators=[validators.UniqueValidator(queryset=User.objects.all())] 
    )
    password = serializers.CharField(
        write_only=True, #!sadece write yaparken bu çeğrılacak, get de yok
        # required=True,
        validators=[validate_password],
        style={"input_type": "password"} #Browser API da güzel gözüksün diye, frontend le alakalı değil
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"} 
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        )
    def create(self, validated_data):
        password = validated_data.pop("password") 
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


# Kendi validationumuzu yaptık? pass1 eşitmi pass2

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password": "Password didn't match...."}
            )
        return data

#! Login olunca tokenla birlikte user bilgilerini de göndermek için tokenserialzers ı override ediyoruz.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email"
        )


class CustomTokenSerializer(TokenSerializer):
    user = UserSerializer(read_only=True)

    class Meta(TokenSerializer.Meta): #token serializerın metasını kullan
        fields = (
            "key",
            "user"
        )
