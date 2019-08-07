# Generated by Django 2.2.4 on 2019-08-07 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_it', '0003_user_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelf',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='shelf',
            name='shelf_third',
        ),
        migrations.CreateModel(
            name='ShelfSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_third', models.CharField(default='Front-Third', max_length=225)),
                ('product_id', models.ManyToManyField(related_name='products', to='shop_it.Product')),
            ],
        ),
        migrations.AddField(
            model_name='shelf',
            name='shelf_third',
            field=models.ManyToManyField(related_name='shelf_sections', to='shop_it.ShelfSection'),
        ),
    ]