from rest_framework import serializers
from get_docs.models import Text


class TextSerializer(serializers.ModelSerializer):
    cpfs = serializers.CharField(read_only=True)
    cnpjs = serializers.CharField(read_only=True)
    ceps = serializers.CharField(read_only=True)
    class Meta:
        model = Text
        fields = ['text', 'cpfs', 'cnpjs', 'ceps']
