from django.urls import path
from Accounts import views


urlpatterns = [
    
    path('', views.loginview, name='login-page'),
    path('logout/', views.logoutfonc, name='logout'),
    path('register/', views.Registerfonc, name='register'),

]

