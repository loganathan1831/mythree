from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('loganathan/',loganathan,name='loganathan'),
    path('logan/',logan,name='logan')
]