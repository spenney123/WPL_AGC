from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import contracts
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView
from .tables import ContractsTable, ContractFilter
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin

class ContractDetailView(DetailView):
    model = contracts
    template_name = 'contract_detail.html'

class ContractCreateView(CreateView):
    model = contracts
    template_name = 'contract_create.html'
    fields = ['reference_number','WPL_reference','trust','WPL_category_area','sub_category','project_title','description','division','route_to_market','department','agreement_type','personal_info','contract_value','contract_term','supplier','contract_start','extension','extension_months','notice','notice_days','contract_available','indexation_clause','contract_available']
    success_url = reverse_lazy('contracts_list')

class ContractListView(ExportMixin,SingleTableMixin,FilterView):
    model = contracts
    table_class = ContractsTable
    template_name = 'contracts_list.html'

    filterset_class = ContractFilter


class ContractUpdateView(UpdateView, LoginRequiredMixin):
    model = contracts
    template_name = 'contract_update.html'
    success_url = reverse_lazy('contracts_list')
    login_url = 'login'
    fields = ['reference_number','WPL_reference','trust','WPL_category_area','sub_category','project_title','description','division','route_to_market','department','agreement_type','personal_info','contract_value','contract_term','supplier','contract_start','extension','extension_months','notice','notice_days','contract_available','indexation_clause','WPL_lead']

