from django.urls import path
from .views import ActivityListView, TeamActivityListView

urlpatterns = [
    path('', ActivityListView.as_view(), name='activity-list'),
    path('team/<int:team_id>/', TeamActivityListView.as_view(), name='team-activity-list'),
]