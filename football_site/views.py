from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import TeamName

def home(request):
	
	return render(request, 'football_site/home.html')

def team_name_U9(request):
	team_name_U9 = TeamName.objects.filter(age_group="U9").order_by('team_name')

	return render(request, 'football_site/team_name_U9.html', {
		'team_name_U9': team_name_U9
		})

def team_name_U10(request):
	team_name_U10 = TeamName.objects.filter(age_group="U10").order_by('team_name')

	return render(request, 'football_site/team_name_U10.html', {
		'team_name_U10': team_name_U10
		})