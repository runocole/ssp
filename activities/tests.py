from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Activity

User = get_user_model()

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@activity.com", password="pass1234", role="analyst")
        self.activity = Activity.objects.create(
            user=self.user,
            action='created',
            resource_type='report',
            resource_id=1,
            details='Created scouting report'
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.user.email, "test@activity.com")
        self.assertEqual(self.activity.action, "created")
        self.assertEqual(self.activity.resource_type, "report")
        self.assertEqual(self.activity.resource_id, 1)