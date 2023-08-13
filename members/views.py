from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Replace 'profile' with the URL name of your member profile page
        else:
            # Invalid credentials, show an error message
            error_message = 'Invalid login credentials'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile_view(request):
    # Retrieve and display the member's profile
    # Add your logic here to fetch and render the member's profile
    return render(request, 'profile.html')
