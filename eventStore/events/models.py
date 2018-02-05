# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Deploys(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    sha = models.CharField(max_length=40, blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=8, blank=True, null=True)
    engineer = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.engineer

    class Meta:
        managed = False
        db_table = 'deploys'


