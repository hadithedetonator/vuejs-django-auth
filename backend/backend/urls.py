# main urls.py (e.g., project_name/urls.py)
from django.contrib import admin
from django.urls import path, include  # Import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include your app's URLs for Swagger
    path('api/', include('app.urls')),  # Update with your app's name
]
