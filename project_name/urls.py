from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse, HttpResponsePermanentRedirect

from ratelimitbackend import admin
admin.autodiscover()

robots = lambda _: HttpResponse('User-agent: *\nDisallow:\n',
                                mimetype='text/plain')

favicon = lambda _: HttpResponsePermanentRedirect(
    '{0}core/img/favicon.png'.format(settings.STATIC_URL)
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('ratelimitbackend.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^robots.txt$', robots),
    url(r'^favicon.ico$', favicon),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
