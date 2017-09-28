# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class ObItem(models.Model):
    is_discard = models.NullBooleanField()
    credit_account_no = models.CharField(max_length=1000, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    # create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    item_code = models.CharField(unique=True, max_length=60)
    item_description_english = models.TextField()
    write_date = models.DateTimeField(blank=True, null=True)
    vat_code = models.CharField(max_length=1000, blank=True, null=True)
    vat_percent = models.FloatField(blank=True, null=True)
    # write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    item_description = models.TextField()

    class Meta:
        managed = True
        db_table = 'ob_item'

    def __str__(self):
        return self.item_description_english