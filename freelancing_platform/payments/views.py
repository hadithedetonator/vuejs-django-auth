# payments/views.py
from rest_framework import generics
from .models import Payment, Milestone
from .serializers import PaymentSerializer, MilestoneSerializer

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class MilestoneCreateView(generics.CreateAPIView):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
