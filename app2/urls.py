from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path('ram/',ram,name='ram')
    path('man/',man,name='man')
]