# Generated by Django 3.1.1 on 2020-11-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0008_auto_20201022_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='stu_img',
            field=models.ImageField(default='images/default.png', upload_to='images'),
        ),
    ]