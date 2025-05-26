from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication

class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_auth = JWTAuthentication()
        try:
            user, _ = user_auth.authenticate(request)
            request.user = user
        except:
            request.user = None
        return self.get_response(request)