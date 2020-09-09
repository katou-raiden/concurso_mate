def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            for role in allowed_roles:
                if request.user.groups.filter(name=role).exists():
                    return view_function(request, *args, **kwargs)
            return HttpResponse('No tiene permiso para acceder a esa pagina.')
        return wrapper_function
    return decorator
        