from django.core.mail import EmailMessage

# import os
# # send_mail('hello maen', 'this is a message','2001stany@gmail.com', ['doccasheby@gmail.com',])


# print(os.environ.get('EMAIL_HOST_USER'))

try:
    email = EmailMessage(subject='hi', body='testing mail',
        from_email='2001stany@gmail.com', to=['doccasheby@gmail.com',])
    
    email.send()
    print('success')

except:
    print('failed')