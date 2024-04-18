from rest_framework import serializers
from .models import Users, BioMedicalData, GyroscopeData, GPSData


class BioMedicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioMedicalData
        fields = ["age", "pulse", "timestamps"]


class GPSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSData
        fields = ["latitude", "longitude", "timestamps"]


class UserSerializer(serializers.ModelSerializer):
    biomedical_data = BioMedicalDataSerializer(many=True, read_only=True)
    gps_data = GPSDataSerializer(many=True, read_only=True)

    class Meta:
        model = Users
        fields = [
            "username",
            "email",
            "password",
            "created_at",
            "updated_at",
            "biomedical_data",
            "gps_data",
        ]
