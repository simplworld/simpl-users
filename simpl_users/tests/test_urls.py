# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url


# Our application urls
urlpatterns = [
    url(r'^users/', include('simpl_users.urls', namespace='users')),
    # url(r'^apis/', include(api_router.urls, namespace='simpl_api')),
    # url(r'^docs/', include('rest_framework_swagger.urls')),
]
