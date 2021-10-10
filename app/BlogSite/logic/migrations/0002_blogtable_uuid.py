# Generated by Django 3.2.7 on 2021-10-10 16:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtable',
            name='UUID',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]