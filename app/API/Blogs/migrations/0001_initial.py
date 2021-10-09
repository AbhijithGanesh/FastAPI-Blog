# Generated by Django 3.2.7 on 2021-10-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_creation', models.DateTimeField(auto_created=True)),
                ('Title', models.CharField(default='No Title', max_length=255)),
                ('SubTitle', models.CharField(default='No SubTitle', max_length=255)),
                ('Content', models.TextField()),
                ('URL', models.URLField()),
            ],
        ),
    ]