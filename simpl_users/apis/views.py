from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .. import models


# Mixins

class CommonViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


# ViewSets

class UserViewSet(CommonViewSet):
    """ User resource. """

    queryset = models.User.objects.all()
    filter_fields = (
        'canvas_id',
        'is_active',
        'is_staff',
        'is_superuser',
        'email',
        'pk',
        'subscriber_code',
    )
    lookup_field = 'pk'
    ordering_fields = ()

    def get_serializer(self, *args, **kwargs):
        # Only allow admin users to update passwords
        if self.request.user.is_staff:
            return serializers.UserUpdateSerializer(*args, **kwargs)
        else:
            return serializers.UserSerializer(*args, **kwargs)

    def destroy(self, request, pk=None):
        """
        Delete an User
        """
        return super(UserViewSet, self).destroy(request, pk=pk)

    def list(self, request):
        """
        Returns a list of User
        ---
        parameters:
            - name: canvas_id
              type: integer
              paramType: query
              required: false
              description: Filters User per Canvas ID via canvas_id
            - name: is_active
              type: boolean
              paramType: query
              required: false
              description: Filters User per Is Active via is_active
            - name: is_staff
              type: boolean
              paramType: query
              required: false
              description: Filters User per Is Staff via is_staff
            - name: is_superuser
              type: boolean
              paramType: query
              required: false
              description: Filters User per Is Superuser via is_superuser
            - name: subscriber_code
              type: string
              paramType: query
              required: false
              description: Filters User per Subscriber Code via subscriber_code
            - name: username
              type: string
              paramType: query
              required: false
              description: Filters User per Username via username
        """
        return super(UserViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing User
        """
        return super(UserViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an User by username
        """
        return super(UserViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing User
        """
        return super(UserViewSet, self).update(request, pk=pk)
