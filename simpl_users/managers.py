from django.db import models
from django.contrib.auth.models import UserManager


class UserQuerySet(models.QuerySet):
    """ QuerySet to differentiate between faculty and students """


class UserManager(UserManager):
    """ Corresponding manager to differentiate between faculty and students """

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)
