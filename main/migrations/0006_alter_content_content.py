# Generated by Django 4.2.1 on 2023-05-29 04:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_content_content_menu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
