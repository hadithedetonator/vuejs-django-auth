# notifications/urls.py
from django.urls import path
from .views import NotificationListView, NotificationMarkAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications_list'),
    path('<int:pk>/mark-as-read/', NotificationMarkAsReadView.as_view(), name='notification_mark_as_read'),
]
