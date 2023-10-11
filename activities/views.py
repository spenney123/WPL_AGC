from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import activity
from .tables import ActivityTable, ActivityFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2.export.views import ExportMixin
import django_tables2 as tables
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from CPW.models import CPW
from contracts.models import contracts
from pipeline.models import pipeline




class ActivityDetailView(DetailView,LoginRequiredMixin):
    model = activity
    template_name = 'activity_detail.html'
    login_url = 'login'

    def get_context_data(self,**kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['CPWs'] = CPW.objects.filter(reference_number=pk)
        context['contracts'] = contracts.objects.filter(reference_number=pk)
        context['pipeline'] = pipeline.objects.filter(reference_number=pk)
        return context



class ActivityCreateView(CreateView,LoginRequiredMixin):
    model = activity
    template_name = 'activity_create.html'
    fields = ['WPL_lead','trust','project_title','project_type','supplier']
    success_url = reverse_lazy('activity_list')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)



class ActivityListView(ExportMixin,SingleTableMixin,FilterView,LoginRequiredMixin):
    table_class = ActivityTable
    model = activity
    template_name = 'activity_list.html'
    login_url = 'login'


    filterset_class = ActivityFilter


class ActivityExportView(ExportMixin,tables.SingleTableView,LoginRequiredMixin):
    table_class = ActivityTable
    model = activity
    template_name = "django_tables2/bootstrap.html"
    login_url = 'login'

class ActivityUpdateView(UpdateView, LoginRequiredMixin):
    model = activity
    template_name = 'activity_update.html'
    success_url = reverse_lazy('activity_list')
    login_url = 'login'
    fields = ['WPL_lead','trust','project_title','project_type','supplier']

