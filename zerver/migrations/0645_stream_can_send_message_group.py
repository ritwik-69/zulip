# Generated by Django 5.0.9 on 2024-12-09 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0644_check_update_all_channels_active_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="stream",
            name="can_send_message_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
    ]
