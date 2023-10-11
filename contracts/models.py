from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

Trust = [('HHFT','HHFT'),('UHS','UHS'),('UEL','UEL'),('HHCS','HHCS')]
ProjectType = [('CPW','CPW'),('Contracting/Tendering','Contracting/Tendering'),('Catalogue Submission','Catalogue Submission'),('CIP/Cost Avoidance','CIP/Cost Avoidance'),('Contract Only (if 12 months or over please add to the Contracts Register)','Contract Only (if 12 months or over please add to the Contracts Register)')]
categories = [('Ward Based Consumables','Ward Based Consumables'),('Sterile Intervention Equipment and Associated Consumables','Sterile Intervention Equipment and Associated Consumables'),('Infection Control and Wound Care','Infection Control and Wound Care'),('Orthopaedics, Trauma & Spine, Ophthamology','Orthopaedics, Trauma & Spine, Ophthamology'),('Rehabilitation, Disabled Services, Women\'s Health & Associated Consumables','Rehabilitation, Disabled Services, Women\'s Health & Associated Consumables'),('Cardio-Vascular, Radiology, Specialist Medicine, Audiology & Pain Management','Cardio-Vascular, Radiology, Specialist Medicine, Audiology & Pain Management'),('Clinical Capital and Diagnostic Devices','Clinical Capital and Diagnostic Devices'),('Office Solutions','Office Solutions'),('Facilities & Catering','Facilities & Catering'),('Estates','Estates'),('Informatics','Informatics'),('Human Resources','Human Resources'),('Pathology','Pathology'),('Corporate','Corporate')]
sub_cats = [('Electrodes & Diathermy','Electrodes & Diathermy'),('Enteral / Dietetics','Enteral / Dietetics'),('IV Therapy','IV Therapy'),('Mobile Devices - Pump Drivers, Syringe Admin Infusion','Mobile Devices - Pump Drivers, Syringe Admin Infusion'),('Patient Assessment / Patient Monitoring','Patient Assessment / Patient Monitoring'),('Theatre & General Procedure Packs & Associated Sterile','Theatre & General Procedure Packs & Associated Sterile'),('Theatre Equipment & Staff Protective Consumables','Theatre Equipment & Staff Protective Consumables'),('Theatre Equipment & Surgical Instruments','Theatre Equipment & Surgical Instruments'),('Theatre Patient Temperature Management','Theatre Patient Temperature Management'),('Theatre Sterile Intraoperative & Post Operative Consumables','Theatre Sterile Intraoperative & Post Operative Consumables'),('ENT Consumables','ENT Consumables'),('Dressings & Woundcare','Dressings & Woundcare'),('Infection Control Consumables','Infection Control Consumables'),('Ophthalmology','Ophthalmology'),('Orthopaedics & Associated Consumables','Orthopaedics & Associated Consumables'),('Aides to Daily Living (Rehab)','Aides to Daily Living (Rehab)'),('Continence Inc Bowel Management','Continence Inc Bowel Management'),('Patient Handling','Patient Handling'),('Podiatry, Chiropody & Occupational Therapy','Podiatry, Chiropody & Occupational Therapy'),('Pressure Therapy (inc Bed Frames)','Pressure Therapy (inc Bed Frames)'),('Woman\'s Health','Woman\'s Health'),('Renal Inc. Urology Equipment & Consumables','Renal Inc. Urology Equipment & Consumables'),('Audiology','Audiology'),('Cardio-vascular, Radiology & Endoscopy','Cardio-vascular, Radiology & Endoscopy'),('Neurology & Pain Management','Neurology & Pain Management'),('Respiratory & Sleep Therapy Equipment','Respiratory & Sleep Therapy Equipment'),('Cancer Services','Cancer Services'),('Capital Leasing','Capital Leasing'),('Device Maintenance','Device Maintenance'),('Capital Replacement Programme','Capital Replacement Programme'),('Clinical equipment rental/hire','Clinical equipment rental/hire'),('Device Rental','Device Rental'),('Stationery','Stationery'),('Furniture','Furniture'),('Catering Consumables','Catering Consumables'),('Catering Food','Catering Food'),('Domestic Management - Paper','Domestic Management - Paper'),('Domestic Management - Janitorial','Domestic Management - Janitorial'),('Non Clinical Clothing, Protective Clothing, Curtains, Bedding, Haberdashery','Non Clinical Clothing, Protective Clothing, Curtains, Bedding, Haberdashery'),('Polymer (Plastics)','Polymer (Plastics)'),('Design & Build','Design & Build'),('states Goods & Services','Estates Goods & Services'),('Construction','Construction'),('Estates Capital Equipment','Estates Capital Equipment'),('I.T Software','I.T Software'),('I.T Hardware','I.T Hardware'),('I.T Consultancy','I.T Consultancy'),('Temporary Staffing','Temporary Staffing'),('Insourcing Services','Insourcing Services'),('Training Services','Training Services'),('Pathology Consumables','Pathology Consumables'),('Pathology Managed Services','Pathology Managed Services'),('Pathology Equipment Maintenance','Pathology Equipment Maintenance'),('Equipment Purchase','Equipment Purchase'),('Reagent Rental','Reagent Rental'),('Software','Software'),('Managed Services','Managed Services'),('Finance & Audit services','Finance & Audit services'),('Independent Sector','Independent Sector'),('Consultancy Services','Consultancy Services'),('Research & Development','Research & Development'),('Training Services','Training Services')]
div=[('Multiple Divisions','Multiple Divisions'),('F&CS Division','F&CS Division'),('Medicine Division','Medicine Division'),('Surgery Division','Surgery Division'),('Corporate Division','Corporate Division'),('Private Patients','Private Patients'),('Central','Central'),('Trust Balance Sheet','Trust Balance Sheet'),('MOHHS','MOHHS'),('Trustwide','Trustwide'),('Division A','Division A'),('Division B','Division B'),('Division C','Division C'),('Division D','Division D'),('Trust Headquarters','Trust Headquarters'),('Balance Sheet','Balance Sheet'),('Central Income','Central Income'),('Chilworth Project','Chilworth Project'),('R&D','R&D'),('UEL Theatres','UEL Theatres'),('UEL Estates','UEL Estates'),('UEL Corporate','UEL Corporate'),('HH Contract Services','HH Contract Services')]
agreement = [('Construction Contract','Construction Contract'),('Goods or Services','Goods or Services'),('I.T Contract','I.T Contract'),('Maintenance of Equipment Contract','Maintenance of Equipment Contract'),('Maintenance of Estate Contract','Maintenance of Estate Contract'),('NHSSC - National Pricing Matrix','NHSSC - National Pricing Matrix'),('Operating/Finance Lease','Operating/Finance Lease'),('Rebate Agreement','Rebate Agreement')]
YN = [('Yes','Yes'),('No','No')]
Route = [('Consortium Arrangement','Consortium Arrangement'),('Direct Award via Framework','Direct Award via Framework'),('Direct Award/Negotiation/CPW','Direct Award/Negotiation/CPW'),('Framework - Mini Competition','Framework - Mini Competition'),('Intra-NHS','Intra-NHS'),('Local Tender','Local Tender'),('NHSSC Category Towers','NHSSC Category Towers'),('Request for Quotation','Request for Quotation'),('Contract Extension','Contract Extension')]

