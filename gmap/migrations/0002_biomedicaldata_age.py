# Generated by Django 4.2.1 on 2024-04-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gmap", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="biomedicaldata",
            name="age",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
