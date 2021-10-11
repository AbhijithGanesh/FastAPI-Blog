from django.db import models
from django.contrib.auth.models import User
import uuid


class BlogTable(models.Model):
    Title = models.CharField(
        max_length=255, default="No Title", null=False, blank=False
    )
    Identifier = models.CharField(
        max_length=140, default="No SEO Optimized tag", blank=False, null=False
    )
    UUID = models.UUIDField(default=uuid.uuid4, editable=False)
    SubTitle = models.CharField(
        max_length=255, default="No SubTitle", null=False, blank=False
    )
    Date_of_creation = models.DateTimeField(auto_now_add=True)
    Content = models.TextField()
    URL = models.URLField()


class AbstractUser(models.Model):
    reference = models.ForeignKey(User, on_delete=models.CASCADE)


class Socials(AbstractUser):
    GitHub = models.CharField(
        max_length=100, blank=True, null=True, default="No GitHub UserName specifiied"
    )
    Instagram = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="No Instagram UserName specifiied",
    )
    Twitter = models.CharField(
        max_length=100, blank=True, null=True, default="No Twitter UserName specifiied"
    )
    LinkedIn = models.CharField(
        max_length=100, blank=True, null=True, default="No LinkedIn UserName specifiied"
    )
    YouTube = models.CharField(
        max_length=100, blank=True, null=True, default="No YouTube UserName specifiied"
    )
    Website = models.URLField()
