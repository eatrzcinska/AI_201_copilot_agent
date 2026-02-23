from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clean up old data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()


        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', username='IronMan', team_id=str(marvel._id))
        captain = User.objects.create(email='captain@marvel.com', username='CaptainAmerica', team_id=str(marvel._id))
        batman = User.objects.create(email='batman@dc.com', username='Batman', team_id=str(dc._id))
        superman = User.objects.create(email='superman@dc.com', username='Superman', team_id=str(dc._id))

        # Activities
        Activity.objects.create(user_id=str(ironman._id), type='run', duration=30, date='2024-01-01')
        Activity.objects.create(user_id=str(captain._id), type='cycle', duration=45, date='2024-01-02')
        Activity.objects.create(user_id=str(batman._id), type='swim', duration=60, date='2024-01-03')
        Activity.objects.create(user_id=str(superman._id), type='fly', duration=120, date='2024-01-04')

        # Workouts
        w1 = Workout.objects.create(name='Pushups', description='Do 50 pushups', suggested_for_ids=[str(marvel._id), str(dc._id)])
        w2 = Workout.objects.create(name='Situps', description='Do 50 situps', suggested_for_ids=[str(dc._id)])

        # Leaderboard
        Leaderboard.objects.create(team_id=str(marvel._id), points=200)
        Leaderboard.objects.create(team_id=str(dc._id), points=150)

        # Ensure unique index on email
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]
        db.users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data and unique email index created.'))
