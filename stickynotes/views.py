# stickynotes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm


def get_all(request):
    """
    View to display a list of all stickynotes.

    :parameter request: HTTP request object.
    :return: Rendered template with a list of stickynotes.
    """
    stickynotes = StickyNote.objects.all()

    # Creating a context dictionary to pass data.
    context = {
        'stickynotes': stickynotes,
        'page_title': '''Sorcha's StickyNote App'''
    }

    return render(request, 'stickynotes/index.html', context=context)


def get(request, pk):
    """
    View to display details of a specific stickynote.
    
    :parameter request: HTTP request object.
    :parameter pk: Primary key of the stickynote.
    :return: Rendered template with details of the specified stickynote.
    """
    stickynote = get_object_or_404(StickyNote, pk=pk)
    return render(request, 'stickynotes/stickynote.html',
                   {'stickynote': stickynote}
    )


def create(request):
    """
    View to create a new stickynote.

    :parameter request: HTTP request object.
    :return: Rendered template for creating a new stickynote.
    """
    if request.method == 'POST':
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            stickynote = form.save(commit=False)
            stickynote.save()
            return redirect('stickynotes')
    else:
        form = StickyNoteForm()
    return render(request, 'stickynotes/stickynote_form.html',
                   {'form': form}
    )


def update(request, pk):
    """
    View to update an existing stickynote.

    :parameter request: HTTP request object.
    :parameter pk: Primary key of the stickynote to be updated.
    :return: Rendered template for updating the specified stickynote.
    """
    stickynote = get_object_or_404(StickyNote, pk=pk)

    if request.method == 'POST':
        form = StickyNoteForm(request.POST, instance=stickynote)

        if form.is_valid():
            stickynote = form.save(commit=False)
            stickynote.save()
            return redirect('stickynotes')
    else:
        form = StickyNoteForm(instance=stickynote)

    return render(request, 'stickynotes/stickynote_form.html', {'form': form})


def delete(request, pk):
    """
    View to delete an existing stickynote.
    
    :parameter request: HTTP request object.
    :parameter pk: Primary key of the post to be deleted.
    :return: Redirect to the stickynote list after deletion.
    """
    stickynote = get_object_or_404(StickyNote, pk=pk)
    stickynote.delete()
    return redirect('stickynotes')
