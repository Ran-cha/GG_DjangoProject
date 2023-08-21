# Generated by Django 4.2.4 on 2023-08-17 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("bcuser", "0002_bcuser_nickname"),
        ("k_sellboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(verbose_name="수량")),
                (
                    "register_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="주문날짜"),
                ),
                (
                    "bcuser",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bcuser.bcuser",
                        verbose_name="사용자",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="k_sellboard.product",
                        verbose_name="상품",
                    ),
                ),
            ],
            options={
                "verbose_name": "주문",
                "verbose_name_plural": "주문들",
                "db_table": "bootcampus_order",
            },
        ),
    ]
