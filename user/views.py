
from django.forms import PasswordInput
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication

from user.serializers import AccountSerializer, LoginSerializer

from .models import User
from django.views.generic.edit import CreateView


class UserViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = []

    def accounts(self, request):
        html = 'account.html'
        try:
            serializer = AccountSerializer(data=request.data)
            print(request.data)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            resp = 'Cadastro realizado'
            return render(request, html, { 'status_code':201, 'resp': resp})
            
        except:
            print(request.data)
            if request.data == {}:
                resp = ''
                status_code=404
            else :
                resp = 'Erro no cadastro'
                status_code=400

            return render(request, html, { 'status_code':status_code, 'resp': resp})

    

    def login(self, request):
        html = 'login.html'
        try:
            serializer = LoginSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            user = authenticate(**serializer.validated_data)

            if user:
                token = Token.objects.get_or_create(user=user)[0]
                return render(request, html, {'token': token.key, 'status_code':200, 'password': PasswordInput})

            
            return render(request, html, { 'status_code':401, 'err': 'Invalid username or password'})
        
        except:
            return render(request, html, { 'status_code':400, 'err': 'Invalid username or password'})
