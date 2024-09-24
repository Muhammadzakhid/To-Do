from django.urls  import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('edit/<int:task_id>/', views.tasks_edit, name="task_edit"),
    path('delete/<int:task_id>/', views.task_delete, name="task_delete"),
]