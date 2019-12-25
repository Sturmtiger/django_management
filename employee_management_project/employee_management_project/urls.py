"""employee_management_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from management_app.api.urls import router

urlpatterns = [
    path('', include('management_app.urls', namespace='management_app')),
    path('', include('auth_app.urls')),
    # Django authentication
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('docs/', get_swagger_view(title='Management API'), name='docs'),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    # DRF API authentication(same session with Django)
    path('api-auth/', include('rest_framework.urls')),
]