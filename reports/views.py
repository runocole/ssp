from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer
from .permissions import IsAnalystOrReadOnly, IsReportOwnerOrReadOnly

class ReportListCreateView(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsAnalystOrReadOnly]

    def get_queryset(self):
        if self.request.user.role == 'analyst':
            return Report.objects.filter(author=self.request.user)
        return Report.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsReportOwnerOrReadOnly]

class TeamReportsView(generics.ListAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Report.objects.filter(team_id=team_id)

class UpdateReportStatusView(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated, IsReportOwnerOrReadOnly]

    def patch(self, request, *args, **kwargs):
        report = self.get_object()
        status_value = request.data.get('status')
        if status_value:
            report.status = status_value
            report.save()
            return Response(ReportSerializer(report).data)
        return Response({'detail': 'Missing status'}, status=status.HTTP_400_BAD_REQUEST)