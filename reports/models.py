from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('official', 'Official'),
        ('draft', 'Draft'),
    ]

    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES, default='draft')
    title= models.CharField(max_length=200, default = "Untitled Report")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Tactical Panels
    in_possession = models.TextField(blank=True)
    out_of_possession = models.TextField(blank=True)
    pressing_systems = models.TextField(blank=True)

    # Charts/stats field (stored as JSON string or plain text)
    stats_data = models.TextField(blank=True)

    def __str__(self):
        return f"{self.team.name} - {self.report_type.capitalize()} by {self.coach.username}"


class ReportImage(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='report_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.report.team.name} report"