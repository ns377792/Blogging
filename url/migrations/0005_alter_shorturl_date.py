# Generated by Django 3.2.8 on 2021-12-28 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0004_shorturl_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
