from django.urls import path
from api import views

urlpatterns = [
    path('data/', views.get_data, name="get_data"),
]
