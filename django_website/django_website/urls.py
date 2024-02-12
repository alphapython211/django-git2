from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('contactus/', include('ContactUs.urls')),
    path('about/', include ('dd_app.urls')),
    path('', include('Home.urls')),

]
