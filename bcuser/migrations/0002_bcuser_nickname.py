# Generated by Django 4.2.4 on 2023-08-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bcuser", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bcuser",
            name="nickname",
            field=models.CharField(max_length=64, verbose_name="닉네임"),
            
        ),
    ]
