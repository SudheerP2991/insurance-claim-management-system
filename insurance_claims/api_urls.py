from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ClaimViewSet

# Set up the router for Claim API
router = DefaultRouter()
router.register(r'claims', ClaimViewSet)

urlpatterns = [
    # Claim API endpoints
    path('api/', include(router.urls)),

    # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
