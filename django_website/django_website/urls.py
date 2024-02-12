from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('form/', include('form.urls')),
    path('contactus/', include('ContactUs.urls')),
    path('about/', include ('dd_app.urls')),
    path('', include('Home.urls')),

]
