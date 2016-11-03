from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, default=User.objects.get(username="taufiq"))
    #user = models.ForeignKey('auth.User')
    status = models.TextField()
    published_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.status[:10]



