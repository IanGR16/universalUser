from django.db.models import fields
from rest_framework import serializers

from user.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'email', 
            'first_name', 
            'last_name', 
            'cpf', 
            'gr', 
            'birth_date', 
            'telephone',
            'cep',
            'residential_complement', 
            'residential_num', 
            'is_apartment'
        ]

        extra_kwargs= {'password':{'write_only': True}}

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

