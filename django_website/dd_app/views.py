from django.http import HttpResponse
from django.shortcuts import render


def about(request): 
    print("this is about page")
    # return HttpResponse("<h1>hello this is about page</h1>")
    return render(request,"index.html")