from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from django.contrib import admin
admin.autodiscover()


from main.models import Catalog
class CatalogViewSet(viewsets.ModelViewSet):
    model = Catalog

router = routers.DefaultRouter()
router.register(r'catalog', CatalogViewSet)

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rest/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)
