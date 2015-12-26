from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Data(models.Model):
    quote_text = models.CharField(max_length=1000)
    def __str__(self):
        return self.quote_text
