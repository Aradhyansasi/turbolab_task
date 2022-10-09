from django.shortcuts import render
from generate_file.task import generate_csv
import csv

from generate_file.forms import CSVForm
from django.template import RequestContext
from .models import Datas
def create_view(request):
    context ={}

    # add the dictionary during initialization
    form = CSVForm(request.POST or None)
    if form.is_valid():
        file_name = (form.data.get('file_name'))
        count=(form.data.get('count'))      
        celery = generate_csv.delay(file_name, count)
        print(celery,'celery id')
        form.save()
            
    context['form']= form
    return render(request, "csv_form.html", context)
