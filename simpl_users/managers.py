from django.db import models
from django.contrib.auth.models import UserManager


class UserQuerySet(models.QuerySet):
    """ QuerySet to access Users """


class UserManager(UserManager):
    """ Corresponding Manager to query Users """

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)
