# Generated by Django 2.2.14 on 2021-01-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210127_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('10', 'discount 10%'), ('5', 'discount 5%')], default=None, max_length=2, null=True),
        ),
    ]
