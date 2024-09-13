from rest_framework import serializers
from .models import Magazin, Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"


class MagazinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazin
        fields = "__all__"
