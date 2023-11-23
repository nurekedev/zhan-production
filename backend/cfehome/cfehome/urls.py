"""cfehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularSwaggerView, 
    SpectacularRedocView)

from job.views import main_lite_form


# from .routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/vacancies/', include('job.urls')),
    path('submit-contact/', main_lite_form, name='submitcontact'),
    path('__debug__/', include(debug_toolbar.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
     path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema/swagger-ui/",
         SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui")
]

urlpatterns += [path('jsi18n/', JavaScriptCatalog.as_view())]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
