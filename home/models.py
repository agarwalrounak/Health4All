from django.db import models
from django.urls import reverse



# Create your models here.
# Create your models here.



class Patient(models.Model):
   name = models.CharField(max_length=20)
   aadhaar_number = models.IntegerField(primary_key=True, max_length=12)
   birth_date = models.DateTimeField()
   gender = models.CharField(max_length=15)
   phone_number = models.CharField(max_length=10)
   city = models.CharField(max_length=50)
   pin_code = models.IntegerField(max_length=6)
   bloodgroup = models.CharField(max_length=3)
   allergies = models.CharField(max_length=20)
   medical_conditions = models.CharField(max_length=100)
   address = models.CharField(max_length=20)

   def __str__(self):
       return self.aadhar_number

class PatientLogin(models.Model):
    aadhaar_number=models.IntegerField(primary_key=True, max_length=12)
    password=models.CharField(max_length=30)

class DoctorLogin(models.Model):
    registration_number=models.IntegerField(primary_key=True, max_length=12)
    password=models.CharField(max_length=30)


class Doctor(models.Model):
  registration_number = models.IntegerField(primary_key=True, max_length=12)
  gender = models.CharField(max_length=15)
  phone_number = models.CharField(max_length=10)

class Medicine(models.Model):
    disease=models.CharField(max_length=50)
    medicine=models.CharField(max_length=50)

class PatientInfo(models.Model):
    aadhaar_number=models.IntegerField(primary_key=True, max_length=12)
    disease=models.ForeignKey(Medicine,on_delete=models.CASCADE)


  def __str__(self):
       return self.registration_number