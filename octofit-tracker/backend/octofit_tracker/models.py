

from djongo import models

class Team(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False)
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	class Meta:
		db_table = 'teams'
	def __str__(self):
		return self.name

class User(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False)
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=100)
	team_id = models.CharField(max_length=24, blank=True, null=True)
	is_active = models.BooleanField(default=True)
	class Meta:
		db_table = 'users'
	def __str__(self):
		return self.username

class Activity(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False)
	user_id = models.CharField(max_length=24)
	type = models.CharField(max_length=50)
	duration = models.PositiveIntegerField(help_text='Duration in minutes')
	date = models.DateField()
	class Meta:
		db_table = 'activities'
	def __str__(self):
		return f"{self.user_id} - {self.type} ({self.date})"

class Workout(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	suggested_for_ids = models.JSONField(default=list, blank=True)
	class Meta:
		db_table = 'workouts'
	def __str__(self):
		return self.name

class Leaderboard(models.Model):
	_id = models.ObjectIdField(primary_key=True, editable=False)
	team_id = models.CharField(max_length=24)
	points = models.PositiveIntegerField(default=0)
	class Meta:
		db_table = 'leaderboard'
	def __str__(self):
		return f"{self.team_id}: {self.points} pkt"
