
from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ['_id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['_id', 'email', 'username', 'team_id', 'is_active']

class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = ['_id', 'user_id', 'type', 'duration', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Workout
		fields = ['_id', 'name', 'description', 'suggested_for_ids']

class LeaderboardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leaderboard
		fields = ['_id', 'team_id', 'points']
