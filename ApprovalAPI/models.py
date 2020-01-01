from django.db import models

#each model maps to a database table; is subclass of model
class approvals(models.Model):
	#define user input options; first term in tuple for reference, second term for display
	GENDER_CHOICES = (
		('Male', 'Male'), 
		('Female', 'Female'), 
		('Prefer Not to Say', 'N/A')
	)

	YES_NO_CHOICES = (
		('Yes', 'Yes'), 
		('No', 'No')
	)

	PROPERTY_AREA_CHOICES = (
		('Rural', 'Rural'), 
		('Semiurban', 'Semiurban'), 
		('Urban', 'Urban')
	)

	#class attributes represent database fields
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	dependents = models.IntegerField(default = 0)
	applicant_income = models.IntegerField(default = 0)	
	coapplicant_income = models.IntegerField(default = 0)
	loan_amount	= models.IntegerField(default = 0)
	loan_amount_term = models.IntegerField(default = 0)
	credit_history = models.IntegerField(default = 0)
	gender = models.CharField(max_length = 15, choices = GENDER_CHOICES)
	married = models.CharField(max_length = 15, choices = YES_NO_CHOICES)
	graduated = models.CharField(max_length = 15, choices = YES_NO_CHOICES)
	self_employed = models.CharField(max_length = 15, choices = YES_NO_CHOICES)
	property_area = models.CharField(max_length = 15, choices = PROPERTY_AREA_CHOICES)

	def __str__(self):
		return self.firstname