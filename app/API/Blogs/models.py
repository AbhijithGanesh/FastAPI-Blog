from django.db import models

class BlogTable(models.Model):
    Title = models.CharField(max_length = 255, default = "No Title", null = False, blank = False )
    SubTitle = models.CharField(max_length = 255, default = "No SubTitle", null = False, blank = False )
    Date_of_creation = models.DateTimeField(auto_created=True)
    Content = models.TextField()
    URL = models.URLField()
