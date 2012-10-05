from django.conf.urls.defaults import *
 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
 
urlpatterns = patterns('',
    # Example:
    # (r'^hussa/', include('hussa.foo.urls')),
    url(r'^$', 'news.views.index', name='home'),
    url(r'^news/(?P<id>[0-9]+)/$', 'news.views.index_pag', name='home'),
    #admin                   
    (r'^admin/doc/', include('django.contrib.admindocs.urls')), 
    (r'^admin/', include(admin.site.urls)),
    (r'^news/(?P<slug>[\w\-_]+)/$', 'news.views.show_news'),
    #artykuly
    (r'^artykuly/$', 'artykuly.views.index'),
    (r'^artykuly/(?P<slug>[\w\-_]+)/$', 'artykuly.views.show_art'),
    # login
    (r'^login/$','default.views.login_page'),
    (r'^logout/$','default.views.logout_page'),
    # registration
    (r'^register/$','default.views.register_page'),
)
