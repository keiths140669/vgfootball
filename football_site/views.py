from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime
from .models import TeamName
from .models import Fixture
from .models import Player 
from .models import Stat
from django.db.models import Count, Sum, Avg
from django.db.models import Q

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

def goals_scored_U10(request):
	
	gs_count = Player.objects.filter(stat__age_group="U10").annotate(total_goals=Sum('stat__stat_goals_scored'), 
		total_goal_assists=Sum('stat__stat_goal_assists'), 
		games_played=Count('stat__stat_goals_scored'),
		goals_per_game=Avg('stat__stat_goals_scored'),
		assists_per_game=Avg('stat__stat_goal_assists')).order_by('-total_goals')
	
	return render(request, 'football_site/goals_U10.html', {
		'gs_count': gs_count,
		})

def stats_players_U9(request):
	stats_players_U9 = Stat.objects.filter(age_group="U9").order_by('stat_date')
	stats_players_count_U9 = Player.objects.all()

	return render(request, 'football_site/stats_U9.html', {
		'stats_players_list': stats_players_U9,
		})

def stats_players_U10(request):
	searchTerm = request.GET.get('searchPlayer')
	if searchTerm:
		#stats_players_U10 = Stat.objects.filter(Q(player_name__first_name__icontains=searchTerm)|Q(player_name__last_name__icontains=searchTerm)).order_by('stat_date')
		stats_players_U10 = Stat.objects.filter(age_group="U10")
		stats_players_U10_1 = stats_players_U10.filter(Q(player_name__first_name__icontains=searchTerm)|Q(player_name__last_name__icontains=searchTerm)).order_by('stat_date')
	else:
		#stats_players_U10 = Stat.objects.all()
		stats_players_U10_1 = Stat.objects.filter(age_group="U10").order_by('stat_date')
		stats_players_count_U10 = Player.objects.all()

	return render(request, 'football_site/stats_U10.html', {
	'stats_players_list': stats_players_U10_1,
	'searchTerm': searchTerm
	})

def fixture_U10(request):
	fixture_U10 = Fixture.objects.filter(age_group="U10").order_by('fixture_date')
	return render(request, 'football_site/fixture_U10.html', {
		'fixture_list_U10': fixture_U10,
		})