from django.shortcuts import render, HttpResponse

def contactus(request):
    return render(request, "contactus.html")