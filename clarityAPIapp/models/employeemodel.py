from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from .abstractmodel import AbstractModel


class EmployeeModel(models.Model, AbstractModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # thought Employee Num could be id
    id = models.CharField(max_length=50)
    employee_admin = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=True)
    title_role = models.CharField(max_length=75)

    class Meta:
        verbose_name = ("employee")
        verbose_name_plural = ("employees")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EmployeeModel_detail", kwargs={"pk": self.pk})
