# Generated by Django 3.0.3 on 2020-07-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0002_auto_20200730_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=10),
        ),
    ]
