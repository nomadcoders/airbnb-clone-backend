from rest_framework import authentication
from rest_framework import exceptions
from users.models import User


class CustomAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("Trust-Me-Bro")

        if not username:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user.")

        return (user, None)
