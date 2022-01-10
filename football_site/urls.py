from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('team_name_U10', views.team_name_U10, name='team-name-U10'),
]