from django.db import models

# Create your models here.
from VAYU_MAIN.models import User


class Disease(models.Model):
    name = models.CharField(max_length=35, verbose_name="Disease Name")
    description = models.TextField(max_length=250, verbose_name="Disease Description")
    symptoms = models.TextField(max_length=150, verbose_name="Main Symptoms")


class HealthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=1, verbose_name="Gender")
    blood_group = models.CharField(max_length=3, verbose_name="Blood Group")
    chronic_disease = models.ManyToManyField(Disease, null=True, blank=True)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50, verbose_name="Qualification")
    fees = models.IntegerField(verbose_name="Consultaion Fees")
    diseases = models.ManyToManyField(Disease, null=True, blank=True)
    license_image = models.ImageField(verbose_name="Doctor License")


class LabTechnician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tests = models.TextField(max_length=250, verbose_name="Tests Performed")
    fees = models.IntegerField(verbose_name="Test Fees")

