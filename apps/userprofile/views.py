from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Userprofile


@login_required
def profile(request, userprofile_id=None):
    """
    Provides userprofil
    """
    if userprofile_id:
        userprofil = Userprofile.objects.get(pk=userprofile_id)
    else:
        userprofil = request.user.userprofile

    return render(request, 'userprofile/profile.html', {'userprofil': userprofil})


@login_required
def edit_Profile(request):
    """
    Provites the Prodile edit template and updates the userprofil with given attr from forms
    """
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email = request.POST.get('email', '')
        request.user.save()

        userprofile = request.user.userprofile

        if request.POST.get('image_delete', False):
            userprofile.image.delete()

        if request.FILES:
            image = request.FILES['image']
            userprofile.image = image

        userprofile.save()
        messages.info(request, 'Die Änderungen wurden gespeichert.')
        return redirect('profile')

    return render(request, 'userprofile/editProfile.html')
