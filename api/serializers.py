from rest_framework import serializers
from datetime import date
from .models import Language, Media
from rest_framework.permissions import IsAuthenticated


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'