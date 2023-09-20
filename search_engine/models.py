from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Organisation(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    founders = models.JSONField(
        ArrayField(models.CharField(max_length=128)), null=True
    )
    board_members = models.JSONField(
        ArrayField(models.CharField(max_length=128)), null=True
    )
    street_address = models.CharField(max_length=128, null=True)
    headquarters = models.CharField(max_length=128, null=True)
    employee_count = models.PositiveIntegerField(default=0)
    is_parent_org = models.BooleanField(default=False)
