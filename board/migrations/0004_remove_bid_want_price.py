# Generated by Django 4.1.3 on 2022-11-06 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0003_remove_bid_flag"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bid",
            name="want_price",
        ),
    ]
