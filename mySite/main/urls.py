from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('show/',views.showItems,name='showItems'),
    path('<int:id>/',views.deleteItems,name="delete")
]
