# Generated by Django 3.1.1 on 2020-10-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0002_auto_20201015_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=70)),
                ('student_email', models.EmailField(max_length=254)),
                ('course_id', models.CharField(max_length=70)),
                ('status', models.CharField(max_length=70)),
                ('respmsg', models.CharField(max_length=70)),
                ('amount', models.CharField(max_length=70)),
                ('order_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='stu_img',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]