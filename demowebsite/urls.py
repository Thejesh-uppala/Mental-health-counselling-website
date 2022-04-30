from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('studentlogin',views.studentlogin,name='studentlogin'),
    path('counsellorlogin',views.counsellorlogin,name='counsellorlogin'),
    path('signup',views.signup,name='signup'),
    path('register',views.register,name='register'),
    path('slogin',views.slogin,name='slogin'),
    path('clogin',views.clogin,name='clogin'),
    path('bookappointment',views.bookappointment,name='bookappointment'),
    path('fixappointment',views.fixappointment,name='fixappointment'),
]