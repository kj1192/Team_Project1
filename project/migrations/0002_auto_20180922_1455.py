# Generated by Django 2.1.1 on 2018-09-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytable',
            name='strength',
            field=models.CharField(default='Not', max_length=10),
        ),
        migrations.AlterField(
            model_name='mytable',
            name='stat',
            field=models.CharField(max_length=10),
        ),
    ]
