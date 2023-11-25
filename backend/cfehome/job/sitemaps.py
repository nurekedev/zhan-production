from django.contrib.sitemaps import Sitemap
from .models import *


class VacancySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Vacancy.objects.filter(status=Vacancy.PUBLISHED)

    def lastmod(self, obj):
        return obj.publish