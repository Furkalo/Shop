from django.http import Http404

# Custom function to check if the user is a manager
def is_manager(user):
    try:
        if not user.is_manager:  # Check if user has manager status
            raise Http404  # If not a manager, raise 404 error
        return True
    except:
        raise Http404  # In case of an error, raise 404 error

