from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog.views import JournalListView, JournalDetailView
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'main.views.home', name='home'),
     url(r'^catalog/(?P<slug>[^\.]+).html', JournalListView.as_view(), name="catalog"),
     url(r'^journal/(?P<slug>[^\.]+).html', JournalDetailView.as_view(), name="journal"),

     url(r'^admin/', include(admin.site.urls)),

)
