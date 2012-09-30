from django.conf.urls import patterns, include, url

from ratelimitbackend import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
