# Generated by Django 4.2.4 on 2023-08-25 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_article_comment_article_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article',
        ),
    ]