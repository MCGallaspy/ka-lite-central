from django.conf.urls.defaults import patterns, url, include


urlpatterns = patterns(__package__ + '.views',
    url(r'^$', 'update', {}, 'update'),
    url(r'^videos/$', 'update_videos', {}, 'update_videos'),
    url(r'^languages/$', 'update_languages', {}, 'update_languages'),
    url(r'^software/$', 'update_software', {}, 'update_software'),

)