# Generated by Django 4.2.4 on 2023-08-16 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("k_sellboard", "0002_alter_product_options_alter_product_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="seller",
        ),
    ]