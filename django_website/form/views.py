from django.shortcuts import render

# Create your views here.
def formfill(request):
    return render(request, 'form.html')