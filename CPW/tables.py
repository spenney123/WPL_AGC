import django_tables2 as tables
from .models import CPW
from django_filters import FilterSet
from django_tables2.utils import A
from django import forms
from django.db import models
import django_filters

class CPWTable(tables.Table):
    reference_number = tables.LinkColumn('activity_detail', args=[A('reference_number')])
    class Meta:
        model = CPW
        template_name = "django_tables2/bootstrap.html"
        fields = ("reference_number","WPL_reference","trust","date_added_to_cpw","project_title","cpw_rationale","supplier","total_cpw_value","division","department","most_senior_approval_received_by","date_final_approval_received","one_off_purchase","contract_term")
        attrs = {"class": "table-hover table-bordered table-condensed"}

class CPWFilter(FilterSet):

      class Meta:
        model = CPW
        fields = {"reference_number": ["exact"], "trust": ["exact"],"date_added_to_cpw": ['date__gte','date__lte'], "project_title": ["contains"], "supplier": ["contains"], "division": ["exact"], "department": ["contains"], "most_senior_approval_received_by": ["contains"], "one_off_purchase": ["exact"],"date_final_approval_received":['gte','lte']}
