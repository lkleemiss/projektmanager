from django.db.models import Q


def user_projects(request):
    if request.user.is_authenticated:
        user_projects = request.user.projects.all()
        projects_completed = user_projects.filter(status='finished')
        projects_active = user_projects.filter(status='active')
        projects_current = user_projects.filter(
            ~Q(status='finished') & ~Q(status='closed')
        )

        return {'projects': request.user.projects.all().order_by('-last_change'),
                'projects_completed': projects_completed, 'projects_active': projects_active,
                'projects_current': projects_current}
    return {}
