from django import forms

class ApprovalForm(forms.Form):
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	Dependents = forms.IntegerField()
	ApplicantIncome = forms.IntegerField()	
	CoapplicantIncome = forms.IntegerField()
	LoanAmount	= forms.IntegerField()
	Loan_Amount_Term = forms.IntegerField()
	Credit_History = forms.IntegerField()
	Gender = forms.ChoiceField(choices = [
		('Male', 'Male'), 
		('Female', 'Female'), 
		('Prefer Not to Say', 'N/A'
)		])
	Married = forms.ChoiceField(choices = [('Yes', 'Yes'), ('No', 'No')])
	Graduated = forms.ChoiceField(choices = [('Yes', 'Yes'), ('No', 'No')])
	Self_Employed = forms.ChoiceField(choices = [('Yes', 'Yes'), ('No', 'No')])	
	Property_Area = forms.ChoiceField(choices = [('Rural', 'Rural'), 
		('Semiurban', 'Semiurban'), 
		('Urban', 'Urban')])