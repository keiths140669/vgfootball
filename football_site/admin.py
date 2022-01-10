from django.contrib import admin
from .models import TeamName

@admin.register(TeamName)
class TeamNameAdmin(admin.ModelAdmin):
	list_display = ('team_name', 'age_group')
	ordering = ('team_name',)
