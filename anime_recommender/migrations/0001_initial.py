# Generated by Django 3.0.3 on 2020-08-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_id', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
                ('episode', models.IntegerField(max_length=10)),
                ('rating', models.IntegerField(max_length=3)),
                ('member', models.IntegerField(max_length=10)),
            ],
        ),
    ]