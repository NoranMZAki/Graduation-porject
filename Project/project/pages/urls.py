from django.urls import path
from .import views
urlpatterns = [


    path('aboutus', views.AboutUs.as_view(), name='about'),
    path('', views.HomeView.as_view(), name='index'),
    path('settings/', views.Setting.as_view(), name='setting')


]
