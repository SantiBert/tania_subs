import uuid

from django.db import models
from django.utils import timezone


class Suscribes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre", max_length=150, unique=True)
    email = models.EmailField("E-mail", max_length=254, unique=True)
    acept = models.BooleanField("Aceptar", default=False)
    created_date = models.DateTimeField(
        "Fecha de cración", default=timezone.now)

    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"
        ordering = ['-created_date']

    def __str__(self):
        return self.name
