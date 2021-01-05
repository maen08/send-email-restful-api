from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from serializers import RegisterSerilizer
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import EmailMessage
from django.http import HttpResponse



class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerilizer

    def post(self, request):
        serilizer = self.serializer_class(data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()


        # creating token part
        user_data = serilizer.data
        user = User.objects.get(email=user_data.get('email'))
        token = RefreshToken.for_user(user).access_token
        print(token)

        EmailMessage(subject='hi', body='this is trial', to='doccasheby@gmail.com')
        
    
        return HttpResponse('<h1>API worked!</h1>')












        # current_site = get_current_site(request).domain

    # @staticmethod
    # def send_email(data):
    #     email = EmailMessage(
    #         subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
    #     EmailThread(email).start()
