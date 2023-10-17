from django.http import HttpResponse
from .tasks import sendEmail

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")