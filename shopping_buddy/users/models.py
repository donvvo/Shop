# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db import models
# from django.utils.translation import ugettext_lazy as _
from wishlist.models import WishList


class User(AbstractUser):
    friends = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def get_friends_wishlist(self):
        wishlists = WishList.objects.filter(user__in=self.friends)
        wishlist_combined = ""
        for wishlist in wishlists:
            wishlist_combined += wishlist.items
        return wishlist_combined
