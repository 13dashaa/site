from django.shortcuts import render, redirect
from .models import Note
from .forms import NotesForm
from django.views.generic import DetailView #UpdateView, DeleteView
def notes_home(request):
    notes = Note.objects.order_by('-date')
    return render(request, 'notes/index_notes.html', {'notes' : notes})

class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/notes_view.html'
    context_object_name = 'note'

def create(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_home')
        else:
            error = 'Форма заполнена неверно'

    form = NotesForm()
    data = {'form': form, 'error': error}

    return render(request, 'notes/create_note.html', data)