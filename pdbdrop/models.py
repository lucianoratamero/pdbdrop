from __future__ import unicode_literals

from django.db import models


class Upload(models.Model):
    file_path = models.CharField(max_length=255)
    user_email = models.EmailField()

    # here goes the options
    keep_list = models.CharField(max_length=255, null=True, blank=True)
    waters = models.BooleanField(default=False)
    three_d = models.BooleanField(default=False)
    combi = models.BooleanField(default=False)
    multiple = models.BooleanField(default=False)
    confs = models.IntegerField(null=True, blank=True)
    freq = models.IntegerField(null=True, blank=True)
    step = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    dstep = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    res = models.CommaSeparatedIntegerField(max_length=15, null=True, blank=True)
    modes = models.CommaSeparatedIntegerField(max_length=50, null=True, blank=True)
    ecuts = models.CharField(max_length=50, null=True, blank=True)
    video_path = models.CharField(max_length=255, null=True, blank=True)
