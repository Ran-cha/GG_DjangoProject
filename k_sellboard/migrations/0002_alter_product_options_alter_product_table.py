# Generated by Django 4.2.4 on 2023-08-16 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("k_sellboard", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "상품", "verbose_name_plural": "상품들"},
        ),
        migrations.AlterModelTable(
            name="product",
            table="bootcampus_sellproduct",
        ),
    ]
