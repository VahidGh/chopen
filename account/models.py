from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='account/user/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username
