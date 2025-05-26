from rest_framework import generics, permissions
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsActivityOwner

class ActivityListView(generics.ListAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user).order_by('-timestamp')

class TeamActivityListView(generics.ListAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Activity.objects.filter(resource_type='report', resource_id__in=[
            report.id for report in self.request.user.reports.filter(team_id=team_id)
        ])