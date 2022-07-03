from django.db import models


class ExcelFile(models.Model):
    file = models.FileField(blank=True)
    file_path = models.FilePathField(blank=True)
    url = models.URLField(blank=True)