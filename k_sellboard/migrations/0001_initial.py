# Generated by Django 4.2.4 on 2023-08-16 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bcuser", "0002_bcuser_nickname"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=256, verbose_name="상품명")),
                ("price", models.IntegerField(verbose_name="상품가격")),
                ("description", models.TextField(verbose_name="상품설명")),
                ("stock", models.IntegerField(verbose_name="재고")),
                (
                    "register_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록날짜"),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bcuser.bcuser",
                        verbose_name="판매자",
                    ),
                ),
            ],
        ),
    ]
