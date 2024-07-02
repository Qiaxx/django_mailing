# Generated by Django 5.0.6 on 2024-07-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [("block_user", "Can blocking users")],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="is_blocked",
            field=models.BooleanField(default=False),
        ),
    ]
