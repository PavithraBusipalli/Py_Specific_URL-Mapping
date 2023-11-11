from django.urls import path
from app2.views import *
app_name='any'
urlpatterns=[
    path('fun1/',fun1,name='fun1ofapp2'),
    path('fun2/',fun2,name='fun2ofapp2'),
]