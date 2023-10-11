import django_tables2 as tables
from .models import contracts
from django_filters import FilterSet, filters
from django_tables2.utils import A
from django.forms.widgets import TextInput
class ContractsTable(tables.Table):
    reference_number = tables.LinkColumn('activity_detail', args=[A('reference_number')])
    class Meta:
        model = contracts
        template_name = "django_tables2/bootstrap.html"
        fields = ("reference_number","WPL_reference","trust","WPL_category_area","sub_category","project_title","description","division","route_to_market","department","agreement_type","personal_info","contract_value","contract_term","supplier","contract_start","extension","extension_months","notice","notice_days","contract_available","indexation_clause","WPL_lead")
        attrs = {"class": "table-hover table-bordered table-condensed"}

class ContractFilter(FilterSet):
    class Meta:
        model = contracts

        fields = {"trust": ["exact"],"reference_number": ["exact"],"WPL_category_area" : ["exact"],"sub_category" : ["exact"],"project_title" : ["contains"],"description" : ["contains"],"division" : ["exact"],"route_to_market" : ["exact"],"department" : ["exact"],"agreement_type" : ["exact"],"supplier" : ["contains"],"WPL_lead" : ["exact"]}