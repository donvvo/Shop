from django.db import models

from shopping_buddy.users.models import User


# Create your models here.
class WishList(models.Model):
    user = models.ForeignKey(User)
    items = models.TextField(blank=True)
