from django.http import HttpResponse,JsonResponse
from .tasks import sendEmail
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")


@cache_page(60)
def test(request):
    response = requests.get("https://e241b94b-be0a-420d-b2e8-0730c530c097.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())