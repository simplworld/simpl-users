# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserDetailView
    # This ugly regexp is a negative match on anything that doesn't look like
    # a URL piece.
    url(
        regex=r'^(?P<email>[^\/\#?]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),

    # URL pattern for the UserDeleteView
    url(
        regex=r'^(?P<email>[^\/\#?]+)/delete/$',
        view=views.UserDeleteView.as_view(),
        name='delete'
    ),

    # URL pattern for the ManageUserUpdateView
    url(
        regex=r'^(?P<email>[^\/\#?]+)/update/$',
        view=views.ManageUserUpdateView.as_view(),
        name='user_update'
    ),
]
