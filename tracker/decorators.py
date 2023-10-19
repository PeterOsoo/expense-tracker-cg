from django.shortcuts import redirect


def redirect_logged_in_user(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('expense_list')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
