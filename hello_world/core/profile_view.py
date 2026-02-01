from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile

def profile(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    message = None
    if request.method == 'POST':
        if 'join' in request.POST:
            profile.membership = 'premium'
            profile.save()
            message = 'You have joined Premium membership.'
        elif 'leave' in request.POST:
            profile.membership = 'free'
            profile.save()
            message = 'You have left Premium membership.'
        elif 'membership' in request.POST:
            membership = request.POST.get('membership')
            if membership in dict(UserProfile.MEMBERSHIP_CHOICES):
                profile.membership = membership
                profile.save()
                message = f'Membership updated to {profile.get_membership_display()}.'
    return render(request, 'profile.html', {'profile': profile, 'message': message})
