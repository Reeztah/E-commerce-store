# Generated by Django 4.2.4 on 2023-09-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_rename_wishlist_wishlist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
