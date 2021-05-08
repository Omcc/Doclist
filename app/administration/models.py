from django.db import models
from django.utils.translation import ugettext as _
from smart_selects.db_fields import (
    ChainedForeignKey,
    ChainedManyToManyField,
    GroupedForeignKey,
)
# Create your models here.


class PersonalInformations(models.Model):
    GENDER_IN_PERSONALINFO_CHOICES = [
        ('M', _('Male')),
        ('F', _('Female')),
        ('U', _('Unknown'))
    ]
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    telephone = models.CharField(max_length=20,null=False,blank=False)
    gender = models.CharField(choices=GENDER_IN_PERSONALINFO_CHOICES,max_length=2)
    class Meta:
        abstract = True


class Country(models.Model):
    binary_code = models.CharField(max_length=2,null=False)
    triple_code = models.CharField(max_length=3,null=False)
    country_name = models.CharField(max_length=100,null=False)
    phone_code = models.CharField(max_length=6,null=False)

    def __str__(self):
        return self.country_name

class City(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100,null=False)
    plate_no = models.CharField(max_length=2,null=False)
    phone_code = models.CharField(max_length=7, null=False)

    def __str__(self):
        return self.city_name

class County(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    county_name = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.county_name

class District(models.Model):
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    district_name = models.CharField(max_length=100,null=False)
    zip_code = models.CharField(max_length=20,null=False)

class Address(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    city = ChainedForeignKey(
        "City",
        chained_field="country",
        chained_model_field="country",
        show_all=False,
        auto_choose=True,
    )
    county =ChainedForeignKey(
        "County",
        chained_field="city",
        chained_model_field="city",
        show_all=False,
        auto_choose=True,
    )
    district = models.CharField(max_length=100,null=False)
    full_address = models.CharField(max_length=100,null=False)
    postal_code = models.IntegerField(null=False)

    def __str__(self):
        return "{} {} {}".format(self.city,self.county,self.full_address)