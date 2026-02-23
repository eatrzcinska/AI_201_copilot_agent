from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, User, Activity, Workout, Leaderboard

class BasicApiTests(APITestCase):
	def setUp(self):
		self.team = Team.objects.create(name="Marvel", description="Marvel team")
		self.user = User.objects.create(email="ironman@marvel.com", username="IronMan", team=self.team)
		self.workout = Workout.objects.create(name="Pushups", description="Do 50 pushups")
		self.activity = Activity.objects.create(user=self.user, type="run", duration=30, date="2024-01-01")
		self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

	def test_api_root(self):
		url = reverse('api-root')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_users_list(self):
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_teams_list(self):
		url = reverse('team-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_activities_list(self):
		url = reverse('activity-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_workouts_list(self):
		url = reverse('workout-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_leaderboard_list(self):
		url = reverse('leaderboard-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
