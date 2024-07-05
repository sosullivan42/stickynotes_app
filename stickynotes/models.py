# stickynotes/models.py
from django.db import models

"""
Model representing a stickynotes application.

Fields:
 - title: Charfield for the stickynote title with a maximum length of 50
 characters.
 - description: TextField for the stickynote description.
 - mark_as_complete: BooleanFiels set initially to False and True when
 complete.
 - created_by: CharField for the stickynote creator to be named (max
 length 50 characters).
"""
class StickyNote(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    mark_as_complete = models.BooleanField(default=False)
    created_by = models.CharField(max_length=50)
