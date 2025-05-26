from django.test import TestCase
from django.contrib.auth import get_user_model
from teams.models import Team
from .models import Report

User = get_user_model()

class ReportModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test FC", logo="http://logo.png", color="#fff", league_id=1)
        self.user = User.objects.create_user(email="analyst@test.com", password="pass1234", role="analyst")
        self.report = Report.objects.create(
            team=self.team,
            author=self.user,
            status='in-progress',
            key_players=[{"id": 1, "name": "Player 1", "position": "FW", "rating": 8, "strengths": "Speed"}],
            match_stats={"possession": 55, "shots": 10},
            tactical_summary={"formation": "4-3-3", "overview": "High press", "strengths": "Midfield", "weaknesses": "Defense"},
            performance_insights="Great team performance"
        )

    def test_report_creation(self):
        self.assertEqual(self.report.team.name, "Test FC")
        self.assertEqual(self.report.author.email, "analyst@test.com")
        self.assertEqual(self.report.status, "in-progress")