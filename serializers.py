from rest_framework import serializers
from django.contrib.auth.models import User




class RegisterSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']