from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication


class AutoLoginAuthentication(BaseAuthentication):
    def authenticate(self, request):
        User = get_user_model()
        user = User.objects.first()
        if not user:
            user = User.objects.create_user("test@test.com", password="test")

        return (user, None)
