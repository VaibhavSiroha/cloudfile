from django.urls import path
from . import views

urlpatterns = [
    path('test', views.TestView.as_view(),name='test'),
    path('register', views.RegisterView.as_view(),name='register'),
    path('login', views.LoginView.as_view(),name='login'),
    path('logout', views.LogoutView.as_view(),name='logout'),
    path('profile/<str:username>', views.ProfileView.as_view(),name='profile'),
]
