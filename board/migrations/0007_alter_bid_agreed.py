# Generated by Django 4.1.3 on 2022-11-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0006_bid_modify_date_sale_modify_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="agreed",
            field=models.IntegerField(default=0),
        ),
    ]