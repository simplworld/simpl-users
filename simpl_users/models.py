# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.postgres.fields import JSONField
from django.core.urlresolvers import reverse
from django.db import models

from cuser.models import AbstractCUser


class User(AbstractCUser):
    external_id = models.CharField(max_length=50, blank=True, null=True)
    data = JSONField(blank=True, null=True)

    # These are for "GIST Python Django" Compatability
    subscriber_code = models.CharField('Subscriber Code', max_length=255, blank=True)
    faculty = models.BooleanField(default=False, db_index=True)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'pk': self.pk})
