from django.conf.urls import patterns, include, url
from django.contrib import admin
import main.views as v

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ezycv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^try$', 'main.views.try_test', name = 'testing'),

)
