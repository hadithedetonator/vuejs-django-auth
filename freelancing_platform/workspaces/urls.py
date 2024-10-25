# workspaces/urls.py
from django.urls import path
from .views import WorkspaceCreateView, TaskCreateView, WorkspaceDetailView

urlpatterns = [
    path('create/', WorkspaceCreateView.as_view(), name='create_workspace'),
    path('<int:pk>/', WorkspaceDetailView.as_view(), name='workspace_detail'),
    path('<int:workspace_id>/tasks/', TaskCreateView.as_view(), name='create_task'),
]
