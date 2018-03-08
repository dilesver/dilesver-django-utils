from django.db import models


class Destination(models.Model):
    DESTINATION_TYPES = (
        ('IN', 'INCOMING'.capitalize()),
        ('OUT', 'OUTGOING'.capitalize)
    )
    
    type = models.CharField(max_length=6, choices=DESTINATION_TYPES, default='OUT')
    name = models.CharField(max_length=128)


class Messages(models.Model):
    destination = models.ForeignKey(Destination, null=False, blank=False)
    create_time = models.DateField()
