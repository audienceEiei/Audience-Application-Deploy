from django.contrib import admin
from django.urls import path
from . import views

app_name = "audience"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path("sports/", views.sports, name="sports"),
    path("sport/<int:sport_id>", views.sport, name="sport"),

    # For testing get data
    path('get_dashboard/', views.get_dashboard, name="get_dashboard"),
    path('get_sports/', views.get_sports, name="get_sports"),
    path('get_sport/<int:sport_id>', views.get_sport, name="get_sport"),
]
