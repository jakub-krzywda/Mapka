# Generated by Django 4.2.1 on 2024-04-09 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                ("userid", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="GyroscopeData",
            fields=[
                ("dataid", models.AutoField(primary_key=True, serialize=False)),
                ("x", models.JSONField()),
                ("y", models.JSONField()),
                ("z", models.JSONField()),
                ("timestamps", models.JSONField()),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="gmap.users"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GPSData",
            fields=[
                ("dataid", models.AutoField(primary_key=True, serialize=False)),
                ("latitude", models.JSONField()),
                ("longitude", models.JSONField()),
                ("timestamps", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="gmap.users"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BioMedicalData",
            fields=[
                ("dataid", models.AutoField(primary_key=True, serialize=False)),
                ("pulse", models.JSONField()),
                ("respiration", models.JSONField()),
                ("temperature", models.JSONField()),
                ("timestamps", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="gmap.users"
                    ),
                ),
            ],
        ),
    ]