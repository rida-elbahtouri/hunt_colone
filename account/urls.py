from django.urls import path
from . import  views
urlpatterns = [
    path('singhup',views.singhup,name='singhup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]
