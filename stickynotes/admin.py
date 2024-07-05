# stickynotes/admin.py

from django.contrib import admin
from .models import StickyNote

# Register your models here.

# StickyNote model
admin.site.register(StickyNote)
