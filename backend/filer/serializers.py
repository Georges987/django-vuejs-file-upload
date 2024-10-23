from rest_framework import serializers
from .models import Filer

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filer
        fields = '__all__'