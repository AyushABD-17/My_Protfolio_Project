# Generated by Django 4.1.5 on 2023-03-19 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfolio', '0002_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='name',
            field=models.CharField(default='apple', max_length=50),
        ),
    ]
