from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^image/random/', 'imagebrowser.views.random_image'),
    (r'^image/(?P<imageid>.+)/previous/', 'imagebrowser.views.previous_image'),
    (r'^image/(?P<imageid>.+)/next/', 'imagebrowser.views.next_image'),
    (r'^image/(?P<imageid>.+)/rate/', 'imagebrowser.views.rate'),
    (r'^image/(?P<imageid>.+)/favorite/', 'imagebrowser.views.favorite'),
    (r'^image/(?P<imageid>.+)/tag/', 'imagebrowser.views.tag'),
    (r'^image/(?P<imageid>.+)/update_title/', 'imagebrowser.views.update_title'),
    (r'^image/(?P<imageid>.+)/', 'imagebrowser.views.image'),
    (r'^', 'imagebrowser.views.startpage'),
)
