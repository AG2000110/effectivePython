from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import RedirectView

from .views import NoteCreateView, NoteUpdateView, NoteDeleteView, NoteListView, login_view

urlpatterns = [
    path('', RedirectView.as_view(url='/notes/', permanent=True)),
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='note-list'), name='logout'),
    path('note/new/', NoteCreateView.as_view(), name='note-new'),
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name='note-edit'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
