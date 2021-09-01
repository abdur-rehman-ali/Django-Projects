from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('signIn',views.signIn_view,name='signIn'),
    path('logIn/',views.logIn_view,name='logIn'),
    path('logOut/',views.logOut_view,name='logOut'),
]
