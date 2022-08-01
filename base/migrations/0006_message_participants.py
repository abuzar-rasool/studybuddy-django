# Generated by Django 4.0.6 on 2022-07-31 10:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0005_message_created_at_message_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
