from django.contrib.sitemaps import Sitemap
from catalog.models import Journal

class CatalogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Journal.objects.all()

