from django.urls import path
from .views import UserCreateView, UserDeleteView

app_name = 'users'

urlpatterns = [
    path('', UserCreateView.as_view(), name='user-api'),
    path('<int:pk>', UserDeleteView.as_view(), name='user-delete'),
]