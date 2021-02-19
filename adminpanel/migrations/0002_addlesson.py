# Generated by Django 3.1.1 on 2020-10-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addlesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('desc', models.TextField(max_length=70)),
                ('course_id', models.CharField(max_length=70)),
                ('course_name', models.CharField(max_length=70)),
                ('video_link', models.FileField(upload_to='video')),
            ],
        ),
    ]
