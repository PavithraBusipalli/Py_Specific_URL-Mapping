from django.urls import path
from app3.views import *
app_name='any'
urlpatterns=[
    path('fun1ofapp3/',fun1ofapp3,name='fun1ofapp3'),
    path('fun2ofapp3/',fun2ofapp3,name='fun2ofapp3'),
]