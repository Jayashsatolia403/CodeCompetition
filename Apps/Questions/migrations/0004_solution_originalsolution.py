# Generated by Django 3.1 on 2021-05-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0003_auto_20210523_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='originalSolution',
            field=models.FileField(blank=True, null=True, upload_to='Apps/Questions/Answers/Questions/'),
        ),
    ]
