from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from serializers import RegisterSerilizer



class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerilizer