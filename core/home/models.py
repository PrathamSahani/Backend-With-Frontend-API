# logs/models.py

from django.db import models

class Log(models.Model):
    LEVEL_CHOICES = [
        ('info', 'Info'),
        ('error', 'Error'),
        ('success', 'Success'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    log_string = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    source = models.CharField(max_length=50)
    metadata = models.JSONField()
