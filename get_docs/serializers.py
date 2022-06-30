from rest_framework import serializers
from get_docs.models import Text


class TextSerializer(serializers.ModelSerializer):
    cpfs_found = serializers.CharField(read_only=True)
    cnpjs_found = serializers.CharField(read_only=True)
    ceps_found = serializers.CharField(read_only=True)
    class Meta:
        model = Text
        fields = ['id', 'text', 'cpfs_found', 'cnpjs_found', 'ceps_found']
