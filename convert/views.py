
from django.shortcuts import render
from django.http import HttpResponse
from .utils import convert_word_to_pdf, convert_pdf_to_word

def home(request):
    return render(request, 'convert/home.html')

def word_to_pdf(request):
    if request.method == 'POST' and request.FILES['word_file']:
        word_file = request.FILES['word_file']
        pdf_buffer = convert_word_to_pdf(word_file)
        
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="converted.pdf"'
        return response
    return render(request, 'convert/upload_word.html')

def pdf_to_word(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        word_buffer = convert_pdf_to_word(pdf_file)
        
        response = HttpResponse(word_buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename="converted.docx"'
        return response
    return render(request, 'convert/upload_pdf.html')
