from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog.views import JournalListView, JournalDetailView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'main.views.home', name='home'),
     url(r'^catalog/(?P<slug>[^\.]+).html', JournalListView.as_view(), name="catalog"),
     url(r'^journal/(?P<slug>[^\.]+).html', JournalDetailView.as_view(), name="journal"),

     url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),

     )

urlpatterns += staticfiles_urlpatterns()