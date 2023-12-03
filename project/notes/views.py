from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Note
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin



class NoteListView(ListView):
    model = Note
    template_name = 'notes/note_list.html'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')
    login_url = '/login/'
    redirect_field_name = 'next'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class NoteUpdateView(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note-list')

    def test_func(self):
        note = self.get_object()
        return self.request.user == note.created_by


class NoteDeleteView(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    template_name = 'notes/note_confirm_delete.html'

    def test_func(self):
        note = self.get_object()
        return self.request.user == note.created_by or self.request.user.is_superuser


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('note-list')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})