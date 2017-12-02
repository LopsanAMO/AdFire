from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    phone = models.CharField(max_length=13)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Api(models.Model):
    name = models.CharField(max_length=40)
    publication_file = models.FileField(upload_to='files')
    date = models.DateTimeField()
    final_date = models.DateTimeField()
    ad_type = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)
