from rest_framework.serializers import ModelSerializer

from .. import models


class UserSerializer(ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'canvas_id',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'subscriber_code',
            'data',
        )
