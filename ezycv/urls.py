from django.conf.urls import patterns, include, url
from django.contrib import admin
import main.views as v

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ezycv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^try/(?P<id>[\*\w\-]+)$', 'main.views.resume', name = 'testing'),
    url(r'^$',v.index),
    url(r'^facebook_auth/?$',v.MyChatBotView.as_view()),
    #url(r'^resume/(?P<search_string>\d+)$', 'main.views.resume', name = 'testing'),

)
