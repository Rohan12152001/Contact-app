# Generated by Django 3.0.3 on 2020-07-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0004_auto_20200730_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]
