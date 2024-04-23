# Generated by Django 5.0.4 on 2024-04-23 11:40

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postdisplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postview',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='post_title', unique=True),
        ),
    ]
