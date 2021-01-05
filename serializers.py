from rest_framework import serializers
from django.contrib.auth.models import User




class RegisterSerilizer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(min_length=8, max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password', 'url']