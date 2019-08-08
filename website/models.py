
from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    color = models.CharField(max_length=7)
    longitude = models.DecimalField (max_digits=18, decimal_places=16, null=True, blank=True)
    latitude = models.DecimalField (max_digits=18, decimal_places=16, null=True, blank=True)

class AbstractArticle(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(default=datetime.date.today())
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['-date']
        abstract = True


class Article(AbstractArticle):
    pass


class FlashInfo(AbstractArticle):
    pass

