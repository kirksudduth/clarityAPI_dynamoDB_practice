from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.urls import reverse


class PatientModel(models.Model):
  
    patient_first_name = models.CharField(max_length=50)
    patient_middle_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    patient_Date_of_Birth = models.DateField(auto_now=False)
    patient_referral = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = ("patient")
        verbose_name_plural = ("patients")
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PatientModel_detail", kwargs={"pk": self.pk})
