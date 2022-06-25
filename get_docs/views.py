from get_docs.models import Text
from get_docs.serializers import TextSerializer
from rest_framework import generics


class TextList(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer