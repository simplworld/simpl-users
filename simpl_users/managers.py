from django.db import models
from django.contrib.auth.models import UserManager


class UserQuerySet(models.QuerySet):
    """ QuerySet to differentiate between faculty and students """

    def faculty(self):
        return self.filter(faculty=True)

    def students(self):
        return self.filter(faculty=False)


class UserManager(UserManager):
    """ Corresponding manager to differentiate between faculty and students """

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def faculty(self):
        return self.get_queryset().faculty()

    def students(self):
        return self.get_queryset().students()
