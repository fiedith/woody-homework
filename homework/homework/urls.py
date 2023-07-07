from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token

from users.views import UserView

...

schema_view = get_schema_view(
   openapi.Info(
      title="Homework Board API",
      default_version='v1',
      description="API Documentation for boards",
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', UserView.as_view(), name='user-api'),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]