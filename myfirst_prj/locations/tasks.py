from myfirst.celery import app
from django.core.mail import send_mail
from datetime import datetime

start=datetime.now()


@app.task
def send_email(message):

    print("Sending email to loboda.pavel.and@gmail.com")

    send_mail(
        'Hello ^_0',
        str(message),
        'locaionswebapp@gmail.com',
        ['loboda.pavel.and@gmail.com', ],
        fail_silently=False,
    )
    print("email sent")


@app.task
def print_runtime():
    print("[ Log ]: Current runtime is: " + str(datetime.now() - start))