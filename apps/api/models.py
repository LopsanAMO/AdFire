from django.db import models


class Api(models.Model):
    publication_file = models.FileField(upload_to='/files')
