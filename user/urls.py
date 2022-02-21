
from django.urls import path, include

from user.views import UserViewSet


urlpatterns = [
    path('account/', UserViewSet.as_view({'post': 'accounts', 'get': 'accounts'})),
    path('login/', UserViewSet.as_view({'post': 'login', 'get':'login'})),
]

