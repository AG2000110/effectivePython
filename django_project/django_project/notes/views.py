# plik: notes/views.py
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from notes.models import Note


class NoteListView(ListView):
    model = Note
    fields = ['notes']


@method_decorator(login_required, name='dispatch')
class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'body']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'body']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')
