from datetime import datetime

from django.contrib.auth.models import User
from django.db import models



class Appointment(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=200
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'


class Appoint(models.Model):
    idpk = models.IntegerField()

    idpkid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.idpk}'
