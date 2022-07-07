from django.urls import path

from .views import edit_time_entry, delete_time_entry

urlpatterns = [
    path('projekt/<int:project_id>/zeit/<int:time_entry_id>/', edit_time_entry, name='timeentry_edit'),
    path('projekt/entfernen/<int:project_id>/zeit/<int:time_entry_id>/', delete_time_entry, name='timeentry_delete'),
]
