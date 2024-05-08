
def get_current_user(request=None):
    if request and request.user.is_authenticated:
        return request.user
    else:
        return None