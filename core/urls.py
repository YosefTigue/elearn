from django.contrib.auth import views as auth_views
from django.urls import path 
from . import views
from .forms import LoginForm




urlpatterns=[
    path('', views.index, name="index"),
    path('department/', views.department, name="department"),
    path('about/', views.about, name='about'),
    path('<int:pk>/', views.detail, name="detail"),
    path('signup/', views.signup, name="signup"),
    path('contact/',views.contact, name="contact" ),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout_user', views.logout_user, name='logout'),
     
]