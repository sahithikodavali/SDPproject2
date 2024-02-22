from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from . views import*
urlpatterns = [
    path('hello2/', hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('travelpackage',travelpackage,name='travelpackage'),
    path('print',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),

    path('h/',ran,name="ran"),
    path('context/',random123,name='random123'),
    path('date1/', getdate1, name='getdate1'),
    path('date/', get_date, name='get_date'),
    path('r/',reg,name='reg'),
    path('reg/',registerloginfunction,name='registerloginfunction'),
    path('pie1/', Pie, name='Pie'),
    path('pie/', pie_chart, name='pie_chart'),
    path('pics/', fam, name='fam'),
    path('weather/',weatherpage, name='weatherpage'),
    path('w/',weatherlogic,name='weatherlogin'),

    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('contact/',contact,name='contactus'),
    path('contactmail/',contactmail,name='contactmail'),



]