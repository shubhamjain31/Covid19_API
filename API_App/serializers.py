from rest_framework import serializers

class Covid19Serializer(serializers.Serializer):
    country = serializers.CharField(max_length=256)
    totalCases = serializers.CharField(max_length=256)
    newCases = serializers.CharField(max_length=256)
    deaths = serializers.CharField(max_length=256)
    newDeaths = serializers.CharField(max_length=256)
    recovered = serializers.CharField(max_length=256)
    activeCases = serializers.CharField(max_length=256)
    seriousCritical = serializers.CharField(max_length=256)
    totalTests = serializers.CharField(max_length=256)
