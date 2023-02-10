from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_tasks', views.UserTaskListView.as_view(), name='user_task_list'),
    path('my_tasks/<int:pk>', views.UserTaskDetailView.as_view(), name='user_task_single'),
    path('my_tasks/new', views.UserTaskCreateView.as_view(), name='user_task_new'),
    path('my_tasks/<int:pk>/update', views.UserTaskUpdateView.as_view(), name='user_task_update'),
    path('my_tasks/<int:pk>/delete', views.UserTaskDeleteView.as_view(), name='user_task_delete'),
    path('register/', views.register, name='register'),
]