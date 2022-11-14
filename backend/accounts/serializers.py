from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from . models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    phone = serializers.CharField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password],style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('pk','email','password','full_name','phone','is_student','is_tuitor','mctnumber','avatar')
        # read_only_fields = ('get_avatar','get_user_fullname','is_active','is_approved','is_staff')
        

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], 
        validated_data['password']
        )
        user.phone = validated_data['phone']
        user.full_name = validated_data['full_name  ']
        user.is_student = validated_data['is_student']
        user.is_tuitor = validated_data['is_tuitor']
        user.mctnumber = validated_data['mctnumber']
        user.avatar = validated_data['avatar']
        user.save()
        return user
