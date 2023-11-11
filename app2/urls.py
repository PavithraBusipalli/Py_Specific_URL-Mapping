from django.urls import path
from app2.views import *
app_name='any'
urlpatterns=[
    path('fun1ofapp2/',fun1ofapp2,name='fun1ofapp2'),
    path('fun2ofapp2/',fun2ofapp2,name='fun2ofapp2'),
]