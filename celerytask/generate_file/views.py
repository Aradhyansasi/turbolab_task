from django.shortcuts import render

from generate_file.forms import CSVForm
from django.template import RequestContext
from .models import Datas
# Create your views here.
# def home(request):
#     context = {}
#     from = C
    # return render(request, 'csv_form.html' )
    # form = CSVForm(request.POST)
    # # validate your form
    # if form.is_valid():
    #     print(**form.cleaned_data)
    #    #Ticket.objects.create(**form.cleaned_data)
    #    # return success url
    # else:
    #    context = {'form': form}
    #    render(request, 'csv_form.html', context)
def create_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # add the dictionary during initialization
    form = CSVForm(request.POST or None)
    if form.is_valid():
        file_name = (form.data.get('file_name'))
        count=(form.data.get('count'))
        print(file_name , count)
        form.save()
            
    context['form']= form
    return render(request, "csv_form.html", context)
