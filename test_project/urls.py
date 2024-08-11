from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.authentication_app.urls")),
    path("booking/", include("apps.booking_app.urls")), 
    
    #swagger UI paths
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema')),
]


# 5.in views after class and befor fn
#     @extend_schema(
#     request=,
#     responses=,
#     operation_id="Middleware",    
#     description="Root API which recieve a data from frontend and trigger the services like Structural calc, systemsize calc, system characteristic calc , ocpd calculation etc and gives a final response of all calculated values",
#     ) 