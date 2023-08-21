# Generated by Django 4.2.4 on 2023-08-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("bcuser", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeChoice",
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
                (
                    "time",
                    models.CharField(
                        choices=[
                            ("평일오전", "평일오전"),
                            ("평일오후", "평일오후"),
                            ("평일저녁", "평일저녁"),
                            ("주말오전", "주말오전"),
                            ("주말오후", "주말오후"),
                            ("주말저녁", "주말저녁"),
                        ],
                        max_length=20,
                        verbose_name="시간 선택",
                    ),
                ),
            ],
            options={
                "verbose_name": "시간 선택",
                "verbose_name_plural": "시간 선택",
                "db_table": "time_choice",
            },
        ),
        migrations.CreateModel(
            name="Mypage",
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
                (
                    "age",
                    models.CharField(
                        choices=[
                            ("10대", "10대"),
                            ("20대", "20대"),
                            ("30대", "30대"),
                            ("40대", "40대"),
                            ("50대 이상", "50대 이상"),
                        ],
                        default="20대",
                        max_length=10,
                        verbose_name="연령대",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("남자", "남자"), ("여자", "여자")],
                        default="남자",
                        max_length=10,
                        verbose_name="성별",
                    ),
                ),
                ("tags", models.ManyToManyField(to="p_tag.tag", verbose_name="태그")),
                (
                    "time",
                    models.ManyToManyField(to="o_mypage.timechoice", verbose_name="시간"),
                ),
            ],
            options={
                "verbose_name": "나의 프로필",
                "verbose_name_plural": "나의 프로필",
                "db_table": "mypage",
            },
        ),
    ]