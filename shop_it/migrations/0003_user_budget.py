# Generated by Django 2.2.4 on 2019-08-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_it', '0002_auto_20190806_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='budget',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]