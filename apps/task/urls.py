from django.urls import path

from .views import task, edit_task, delete_task, update_task

urlpatterns = [
    path('projekt/<int:project_id>/<int:task_id>/', task, name='task'),
    path('projekt/<int:project_id>/<int:task_id>/bearbeiten', edit_task, name='edit_task'),
    path('projekt/<int:project_id>/<int:task_id>/loeschen', delete_task, name='delete_task'),
    path('projekt/<int:project_id>/<int:task_id>/update', update_task, name='update_task'),
]
