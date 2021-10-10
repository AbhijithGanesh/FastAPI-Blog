from django.db import models
import uuid

class BlogTable(models.Model):
    Title = models.CharField(max_length = 255, default = "No Title", null = False, blank = False )
    Identifier = models.CharField(max_length = 140, default = "No SEO Optimized tag", blank = False, null = False)
    UUID = models.UUIDField(default=uuid.uuid4, editable=False)
    SubTitle = models.CharField(max_length = 255, default = "No SubTitle", null = False, blank = False )
    Date_of_creation = models.DateTimeField(auto_created=True)
    Content = models.TextField()
    URL = models.URLField()
