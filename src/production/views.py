from django import http
from django.shortcuts import render, render_to_response, HttpResponseRedirect, redirect
from django.conf import settings
from django.views import generic
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import Production
from .forms import UploadFileForm
from .functions import handle_uploaded_file


class IndexView(generic.ListView):
    template_name = 'production.html'
    context_object_name = 'all_current_productions'
    def get_queryset(self):
        return Production.objects.order_by('id') 


class DetailView(generic.DetailView):
    model = Production
    template_name = 'detail.html'


def simple_upload(request):
    if request.method == 'POST' and request.FILES['bom_file']:
        myfile = request.FILES['bom_file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'simple_upload.html', {
            'uploaded_file_url': "New production add!"
        })
    else:
        form = UploadFileForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })
