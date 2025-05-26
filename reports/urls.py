from django.urls import path
from .views import ReportListCreateView, ReportDetailView, TeamReportsView, UpdateReportStatusView

urlpatterns = [
    path('', ReportListCreateView.as_view(), name='report-list-create'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('team/<int:team_id>/', TeamReportsView.as_view(), name='team-reports'),
    path('<int:pk>/status/', UpdateReportStatusView.as_view(), name='update-status'),
]