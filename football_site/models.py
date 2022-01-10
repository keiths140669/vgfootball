from django.db import models

class TeamName(models.Model):
	STATUS = [
		('U7', 'U7'),
		('U8', 'U8'),
		('U9', 'U9'),
		('U10', 'U10'),
		('U11', 'U11'),
		('U12', 'U12'),
		('U13', 'U13'),
		('U14', 'U14'),
		('U15', 'U15'),
		('U16', 'U16'),
		]
	team_name = models.CharField('Team Name', max_length=100, null=True)
	age_group = models.CharField(choices=STATUS, max_length=3, null=True)
	venue = models.CharField('Venue', max_length=120, null=True)
	address = models.CharField('Address', max_length=200, null=True)
	contact = models.CharField('Contact Name', max_length=60, null=True)
	contact_mob = models.CharField('Contact Mobile No', max_length=15, null=True)
	contact_email = models.EmailField('Email', max_length=200, null=True)
	map_link = models.URLField('Map Address Link', max_length=300, null=True)

	def __str__(self):
		return self.team_name + " " + self.age_group