from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response

class RegisterView(CreateAPIView):
    queryset = User.objects.all() 
    serializer_class = RegisterSerializer


    #!create methodunu override edip oluşturduğumuz token ı içine koyuyoruz, auth dersinde token ı burada create etmiştik burada signals da create yapıyoruz.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        token = Token.objects.get(user=user)  #O Token ı al
        data["token"] = token.key #data nın içerisine koy
        
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
