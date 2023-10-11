import django_tables2 as tables
from .models import activity
from django_filters import FilterSet
from django_tables2.utils import A
import django_filters

class ActivityTable(tables.Table):
    reference_number = tables.LinkColumn('activity_detail', args=[A('pk')])
    class Meta:
        ### Add Mixin to the overall class to add columns ###
        model = activity
        fields = ("reference_number","WPL_lead","date_logged","trust","project_type","project_title","supplier")
        attrs = {"class": "table-hover table-bordered table-condensed"}
        export_formats = ['csv', 'xls']


class ActivityFilter(FilterSet):

       class Meta:
        model = activity
        fields = {"reference_number": ["exact"],"date_logged":['date__gte','date__lte'], "trust": ["exact"], "project_type": ["exact"], "project_title": ["contains"], "supplier": ["contains"]}

