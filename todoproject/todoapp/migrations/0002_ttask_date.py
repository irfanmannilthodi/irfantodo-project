# Generated by Django 4.2.7 on 2023-12-04 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttask',
            name='date',
            field=models.DateField(default='1999-05-31'),
            preserve_default=False,
        ),
    ]
