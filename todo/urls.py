from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task'),
    path('tasks/create', views.create_task, name='create'),
    path('tasks/update/<int:pk>', views.update_task, name='update'),
    path('tasks/delete/<int:pk>', views.delete_task, name='delete'),
    path('tasks/detail/<int:pk>', views.detail_task, name='detail'),
]
