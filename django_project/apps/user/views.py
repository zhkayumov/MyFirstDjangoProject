from django.http import HttpResponse
from django.http import HttpRequest


# Create your views here.
def hello_user(request: HttpRequest) -> HttpResponse:
    firstname = request.GET.get("firstname", "")
    lastname = request.GET.get("lastname", "")
    if firstname == "" or lastname == "":
        output = "Error!"
    else:
        output = "Hello, {0} {1}!".format(firstname, lastname)
    return HttpResponse(output)
