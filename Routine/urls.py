from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.add_routine, name='routine'),
    #login path
    path('login/', views.login, name='login'),
    #register path  
    path('register/', views.register, name='register'),
    path('logout/',views.logout, name="logout"),
    path('delete/<int:id>', views.delete_routine , name="delete-routine"),
]

