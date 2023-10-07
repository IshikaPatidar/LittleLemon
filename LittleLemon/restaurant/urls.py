from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

# router = routers.DefaultRouter()
# router.register(r'menu', MenuItemViewSet, basename="MenuView")
# router.register(r'users', UserViewSet, basename='UserView')

urlpatterns = [
    path('', index),
    path('menuitem/',MenuItemViews.as_view()),
    # path(r'', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('booking_set', BookingSet.as_view()),
    # path('api-token-auth/', obtain_auth_token)
]
