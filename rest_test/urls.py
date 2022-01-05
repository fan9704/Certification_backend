"""rest_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restfulapi import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views  
from django.contrib.auth import views as view
# ---product list
router = DefaultRouter()
router.register('', views.CertificationViewSet)
app_name = 'Certification list'
# ---
schema_view = get_schema_view(
    openapi.Info(
        title="Certification API",
        default_version='v1',
        description="Certification Swagger API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cxz123499@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path("api/certification/", views.certification_api_view, name="certification"),
    path('api/certifications/', include(router.urls)),
    path('api/accounts/login/', views.loginAPI.as_view()),
    path('api/accounts/logout/', views.loginAPI.as_view()),
    # path('api/accounts/login/', view.LoginView.as_view()),
    # path('api/accounts/logout/', view.LogoutView.as_view()),
    path('api/accounts/register/', views.registerAPI.as_view()),
    path("api/accounts/profile/", views.editprofileAPI.as_view()),
    
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),     
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), 

    path('(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
