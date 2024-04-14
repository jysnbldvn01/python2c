from django.urls import path
from . import views

urlpatterns = [ 
             path('Mypage', views.home, name='home'),
]