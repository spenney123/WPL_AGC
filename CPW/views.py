from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CPW
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView
from .models import CPW
from .tables import CPWTable, CPWFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class Meta:
   model = CPW
   fields = ['date_final_approval_received']
   widgets = {'date_final_approval_received': DateInput(),}


class CPWDetailView(DetailView):
    model = CPW
    template_name = 'cpw_detail.html'

class CPWCreateView(CreateView):
    model = CPW
    template_name = 'cpw_create.html'
    fields = ['reference_number','WPL_reference','trust','project_title','cpw_rationale','supplier','total_cpw_value','division','department','most_senior_approval_received_by','date_final_approval_received','one_off_purchase','contract_term']
    success_url = reverse_lazy('cpw_list')

class CPWListView(ExportMixin,SingleTableMixin,FilterView):
    model = CPW
    table_class = CPWTable
    template_name = 'cpw_list.html'


    filterset_class = CPWFilter

class CPWUpdateView(UpdateView, LoginRequiredMixin):
    model = CPW
    template_name = 'cpw_update.html'
    success_url = reverse_lazy('cpw_list')
    login_url = 'login'
    fields = ['reference_number','WPL_reference','trust','project_title','cpw_rationale','supplier','total_cpw_value','division','department','most_senior_approval_received_by','date_final_approval_received','one_off_purchase','contract_term']


