from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def private_storage_auth(request):
    if not request.user.is_staff:
        return HttpResponseForbidden('Access denied.')
