# Generated by Django 3.0.6 on 2020-07-03 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poolServices', '0004_auto_20200703_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='poolServices/images/'),
        ),
    ]