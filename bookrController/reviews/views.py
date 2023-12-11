from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello uruguaj <3 <h1>god</h1>")


def main(request):
    search = request.GET.get("search")
    return render(request, "base.html", {"search": search})
