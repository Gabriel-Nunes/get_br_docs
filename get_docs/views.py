from get_docs.models import Text
from get_docs.serializers import TextSerializer
from rest_framework import generics, status
from get_docs.utils import find_cpf, find_cnpj, find_cep
from rest_framework.response import Response


class GetData(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        text = serializer.data.get('text')
        cpfs = find_cpf(text)
        cnpjs = find_cnpj(text)
        ceps = find_cep(text)
        res = {'cpfs_found': cpfs,
                'cnpjs_found': cnpjs,
                'ceps_found': ceps}
        return Response(res, status=status.HTTP_200_OK, headers=headers)
