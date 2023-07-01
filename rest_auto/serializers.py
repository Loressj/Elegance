from rest_framework import serializers
from core.models import Auto

class AutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = auto
        field = ['idAuto','precio','marca','modelo']