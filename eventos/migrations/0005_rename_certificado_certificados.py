# Generated by Django 4.2.3 on 2023-07-16 14:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0004_certificado'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certificado',
            new_name='Certificados',
        ),
    ]
