from django.http import HttpResponse
from django.http import HttpRequest
from datetime import datetime


# Create your views here.
def current_time(request: HttpRequest) -> HttpResponse:
    now = datetime.now()
    time_now = now.strftime("%d-%m-%Y %H:%M")
    output = "Current time is {0}!".format(time_now)
    return HttpResponse(output)
