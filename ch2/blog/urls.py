from django.conf.urls import url
from blog.views import *

urlpatterns = [
    # /
    url(r'^$', PostLV.as_view(), name='index'),
    # /post/
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    # /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    # /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    # /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_archive_year'),
    # /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_archive_month'),
    # /2012/nov/10
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_archive_day'),
    # /today/
    url(r'^today/$', PostTAV.as_view(), name='post_archive_today'),
]
