from __future__ import unicode_literals

from django.db import models
from django.db.models import Model


class Votos(Model):
    cantidad = models.IntegerField(null=False, blank=False)
