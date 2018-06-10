'''
This is where all the urls pertaining to MUSIC app should go
'''

from . import views
from django.http import HttpResponse
from django.urls import path, include

#This sets the namespace so when we call the url, we can use <namespace>:url link
# for example <a href="{% url 'main:musicDetails' album.id %}">
app_name = 'main'

urlpatterns = [
    #/main page/
    path('', views.main_page, name = 'homepage'),

]