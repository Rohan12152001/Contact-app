# Generated by Django 3.0.3 on 2020-07-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]
