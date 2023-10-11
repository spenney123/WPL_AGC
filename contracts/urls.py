from django.urls import path
from .views import ContractListView, ContractDetailView, ContractCreateView, ContractUpdateView

#### change pk part to WPL reference! ###
urlpatterns = [
  path('<int:pk>/contract/',ContractDetailView.as_view(),name='contract_detail'),
  path('contract/',ContractListView.as_view(),name='contracts_list'),
  path('new/', ContractCreateView.as_view(), name='contract_create'),
  path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_update'),
]
