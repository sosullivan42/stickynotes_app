from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm

# Create your views here.

def get_all(request): 
    stickynotes = StickyNote.objects.all()

    context = {
        'stickynotes': stickynotes,
        'page_title': '''Sorcha's StickyNote App'''
    }

    return render(request, 'stickynotes/index.html', context=context)


def get(request, pk): 
    stickynote = get_object_or_404(StickyNote, pk=pk)
    return render(request, 'stickynotes/stickynote.html', {'stickynote': stickynote})


def create(request): 
    if request.method == 'POST': 
        form = StickyNoteForm(request.POST)
        if form.is_valid(): 
            stickynote = form.save(commit=False)
            stickynote.save()
            return redirect('stickynotes') 
    else: 
        form = StickyNoteForm()
    return render(request, 'stickynotes/stickynote_form.html', {'form': form})

def update(request, pk): 
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
    stickynote = get_object_or_404(StickyNote, pk=pk)
    stickynote.delete()
    return redirect('stickynotes')


    


