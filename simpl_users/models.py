# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


@python_2_unicode_compatible
class User(AbstractUser):
    canvas_id = models.IntegerField(blank=True, null=True)
    data = JSONField(blank=True, null=True)

    # These are for "GIST Python Django" Compatability
    subscriber_code = models.CharField('Subscriber Code', max_length=255, blank=True)
    faculty = models.BooleanField(default=False, db_index=True)

    objects = UserManager()

    class Meta(object):
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
