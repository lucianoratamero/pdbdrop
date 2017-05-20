from __future__ import unicode_literals

import re

from django.db import models
from django.core.validators import RegexValidator


comma_separated_float_list_re = re.compile('^([-+]?\d*\.?\d+[,\s]*)+$')
validate_comma_separated_float_list = RegexValidator(
              comma_separated_float_list_re,
              'Enter only floats separated by commas.', 'invalid')


class CommaSeparatedFloatField(models.CharField):
    default_validators = [validate_comma_separated_float_list]
    description = "Comma-separated floats"

    def formfield(self, **kwargs):
        defaults = {
            'error_messages': {
                'invalid': 'Enter only floats separated by commas.',
            }
        }
        defaults.update(kwargs)
        return super(CommaSeparatedFloatField, self).formfield(**defaults)


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
    ecuts = CommaSeparatedFloatField(max_length=50, null=True, blank=True)
    video_text = models.TextField(null=True, blank=True)
