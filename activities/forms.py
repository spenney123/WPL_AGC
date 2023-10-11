from django.forms import ModelForm
from django.forms import modelformset_factory, BaseFormSet, TextInput, formset_factory
from django.shortcuts import render
from models import activity
import requests
from django import forms
from django.contrib.admin.widgets import AdminSplitDateTime
from django_bootstrap5.widgets import RadioSelectButtonGroup
import requests

class ActivityCreateForm(ModelForm):
    class Meta:
        model = activity
        fields = ['WPL_lead', 'trust', 'project_title', 'project_type','supplier']

