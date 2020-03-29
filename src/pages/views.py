from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello world </h1>")
    return render(request, "home.html", {})


def contact_view(*args, **kwargs):
    return HttpResponse("<h1> contact page </h1>")


def about_view(*args, **kwargs):
    return HttpResponse("<h1> about page </h1>")


def social_view(*args, **kwargs):
    return HttpResponse("<h1> social page </h1>")
