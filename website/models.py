from django.db import models
from django.core.validators import MaxValueValidator
from datetime import date, datetime
from django.utils import timezone

# Medical Staff Management Models

class Staff(models.Model):
    employeeID = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length =100)
    salary = models.IntegerField(default=50000)
    def __str__(self):
        return(f"{self.employeeID} {self.job_title}")


# Patient Management Models

class Patient(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	DOB = models.DateField()
	SSN = models.IntegerField(primary_key= True, validators=[MaxValueValidator(999999999)],unique=True)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=2)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name} ({self.SSN})")
	

# Create list of applicable doctor specialtys.
realSpecialty = [
	("General","General"),
	("Pediatrics","Pediatrics"),
	("Dermatology", "Dermatology"),
	("Surgery", "Surgery"),
	("Oncology", "Oncology"),
]

class Doctor(models.Model):
    #employeeID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    DOB = models.DateField()
    specialty = models.CharField(max_length=100, choices=realSpecialty)
    employeeID = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None, null=True, blank=True)
    def __str__(self):
        return(f"Dr.{self.first_name} {self.last_name}/ Specialty: {self.specialty} / ID: {self.id} ")

class Nurse(models.Model):
    #employeeID = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    DOB = models.DateField()
    employeeID = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None, null=True, blank=True)
    def __str__(self):
        return(f"Nurse {self.first_name} {self.last_name} / ID: {self.id} ")
          

class Illness(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	common_name = models.CharField(max_length=100)

	def __str__(self):
		return(f"{self.common_name}: {self.id}")
      

class MedicalHistory(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	illness = models.ForeignKey(Illness, on_delete=models.CASCADE)

	def __str__(self):
		return(f"Patient {self.patient} with {self.illness}")
      

class Request(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=1000)
    treatment_type = models.CharField(max_length=20, choices=[("General", "General"),
                                                              ("Surgery", "Surgery")], default='General')
    request_date = models.DateField()
    def __str__(self):
        return(f"{self.patient} to {self.description}, requestID ({self.id})")
    
    def save(self, *args, **kwargs):
        today = date.today()
        if self.request_date <= today:
            self.description = "Not Valid"

        # Save the InPatient object
        super(Request, self).save(*args, **kwargs)
    

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField(default=timezone.now)
    request = models.OneToOneField(Request, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor} on {self.scheduled_date}"




# In-Patient Management Models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    floor = models.PositiveIntegerField()
    wing = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Room {self.room_number}, Floor {self.floor}"

class Bed(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.PositiveIntegerField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.bed_number} in {self.room}"

    class Meta:
        unique_together = ('room', 'bed_number')
    
    def update_occupation_status(self):
        # Check if the bed is occupied in any InPatient record
        is_occupied = InPatient.objects.filter(bed=self, discharge_date__gte=date.today()).exists()

        # Update the is_occupied field
        self.is_occupied = is_occupied
        self.save()
        

class InPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)
    admission_date = models.DateField()
    discharge_date = models.DateField(null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    nurse = models.ForeignKey(Nurse, on_delete=models.SET_NULL,null=True,blank=True)
    treatment_type = models.CharField(max_length=20, choices=[("General", "General"),
                                                              ("Surgery", "Surgery")], default='General')

 


    def __str__(self):
        return f"In-Patient: {self.patient} in Bed {self.bed}"

    def save(self, *args, **kwargs):
        today = date.today()
        if self.discharge_date and self.discharge_date <= today:
            self.bed.is_occupied = False
        else:
            self.bed.is_occupied = True
        self.bed.save()

        # Save the InPatient object
        super(InPatient, self).save(*args, **kwargs)
