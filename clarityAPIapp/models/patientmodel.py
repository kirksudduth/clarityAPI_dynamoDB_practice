from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.urls import reverse


class PatientModel(models.Model):

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False)
    referral = models.CharField(max_length=200)
    # not sure about this one
    office_time = models.CharField(max_length=50)
    report_writing = models.CharField(max_length=300)
    case_number = models.IntegerField(max_length=5)
    evaluation_date = models.DateTimeField(auto_now_add=True)
    county = models.CharField(max_length=30)
    interview_time = models.DateTimeField(auto_now_add=False)
    intake_time = models.DateTimeField(auto_now_add=False)
    father_first_name = models.CharField(max_length=25)
    father_last_name = models.CharField(max_length=25)
    mother_first_name = models.CharField(max_length=25)
    mother_last_name = models.CharField(max_length=25)
    guardian_first_name = models.CharField(
        max_length=25, blank=True, null=True)
    guardian_last_name = models.CharField(max_length=25, blank=True, null=True)
    gender = models.Charfield(max_length=25)
    is_only_child = models.BooleanField(default=False)
    # multiple siblings?? maybe list of objects?
    sibling_first_name = models.CharField(max_length=25)
    sibling_last_name = models.CharField(max_length=25)
    sibling_gender = models.CharField(max_length=25)
    sibling_dob = models.DateField(auto_now_add=False)
    id = models.CharField(max_length=50)
    has_children = models.BooleanField(default=False)
    child_first_name = models.CharField(max_length=25)
    child_last_name = models.CharField(max_length=25)
    child_gender = models.CharField(max_length=25)
    child_dob = models.DateField(auto_now_add=False)

    class Meta:
        verbose_name = ("patient")
        verbose_name_plural = ("patients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PatientModel_detail", kwargs={"pk": self.pk})
