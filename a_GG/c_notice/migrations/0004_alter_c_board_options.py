# Generated by Django 4.2.4 on 2023-08-08 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "c_notice",
            "0003_alter_c_board_options_remove_c_board_register_dttm_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="c_board",
            options={"verbose_name": "공지", "verbose_name_plural": "공지들"},
        ),
    ]
