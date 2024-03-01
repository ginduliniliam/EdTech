# Generated by Django 5.0.2 on 2024-03-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_alter_product_max_users_alter_product_min_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='max_users',
            field=models.IntegerField(default=10, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='min_users',
            field=models.IntegerField(default=1, blank=True, null=True),
        ),
    ]
