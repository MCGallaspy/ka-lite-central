from django.http import HttpResponseRedirect
from django.conf.urls.defaults import patterns, include, url
import securesync.urls
from kalite import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^securesync/', include(securesync.urls)),
)

urlpatterns += patterns('',
    url(r'^' + settings.STATIC_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
    url(r'^' + settings.CONTENT_URL[1:] + '(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.CONTENT_ROOT,
    }),
)
        
# Javascript translations
urlpatterns += patterns('',
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('ka-lite.locale')}, 'i18n_javascript_catalog'),
)

from feeds import RssSiteNewsFeed, AtomSiteNewsFeed

urlpatterns += patterns('central.views',
    url(r'^$', 'homepage', {}, 'homepage'), 
    url(r'^delete_admin/(?P<org_id>\w+)/(?P<user_id>\w+)/$', 'delete_admin', {}, 'delete_admin'), 
    url(r'^delete_invite/(?P<org_id>\w+)/(?P<invite_id>\w+)/$', 'delete_invite', {}, 'delete_invite'), 
    url(r'^accounts/', include('registration.urls')),
    url(r'^organization/(?P<id>\w+)/$', 'organization_form', {}, 'organization_form'),
    url(r'^organization/(?P<org_id>\w+)/zone/(?P<id>\w+)/$', 'zone_form', {}, 'zone_form'),
    url(r'^organization/invite_action/(?P<invite_id>\w+)/$', 'org_invite_action', {}, 'org_invite_action'),
    url(r'^organization/(?P<org_id>\w+)/zone/(?P<zone_id>\w+)/facility/$', 'central_facility_admin', {}, 'central_facility_admin'),
    url(r'^organization/(?P<org_id>\w+)/zone/(?P<zone_id>\w+)/facility/new/$', 'central_facility_edit', {"id": "new"}, 'central_facility_add'),
    url(r'^organization/(?P<org_id>\w+)/zone/(?P<zone_id>\w+)/facility/(?P<id>\w+)/$', 'central_facility_edit', {}, 'central_facility_edit'),
    url(r'^cryptologin/$', 'crypto_login', {}, 'crypto_login'), 
#    url(r'^getstarted/$','get_started', {}, 'get_started'),
    url(r'^glossary/$', 'glossary', {}, 'glossary'),
    url(r'^addsubscription/$', 'add_subscription', {}, 'add_subscription'),
    url(r'^feeds/rss/$', RssSiteNewsFeed(), {}, 'rss_feed'),
    url(r'^feeds/atom/$', AtomSiteNewsFeed(), {}, 'atom_feed'),
    url(r'^faq/', include('faq.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^install/$', 'install_wizard', {}, 'install_wizard'),
    url(r'^wiki/(?P<wurl>\w+)/$', redirect_to, {'url': settings.CENTRAL_WIKI_URL}),
    url(r'^about/$', redirect_to, { 'url': 'http://learningequality.org/' }),
)

handler404 = 'main.views.central_404_handler'
handler500 = 'main.views.central_500_handler'

