from django import forms
from .models import StickyNote

class StickyNoteForm(forms.ModelForm): 
    class Meta: 
        model = StickyNote
        fields = ['title', 'description', 'mark_as_complete', 'created_by']
        