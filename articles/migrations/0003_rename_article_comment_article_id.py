# Generated by Django 4.2.4 on 2023-08-25 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_artivle_comment_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='article_id',
        ),
    ]
