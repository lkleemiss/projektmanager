from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def register(request):
    """
    Provides the User Create Form, saves the user after registration and sends him a mail
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            # MAIL
            email_template = render_to_string('core/email_register_template.html')
            email = EmailMessage(
                'Registrierung beim Projektmanager',
                email_template,
                settings.EMAIL_HOST_USER,
                [user.email],
            )
            email.send(fail_silently=False)

            login(request, user)
            return redirect('startpage')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/register.html', {'form': form})
