from django.db import models

from newspapers.models import Newspaper

class Ad(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    newspaper = models.ManyToManyField(Newspaper)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    client_company = models.CharField(max_length=128, blank=True, null=True)
    client_contact = models.CharField(max_length=128, blank=True, null=True)
    client_phone = models.CharField(max_length=15, blank=True, null=True)
    client_email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)