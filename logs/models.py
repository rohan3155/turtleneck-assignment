from django.db import models

# Create your models here.
class Log(models.Model):
    timestamp = models.DateTimeField()
    source_ip = models.GenericIPAddressField()
    event_type = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.timestamp} | {self.source_ip} | {self.event_type}"