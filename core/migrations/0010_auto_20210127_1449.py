# Generated by Django 2.2.14 on 2021-01-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item'),
        ),
    ]