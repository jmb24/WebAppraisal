from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from src.webapp.models import Profile

# empty url - redirect user to login/welcome page
def redirect_to_login(request):
    return redirect('/welcome/')

# login page - default when first opening the webapp
def login_view(request):
    return render(request, 'coming-soon.html')

# for new users to create an account
def create_account_view(request):
    return render(request, 'coming-soon.html')

# home page for both appraisers and their customers
def dashboard_view(request, user_id):
    user = User.objects.get(pk=user_id)
    role = user.profile.role
    if role is Profile.Roles.APPRAISER:
        # prepare dashboard for appraiser
        return render(request, 'coming-soon.html')
    elif role is Profile.Roles.CUSTOMER:
        # prepare dashboard for customer
        return render(request, 'coming-soon.html')
    else:
        raise TypeError('Unknown user type %s', role)

