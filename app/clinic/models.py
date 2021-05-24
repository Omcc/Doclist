from django.db import models
from administration.models import Address,PersonalInformations,Language,TimeStampMixin,Specialization,Job,Title
from django.utils.translation import ugettext as _
from authentication.models import User



# Create your models here.

class ClinicType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Clinic(TimeStampMixin):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address,on_delete = models.SET_NULL,null=True)
    description = models.CharField(max_length=1000,null=True)
    clinic_type = models.ForeignKey(ClinicType,on_delete=models.SET_NULL,null=True)
    telephone = models.CharField(max_length=15)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    @property
    def images(self):
        return self.imageclinic_set.all()


    class Meta:
        verbose_name = _("Clinic")
        verbose_name_plural = _('Clinics')

    def __str__(self):
        return self.name





class Staff(TimeStampMixin,PersonalInformations):
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.SET_NULL,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    specialisations = models.ManyToManyField(Specialization)
    languages = models.ManyToManyField(Language)
    email = models.CharField(max_length=100,null=True,blank=True)
    photo = models.ImageField(upload_to='profile')
    title = models.ForeignKey(Title,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.firstname + " " + self.lastname

    @property
    def images(self):
        return self.imagestaff_set.all()

class ImageClinic(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clinics/')
    default = models.BooleanField(default=False)

class ImageStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='staffs/')
    default = models.BooleanField(default=False)











class MedicalStaff(models.Model):
    name = models.CharField(max_length=50)
    job = models.ForeignKey(Job,on_delete=models.SET_NULL,null=True)
    specializations = models.ManyToManyField(Specialization)










