import threading
from django.core.mail import EmailMessage



class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

try:
    email = EmailMessage(subject='hi', body='hello, trial API',
                     to=['doccasheby@gmail.com',])


    email.content_subtype = 'html'
    email.send()
    print('done, email sent')

except:
    print('email not sent')