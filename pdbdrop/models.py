from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_comma_separated_integer_list


class Upload(models.Model):
    file_path = models.CharField(max_length=255)
    user_email = models.EmailField()

    # here goes the options
    keep_list = models.CharField(max_length=255, null=True, blank=True)
    waters = models.BooleanField(default=False)
    three_d = models.BooleanField(default=False, verbose_name='3D')
    combi = models.BooleanField(default=False)
    multiple = models.BooleanField(default=False)
    confs = models.IntegerField(null=True, blank=True)
    freq = models.IntegerField(null=True, blank=True)
    step = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    dstep = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    res = models.CharField(max_length=15, validators=[validate_comma_separated_integer_list], null=True, blank=True)
    modes = models.CharField(max_length=50, validators=[validate_comma_separated_integer_list], null=True, blank=True)
    ecuts = models.CharField(max_length=50, null=True, blank=True)
    video_path = models.CharField(max_length=255, null=True, blank=True)
