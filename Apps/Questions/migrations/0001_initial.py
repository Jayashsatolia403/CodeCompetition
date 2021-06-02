# Generated by Django 3.1.7 on 2021-05-22 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('statement', models.TextField()),
                ('example1', models.CharField(blank=True, max_length=250, null=True)),
                ('example2', models.CharField(blank=True, max_length=250, null=True)),
                ('example3', models.CharField(blank=True, max_length=250, null=True)),
                ('constraints', models.CharField(blank=True, max_length=250, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='upload/questions/')),
                ('dificulty', models.CharField(blank=True, max_length=250, null=True)),
                ('relatedTopics', models.CharField(blank=True, max_length=250, null=True)),
                ('relatedQuestions', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('language', models.CharField(max_length=10)),
                ('questionForSolution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionForSolution', to='Questions.questions')),
            ],
        ),
    ]
