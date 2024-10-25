# projects/urls.py
from django.urls import path
from .views import ProjectCreateView, BidCreateView

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create_project'),
    path('<int:project_id>/bid/', BidCreateView.as_view(), name='create_bid'),
]