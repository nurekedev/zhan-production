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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns


from job.views import main_lite_form, question_contact_form
from job.sitemaps import VacancySitemap


sitemaps = {
    'vacancies': VacancySitemap,
}

urlpatterns = [

    path('grappelli/', include('grappelli.urls')),
    path('admin/', include('admin_honeypot.urls')),
    path('art2qn788npek/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('api/v1/vacancies/', include('job.urls')),
    path('submit-contact/', main_lite_form, name='submitcontact'),
    path('submit-question/', question_contact_form, name='submitquestion'),
)


