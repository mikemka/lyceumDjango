from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
