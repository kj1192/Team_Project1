# Generated by Django 2.1.1 on 2018-09-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mytable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('tmp', models.CharField(max_length=10)),
                ('stat', models.IntegerField(default=0)),
            ],
        ),
    ]
