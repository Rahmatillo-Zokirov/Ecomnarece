from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from Core import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Ecommerce API",
      default_version='v1',
      description="Ecommerce API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="#"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),


    path('users/', include('userApp.urls')),
    path('action/', include('actionApp.urls')),
    path('core/', include('coreApp.urls')),
    path('order/', include('orderApp.urls')),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

