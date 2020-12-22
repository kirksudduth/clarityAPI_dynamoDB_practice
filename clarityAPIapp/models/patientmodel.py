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
    marital_status = models.CharField(max_length=25)
    spouse_first_name = models.Charfield(max_length=25)
    spouse_last_name = models.Charfield(max_length=25)
    spouse_gender = models.CharField(max_length=25)
    spouse_dob = models.DateField(auto_now_add=False)
    consent = models.BooleanField(default=False)

    # Termination of Parental Rights
    unforeseeable_future_change = models.BooleanField(default=False)
    conviction_imprisonment_felony = models.BooleanField(default=False)
    emotional_illness_mental_deficiency = models.BooleanField(default=False)
    unable_discharge_childcare_responsibility = models.BooleanField(
        default=False)
    excess_use_controlled_substance = models.BooleanField(default=False)
    rehab_failure = models.BooleanField(default=False)
    serious_bodily_injury_child = models.BooleanField(default=False)
    willful_neglect_abandonment = models.BooleanField(default=False)
    loss_custody_other_children = models.BooleanField(default=False)
    failure_maintain_material_needs = models.BooleanField(default=False)
    failure_maintain_consistent_contact = models.BooleanField(default=False)
    parent_has_abused_child = models.BooleanField(default=False)
    lack_effort_adjust_circumstances = models.BooleanField(default=False)

    # Interview
    times_DHR_interacted_with = models.CharField(max_length=25)
    inference_observations = models.CharField(max_length=300)
    dhr_alleged = models.CharField(max_length=500)
    misconstrued_dhr = models.CharField(max_length=400)
    truth_in_dhr_allegations = models.CharField(max_length=500)
    dhr_steps_taken = models.CharField(max_length=300)
    dhr_steps_taken_by_patient = models.Charfield(max_length=400)
    understanding_why_here = models.CharField(max_length=400)

    times_involved_dhr_al = models.CharField(max_length=25)
    times_involved_other_child_protective_agencies = models.CharField(
        max_length=300)
    how_good_emotionally_now_and_future_children = models.CharField(
        max_length=500)
    how_temperament_dovetail_with_children_now_future = models.CharField(
        max_length=500)
    how_discipline_child = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("patient")
        verbose_name_plural = ("patients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PatientModel_detail", kwargs={"pk": self.pk})
