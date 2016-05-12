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
    serializer_class = serializers.UserSerializer
    filter_fields = (
        'canvas_id',
        'is_active',
        'is_staff',
        'is_superuser',
        'subscriber_code',
    )
    ordering_fields = ()

    def create(self, request):
        """
        Add a new User
        """
        return super(UserViewSet, self).create(request)

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
              description: Filters User per canvas_id via canvas_id
            - name: is_active
              type: boolean
              paramType: query
              required: false
              description: Filters User per is_active via is_active
            - name: is_staff
              type: boolean
              paramType: query
              required: false
              description: Filters User per is_staff via is_staff
            - name: is_superuser
              type: boolean
              paramType: query
              required: false
              description: Filters User per is_superuser via is_superuser
            - name: subscriber_code
              type: string
              paramType: query
              required: false
              description: Filters User per subscriber_code via subscriber_code
        """
        return super(UserViewSet, self).list(request)

    def partial_update(self, request, pk=None):
        """
        Update an existing User
        """
        return super(UserViewSet, self).partial_update(request, pk=pk)

    def retrieve(self, request, pk=None):
        """
        Find an User by ID
        """
        return super(UserViewSet, self).retrieve(request, pk=pk)

    def update(self, request, pk=None):
        """
        Update an existing User
        """
        return super(UserViewSet, self).update(request, pk=pk)
