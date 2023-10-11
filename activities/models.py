from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

Trust = [('HHFT','HHFT'),('UHS','UHS'),('UEL','UEL'),('HHFT & UHS','HHFT & UHS'),('HHCS','HHCS'),('HHFT & UEL','HHFT & UEL')]
ProjectType = [('CPW','CPW'),('Contracting/Tendering','Contracting/Tendering'),('Catalogue Submission','Catalogue Submission'),('CIP/Cost Avoidance','CIP/Cost Avoidance'),('Contract Only','Contract Only')]
WPLLead = [('Adam Skeates','Adam Skeates'),('Amber Burton','Amber Burton'),('Andras Doczi','Andras Doczi'),('Andrea Sleap','Andrea Sleap'),('Anjay Chauhan','Anjay Chauhan'),('Bryn Webb','Bryn Webb'),('Chloe Lacy','Chloe Lacy'),('Claire Charles','Claire Charles'),('David Duly','David Duly'),('David Tozer','David Tozer'),('Emma Ames','Emma Ames'),('George Oliphant','George Oliphant'),('Holly Gooderham','Holly Gooderham'),('Ilona Holt','Ilona Holt'),('Jayne Oxenham','Jayne Oxenham'),('Jessica Comer','Jessica Comer'),('Joanne Pearce','Joanne Pearce'),('John Ayres','John Ayres'),('John Godfrey','John Godfrey'),('Kate Penfield','Kate Penfield'),('Katie Mooney','Katie Mooney'),('Kelly Boadas','Kelly Boadas'),('Rachel Ames','Rachel Ames'),('Rebecca  Vinton','Rebecca Vinton'),('Rob Houston','Rob Houston'),('Sally Turner','Sally Turner'),('Sam Kyuma','Sam Kyuma'),('Sam Morant','Sam Morant'),('Simon Wright','Simon Wright'),('Victoria Williams','Victoria Williams'),('Will Garvey','Will Garvey')]

class activity(models.Model):
    reference_number = models.BigAutoField(primary_key=True)
    WPL_reference_number = models.CharField(max_length=8)
    WPL_lead = models.CharField(max_length=200,choices=WPLLead)
    date_logged = models.DateTimeField(auto_now_add=True)
    trust = models.CharField(max_length=20,choices=Trust)
    project_title = models.TextField()
    project_type = models.CharField(max_length=80,choices=ProjectType)
    supplier = models.TextField(blank=True)




    #link


    def __str__(self):
        return str(self.reference_number)

    def get_absolute_url(self):
        return reverse('activity_detail',args=[str(self.id)])
