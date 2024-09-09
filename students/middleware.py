import json
from django.core.cache import cache
from django.utils.timezone import now


class LogUserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.log_request(request)
        return response

    def log_request(self, request):
        user = request.user.username if request.user.is_authenticated else "Anonymous"
        log_data = {
            "user": user,
            "path": request.path,
            "method": request.method,
            "timestamp": now().isoformat(),
        }
        log_list = cache.get("user_activity_log", [])
        log_list.append(log_data)
        cache.set("user_activity_log", log_list, None)
