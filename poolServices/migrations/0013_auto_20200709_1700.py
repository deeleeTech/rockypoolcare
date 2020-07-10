# Generated by Django 3.0.6 on 2020-07-09 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poolServices', '0012_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='reviewComment',
        ),
        migrations.AddField(
            model_name='review',
            name='comments',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]