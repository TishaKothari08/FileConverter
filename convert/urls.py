

from django.urls import path
from . import views

urlpatterns = [
    path('word-to-pdf/', views.word_to_pdf, name='word_to_pdf'),
    path('pdf-to-word/', views.pdf_to_word, name='pdf_to_word'),
]
