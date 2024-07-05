# stickynotes/urls.py
from django.urls import path
from .views import get, get_all, create, update, delete

urlpatterns = [
    # URL pattern for displaying a list of all stickynotes.
    path('', get_all, name='stickynotes'),
    # URL pattern for displaying details of a specific stickynote.
    path('<int:pk>', get, name='stickynote'),
    # URL pattern for creating a new stickynote.
    path('new/', create, name='create_stickynote'),
    # URL pattern for upldating an existing stickynote.
    path('stickynotes/<int:pk>/edit/', update, name='update_stickynote'),
    # URL pattern for deleting an existing stickynote.
    path('<int:pk>/delete/', delete, name='delete_stickynote'),
]
