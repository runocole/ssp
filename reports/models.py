from django.db import models
from django.conf import settings
from teams.models import Team

class Report(models.Model):
    STATUS_CHOICES = [
        ('not-started', 'Not Started'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='reports')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not-started')

    key_players = models.JSONField(default=list)
    match_stats = models.JSONField(default=dict)
    tactical_summary = models.JSONField(default=dict)
    performance_insights = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team.name} Report by {self.author.email} ({self.status})"