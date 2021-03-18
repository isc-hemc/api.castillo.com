# Generated by Django 3.1.7 on 2021-03-17 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0007_auto_20210317_1323"),
        ("address", "0004_auto_20210317_1323"),
        ("house", "0003_auto_20210317_1323"),
    ]

    operations = [
        migrations.AlterField(
            model_name="housemodel",
            name="address",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="address",
                to="address.addressmodel",
            ),
        ),
        migrations.AlterField(
            model_name="housemodel",
            name="services",
            field=models.ManyToManyField(
                related_name="services", to="service.ServiceModel"
            ),
        ),
    ]