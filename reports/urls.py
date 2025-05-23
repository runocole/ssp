from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, ReportViewSet,LoginView,RegisterView

router=DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'reports', ReportViewSet, basename='reports')

urlpatterns=[
    path('', include (router.urls)),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),

]