class contracts(models.Model):
    contracts_PK = models.BigAutoField(primary_key=True)
    WPL_reference = models.CharField(max_length=8)
    trust = models.CharField(max_length=20,choices=Trust)
    WPL_category_area = models.CharField(max_length=200,choices=categories)
    sub_category = models.CharField(max_length=200,choices=sub_cats)
    project_title = models.TextField()
    description = models.TextField()
    division = models.CharField(max_length=200,choices=div)
    route_to_market = models.CharField(max_length=250,choices=Route)
    #date_logged = models.DateField(auto_now_add=True)
    department = models.CharField(max_length=80)
    agreement_type = models.CharField(max_length=200,choices=agreement)
    personal_info = models.CharField(max_length=200,choices=YN)
    contract_value = models.DecimalField(max_digits=30,decimal_places=2)
    contract_term = models.PositiveSmallIntegerField()
    #contract_val_pa = (contract_value*12)/contract_term
    supplier = models.TextField()
    contract_start = models.DateField()
    #contract_end = contract_start + contract_term
    extension = models.CharField(max_length=200,choices=YN)
    extension_months = models.PositiveSmallIntegerField()
    notice = models.CharField(max_length=200,choices=YN)
    notice_days = models.PositiveSmallIntegerField()
    contract_available = models.CharField(max_length=200,choices=YN)
    indexation_clause = models.CharField(max_length=200,choices=YN)
    #notice_required_by
    #days_until_contract_end
    #contract_status
    #WPL_cat_ref
    #activity_ref_trust
    WPL_lead = models.CharField(max_length=200)
    reference_number = models.ForeignKey('activities.activity',on_delete=models.CASCADE,)
    #clin_nonclin
    #link

    def __str__(self):
        return str(self.WPL_reference)

    def get_absolute_url(self):
        return reverse('contract_detail',args=[str(self.id)])
