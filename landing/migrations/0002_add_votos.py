# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 22:16
from __future__ import unicode_literals

from django.db import migrations, models


def add_votos(apps, schema_editor):
    Votos = apps.get_model("landing", "Votos")
    voto = Votos.objects.create(cantidad=958)
    voto.save()


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_votos)
    ]