from django.urls import path
from app3.views import *
app_name='any'
urlpatterns=[
    path('fun1/',fun1,name='fun1ofapp3'),
    path('fun2/',fun2,name='fun2ofapp3'),
]