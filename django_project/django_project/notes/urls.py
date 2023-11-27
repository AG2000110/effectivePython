from django.urls import path

from notes.views import NoteListView, NoteCreateView, NoteDeleteView, NoteUpdateView

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/add/', NoteCreateView.as_view(), name='note-add'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note-edit'),

]
