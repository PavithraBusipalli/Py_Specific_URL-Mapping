from django.urls import path
from app1.views import *
app_name='any'
urlpatterns=[
    path('fun1ofapp1/',fun1ofapp1,name='fun1ofapp1'),
    path('fun2ofapp1/',fun2ofapp1,name='fun2ofapp1'),
]