# Generated by Django 2.1.1 on 2018-10-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20181003_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
    ]