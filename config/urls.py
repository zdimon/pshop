from django.conf.urls import patterns, include, url
from django.contrib import admin
from catalog.views import JournalListView, JournalDetailView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib.flatpages import views
admin.autodiscover()
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

   

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'main.views.home', name='home'),
     url(r'^buy/(?P<id>[^\.]+).html', 'catalog.views.buy', name="buy"),
     url(r'^payment/(?P<id>[^\.]+).html', 'catalog.views.payment', name="payment"),
     url(r'^report/(?P<time>[^\.]+)/(?P<sign>[^\.]+)', 'catalog.views.report', name="report"),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^liqpay/', include('liqpay.urls')),
     url(r'^redactor/', include('redactor.urls')),
     url(r'^change_language/', 'main.views.change_language', name='change_language'),
     url(r'^rosetta/', include('rosetta.urls')),
     url(r'^reg/', 'catalog.views.reg'),
     url(r'^', include('paymaster.urls')),
    url(r'^reset/$', password_reset,  name='reset-password'),
    url(r'^reset/done/', password_reset_done,name="password_reset_done"),
    url(r'^reset/complete', password_reset_complete,name="password_reset_complete"),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',name="password_reset_confirm"),
)


urlpatterns += i18n_patterns(
    '',
    url(r'^catalog/(?P<slug>[^\.]+).html', JournalListView.as_view(), name="catalog"),
    url(r'^journal/(?P<slug>[^\.]+).html', JournalDetailView.as_view(), name="journal"),
    url(r'^about-us/$', views.flatpage, {'url': '/about/'}, name='about'),
    url(r'^contact/$', views.flatpage, {'url': '/contact/'}, name='contact'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^page/(?P<slug>\w+)$', 'page.views.show', name='page'),
     url(r'^accounts/', include('registration.urls')),
     url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
     url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    )

if settings.DEBUG:
    urlpatterns += patterns('',
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),

     )

urlpatterns += staticfiles_urlpatterns()
