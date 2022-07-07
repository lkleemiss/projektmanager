from django.urls import path

from .views import add_project, projects, project, edit_project, delete_project, start_time, \
    project_new_member, add_time_entry

urlpatterns = [
    path('projekt-neu/', add_project, name='project_add'),
    path('projekte/', projects, name='projects'),
    path('projekt/<int:project_id>/', project, name='project'),
    path('projekt/<int:project_id>/start-tracking', start_time, name='start_tracking'),
    path('projekt/<int:project_id>/neue-zeit', add_time_entry, name='project_add_time_entry'),
    path('projekt/<int:project_id>/neues-mitglied', project_new_member, name='project_new_member'),
    path('projekt/entfernen/<int:project_id>/', delete_project, name='project_delete'),
    path('projekt/<int:project_id>/bearbeiten', edit_project, name='project_edit'),
]
