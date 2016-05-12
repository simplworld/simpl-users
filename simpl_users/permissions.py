from django.contrib.auth.mixins import UserPassesTestMixin


class PermissionMixin(object):
    """
    This Mixin manages permissions for:
        - facilitators
        - game masters
        - professors
        - superusers
    """

    def is_facilitator(self):
        """
        TODO: Remove / update based on (PDLL-11)

        This needs revisited needs to be similar to:

            `return self.request.user.run_user.facilitator()`

        """

        return self.request.user.groups.filter(name='Facilitator')

    def is_game_manager(self):
        """
        TODO: Remove / update based on (PDLL-11)

        This needs revisited needs to be similar to:

            `return self.request.user.run_user.game_manager()`

        """

        return self.request.user.groups.filter(name='Game Manager')

    def is_professor(self):
        return self.request.user.groups.filter(name='Professor')

    def is_superuser(self):
        return self.request.user.is_superuser()


class InFacilitatorGroupMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        return self.is_facilitator()


class InGameManagerGroupMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        return self.is_game_manager()


class InProfessorGroupMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        return self.is_professor()


class InSuperuserGroupMixin(PermissionMixin, UserPassesTestMixin):

    def test_func(self):
        return self.is_superuser()
