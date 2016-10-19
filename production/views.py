from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.conf import settings
from django import http
from django.views import generic

from .models import Production

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'all_current_productions'
    def get_queryset(self):
        return Production.objects.order_by('id')
    def verify_part_bom(self):
	#juntar com script que já está pronto. 
	#verificar lista na planilha, comparar com os componentes em digstock
	#listar os que tem e os que não tem 
	#gerar lista de compras
        bom = Production.objects.get(pk=pk).bom_file
        return bom    

def index(request):
    return render(request, 'index.html')

def upload(request):
    template = 'upload.html'
    form = UploadProductionForm()
    return render(request, 'upload.html',{'form':form})

