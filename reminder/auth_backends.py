
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User  # Import your custom user model

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        # Implement your custom authentication logic here
        # For example, query the database to authenticate the user
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
