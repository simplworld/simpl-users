# Generated by Django 2.2 on 2019-08-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpl_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
