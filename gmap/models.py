from django.db import models


# Create your models here.
class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BioMedicalData(models.Model):
    dataid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    age = models.IntegerField
    pulse = models.JSONField()
    respiration = models.JSONField()
    temperature = models.JSONField()
    timestamps = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


class GyroscopeData(models.Model):
    dataid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    x = models.JSONField()
    y = models.JSONField()
    z = models.JSONField()
    timestamps = models.JSONField()


class GPSData(models.Model):
    dataid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    latitude = models.JSONField()
    longitude = models.JSONField()
    timestamps = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

