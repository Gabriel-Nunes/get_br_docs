from django.db import models
from get_docs.utils import find_cpf, find_cnpj, find_cep


class Text(models.Model):
    text = models.TextField(blank=True)
    cpfs = models.TextField(blank=True, default='')
    cnpjs = models.TextField(blank=True, default='')
    ceps = models.TextField(blank=True, default='')
    def save(self, *args, **kwargs):
        """"
        Find entities in text.
        """
        self.cpfs = find_cpf(self.text)
        self.cnpjs = find_cnpj(self.text)
        self.ceps = find_cep(self.text)
        super().save(*args, **kwargs)