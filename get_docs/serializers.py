from rest_framework import serializers
from get_docs.models import Text


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'text']
