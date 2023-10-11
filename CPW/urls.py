from django.urls import path
from .views import CPWListView, CPWDetailView, CPWCreateView, CPWUpdateView

#### change pk part to WPL reference! ###
urlpatterns = [
  path('cpw/',CPWListView.as_view(),name='cpw_list'),
  path('new/', CPWCreateView.as_view(), name='cpw_create'),
  path('<int:pk>/edit/', CPWUpdateView.as_view(), name='cpw_update'),

]
