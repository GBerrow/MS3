from django.urls import path
from . import views

urlpatterns = [
    path('preferences/', views.preferences, name='preferences'),
    path('notifications/', views.notifications, name='notifications'),
]
