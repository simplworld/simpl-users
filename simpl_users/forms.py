from django import forms

from . import models


class UserForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'lms_id',
            # 'is_superuser',
            # 'is_staff',
            'is_active',
        ]
