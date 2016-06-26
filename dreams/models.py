from __future__ import unicode_literals

from django.db import models


class Dreams(models.Model):
    counter = models.IntegerField()
