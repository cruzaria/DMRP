from django.conf import settings
from django.conf.urls import include, url
from django.views.decorators.cache import cache_page
from django.contrib import admin
from base import views as base_views

from testapp import views as test_views




urlpatterns = [
    url(r'^api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^api/v1/getdata/', include('base.urls', namespace='base')),
    url(r'^test/$', test_views.test, name='test'),
    url(r'^admin/', admin.site.urls),
    # the DMP router - if DEFAULT_HOMEPAGE is set, this should be the last pattern (the wildcards match everything)
    url('^homepage', include('django_mako_plus.urls')),
    # catch all others because of how history is handled by react router - cache this page because it will never change
    url(r'', cache_page(settings.PAGE_CACHE_SECONDS)(base_views.IndexView.as_view()), name='index'),
]
