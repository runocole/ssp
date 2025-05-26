from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def role_required(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not hasattr(request.user, 'role') or request.user.role not in allowed_roles:
                return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

coach_required = role_required(['coach'])
analyst_required = role_required(['analyst'])