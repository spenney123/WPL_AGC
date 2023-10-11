from django.urls import path
from django.contrib import admin
from .views import ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, DetailView


urlpatterns = [
  path('<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),
  path('', ActivityListView.as_view(), name='activity_list'),
  path('new/', ActivityCreateView.as_view(), name='activity_create'),
  path('<int:pk>/edit/', ActivityUpdateView.as_view(), name='activity_update'),
  path('detail/<int:pk>/', DetailView, name="detail_list"),
]


