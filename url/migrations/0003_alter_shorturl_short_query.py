# Generated by Django 3.2.8 on 2021-12-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0002_rename_origin_url_shorturl_original_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_query',
            field=models.CharField(max_length=16),
        ),
    ]
