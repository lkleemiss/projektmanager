from django.shortcuts import render, redirect


def startpage(request):
    """
    Redirects to Dashboard when user ist logged in,
    if not renders startpage template
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'core/startpage.html')


def error_404_view(request, exception):
    """ Renders the 404 Error-Handling page template """
    return render(request, 'core/404.html')


def dashboard(request):
    """ Renders the Dashboard Template """
    return render(request, 'core/dashboard.html')
