# freelancing_platform/urls.py
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/workspaces/', include('workspaces.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/notifications/', include('notifications.urls')),
]
