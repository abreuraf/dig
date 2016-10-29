from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.conf import settings
from django.views import generic
from django import http
from .models import Production
from .forms import UploadFileForm
from .functions import handle_uploaded_file
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_current_productions'
    def get_queryset(self):
        return Production.objects.order_by('id') 


class DetailView(generic.DetailView):
    model = Production
    template_name = 'detail.html'


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')
