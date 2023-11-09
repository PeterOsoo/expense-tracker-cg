# middleware.py


from django.shortcuts import redirect
from django.urls import reverse


class LogoutConfirmationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path != reverse('logout_confirmation'):
            # User is logged in and not accessing logout-confirmation
            # Do not log them out, and redirect them to the desired location (e.g., home)
            return redirect('home')
        elif request.user.is_authenticated and request.path == reverse('logout_confirmation'):
            # User is logged in and trying to access logout-confirmation, log them out
            from django.contrib.auth import logout
            logout(request)

        response = self.get_response(request)
        return response
