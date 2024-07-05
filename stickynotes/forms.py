# stickynote.forms.py
from django import forms
from .models import StickyNote

class StickyNoteForm(forms.ModelForm):
    """
    Form for creating and updating StickyNote objects.

    Fields:
    - title: CharField for the stickynote title.
    - description: TextField for the stickynote description.

    Meta class: 
    - Defines the model to use (StickyNote) and the fields to include
    in the form.

    :parameter forms.ModelForm: Django's ModelForm class.
    """
    class Meta:
        model = StickyNote
        fields = ['title', 'description', 'mark_as_complete', 'created_by']
