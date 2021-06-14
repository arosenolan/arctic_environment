from django.db import models

from django.db import models


class ReleaseInfo(models.Model):
    release_version = models.CharField(max_length=20)  # Example: 1.12.34
    release_date = models.DateTimeField('date published')


