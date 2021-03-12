from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup' ),
    path('signin/', views.signin, name='signin' ),
    path('signout/', views.signout, name='signout' ),
    path('recovery/', views.recovery, name='recovery'),

]