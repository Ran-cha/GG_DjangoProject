# Generated by Django 4.2.4 on 2023-08-16 11:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("bcuser", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="i_Qna",
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
                    "i_category",
                    models.CharField(
                        choices=[("소식", "소식"), ("친목", "친목"), ("기타", "기타")],
                        default="news",
                        max_length=64,
                        verbose_name="카테고리",
                    ),
                ),
                ("i_title", models.CharField(max_length=128, verbose_name="제목")),
                ("i_contents", models.TextField(verbose_name="내용")),
                (
                    "i_register_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="등록날짜"
                    ),
                ),
                ("i_click", models.PositiveIntegerField(default=0)),
                ("i_votes", models.PositiveIntegerField(default=0)),
                (
                    "i_voters",
                    models.ManyToManyField(
                        blank=True, related_name="upvoted_qnas", to="bcuser.bcuser"
                    ),
                ),
                (
                    "i_writer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bcuser.bcuser",
                        verbose_name="작성자",
                    ),
                ),
            ],
            options={
                "verbose_name": "질문",
                "verbose_name_plural": "질문들",
                "db_table": "i_qna",
            },
        ),
        migrations.CreateModel(
            name="i_Comment",
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
                ("comment", models.CharField(max_length=256, verbose_name="댓글 내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bcuser.bcuser",
                        verbose_name="작성자",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="i_qna.i_qna",
                        verbose_name="게시글",
                    ),
                ),
            ],
            options={
                "verbose_name": "댓글",
                "verbose_name_plural": "댓글들",
            },
        ),
    ]
