from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User

class EmployeeModel(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_number = models.CharField(max_length=50)
    employee_admin = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("employee")
        verbose_name_plural = ("employees")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EmployeeModel_detail", kwargs={"pk": self.pk})
