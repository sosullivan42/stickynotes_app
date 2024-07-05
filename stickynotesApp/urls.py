# stickynotesApp/urls.py
from django.contrib import admin
from django.urls import include, path

# Define URL patterns for the entire project.
urlpatterns = [
    # Admin URL pattern, mapping to the Django admin interface
    path('admin/', admin.site.urls),

    # Include URL patterns from the 'stickynotes' app
    # All URLs from 'stickynotes.urls' will be prefixed with stickynotes/'
    path('', include('stickynotes.urls'))
]
