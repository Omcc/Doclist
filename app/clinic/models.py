from django.db import models
from administration.models import Address,PersonalInformations
from django.utils.translation import ugettext as _

# Create your models here.

class MedicalType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Clinic(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address,on_delete = models.SET_NULL,null=True)
    description = models.CharField(max_length=1000)
    medical_type = models.ForeignKey(MedicalType,on_delete=models.SET_NULL,null=True)

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = _("Clinic")
        verbose_name_plural = _('Clinics')

    def __str__(self):
        return self.name

class MedicalUser(PersonalInformations):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=50)

class Specialization(models.Model):
    title = models.CharField(max_length=50)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)

class MedicalStaff(models.Model):
    name = models.CharField(max_length=50)
    job = models.ForeignKey(Job,on_delete=models.SET_NULL,null=True)
    specializations = models.ManyToManyField(Specialization)









