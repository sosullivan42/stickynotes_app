from django.db import models

# Create your models here.
class StickyNote(models.Model): 
    title = models.CharField(max_length=50)
    description = models.TextField()
    mark_as_complete = models.BooleanField(default=False)
    created_by = models.CharField(max_length=50)

