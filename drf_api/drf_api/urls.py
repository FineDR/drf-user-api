from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Define Swagger schema view
schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="Detailed API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/contract/', include('contract.urls')),
    path('api/notification/', include('notification.urls')),
    path('api/assets/', include('assets.urls')),
    path('api/logs/', include('auditLog.urls')),
    path('api/payments/', include('payment.urls')),
    
    # Swagger UI documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    
    # ReDoc UI documentation (optional)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
