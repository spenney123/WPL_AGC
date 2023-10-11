from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
import datetime
from django import forms


cpw_rat = [('Extreme Urgency','Extreme Urgency'),('Direct Award due to Technical or Clinical Requirement','Direct Award due to Technical or Clinical Requirement'),('Renewal with existing supplier/Interim arrangement','Renewal with existing supplier/Interim arrangement'),('Retrospective Approval','Retrospective Approval'),('Centrally Mandated Requirement','Centrally Mandated Requirement')]
div=[('Multiple Divisions','Multiple Divisions'),('F&CS Division','F&CS Division'),('Medicine Division','Medicine Division'),('Surgery Division','Surgery Division'),('Corporate Division','Corporate Division'),('Private Patients','Private Patients'),('Central','Central'),('Trust Balance Sheet','Trust Balance Sheet'),('MOHHS','MOHHS'),('Trustwide','Trustwide'),('Division A','Division A'),('Division B','Division B'),('Division C','Division C'),('Division D','Division D'),('Trust Headquarters','Trust Headquarters'),('Balance Sheet','Balance Sheet'),('Central Income','Central Income'),('Chilworth Project','Chilworth Project'),('R&D','R&D'),('UEL Theatres','UEL Theatres'),('UEL Estates','UEL Estates'),('UEL Corporate','UEL Corporate'),('HH Contract Services','HH Contract Services')]
Trust = [('HHFT','HHFT'),('UHS','UHS'),('UEL','UEL'),('HHCS','HHCS')]
YN = [('Yes','Yes'),('No','No')]

class CPW(models.Model):
    CPW_PK = models.BigAutoField(primary_key=True)
    WPL_reference = models.CharField(max_length=8)
    reference_number = models.ForeignKey('activities.activity',on_delete=models.CASCADE,related_name='cpws',related_query_name="cpw",)
    trust = models.CharField(max_length=20,choices=Trust)
    date_added_to_cpw = models.DateTimeField(auto_now_add=True)
    project_title = models.CharField(max_length=80)
    cpw_rationale = models.CharField(max_length=200,choices=cpw_rat)
    supplier = models.CharField(max_length=80)
    total_cpw_value = models.DecimalField(max_digits=30,decimal_places=2)
    division = models.CharField(max_length=80,choices=div)
    department = models.CharField(max_length=80)
    most_senior_approval_received_by = models.CharField(max_length=80)
    date_final_approval_received = models.DateField()
    one_off_purchase = models.CharField(max_length=80,choices=YN)
    contract_term = models.PositiveSmallIntegerField()
    #WPL_reference_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.WPL_reference)

    def get_absolute_url(self):
        return reverse('cpw_list',args=[str(self.id)])
