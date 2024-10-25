# payments/urls.py
from django.urls import path
from .views import PaymentCreateView, MilestoneCreateView, PaymentDetailView

urlpatterns = [
    path('create/', PaymentCreateView.as_view(), name='create_payment'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('<int:payment_id>/milestones/', MilestoneCreateView.as_view(), name='create_milestone'),
]
