from django.urls import path
from .views import *

app_name= 'about'

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('privacy/', privacy, name="privacy"),
    path("agreement", agreement, name="agreement"),
]
