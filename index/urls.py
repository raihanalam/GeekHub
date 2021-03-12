from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/',include('account.urls')),
    path('home/',include('home.urls')),
    path('question/',include('question.urls')),
]
