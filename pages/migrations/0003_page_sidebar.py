# Generated by Django 2.2.12 on 2022-01-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='sidebar',
            field=models.BooleanField(default=False),
        ),
    ]
