# Generated by Django 3.0.3 on 2020-08-04 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime_recommender', '0002_auto_20200804_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anime',
            old_name='episode',
            new_name='episodes',
        ),
        migrations.RenameField(
            model_name='anime',
            old_name='member',
            new_name='members',
        ),
    ]