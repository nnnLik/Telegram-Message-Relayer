# Generated by Django 4.2.4 on 2023-08-16 21:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_remove_telegramtoken_telegram_username_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="messagehistory",
            old_name="message",
            new_name="content",
        ),
        migrations.AddField(
            model_name="messagehistory",
            name="chat_id",
            field=models.PositiveIntegerField(),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="telegramtoken",
            name="chat_id",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
