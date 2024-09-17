from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_home, name = 'notes_home'),
    path('create', views.create, name='create_note'),
    path('<int:pk>', views.NoteDetailView.as_view(), name='notes-detail'),
]