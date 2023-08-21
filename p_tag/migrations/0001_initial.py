# Generated by Django 4.2.4 on 2023-08-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=15, verbose_name="태그명")),
            ],
            options={
                "verbose_name": "부트캠퍼스 태그",
                "verbose_name_plural": "부트캠퍼스 태그",
                "db_table": "bootcampus_tag",
            },
        ),
    ]
