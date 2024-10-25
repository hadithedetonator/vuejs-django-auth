# projects/views.py
from rest_framework import generics
from .models import Project, Bid
from .serializers import ProjectSerializer, BidSerializer

class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class BidCreateView(generics.CreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer