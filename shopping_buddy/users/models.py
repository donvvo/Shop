# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db import models
# from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    friends = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

