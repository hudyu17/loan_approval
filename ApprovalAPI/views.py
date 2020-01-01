#view functions takes a Web request and returns a Web response
#houses most of the algorithm / logic

from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from .models import approvals
from .serializers import ApprovalsSerializer
from .forms import ApprovalForm

from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from sklearn import preprocessing
from sklearn.externals import joblib

import numpy as np 
import pandas as pd 
import pickle 
import json
import tensorflow.keras

# from .loan_model import calculate

class ApprovalsView(viewsets.ModelViewSet):
	queryset = approvals.objects.all()
	serializer_class = ApprovalsSerializer

def approvereject(unit):
	try:
		mdl = joblib.load('C:/Users/Hudson Yuen/OneDrive/edits/loan_approval/loan_model.pkl')
		scalers = joblib.load('C:/Users/Hudson Yuen/OneDrive/edits/loan_approval/scaler.pkl')

		# data = request.data
		# unit = np.array(list(data.values))
		# unit = unit.reshape(-1, 1)

		X = scalers.transform(unit)
		y_pred = mdl.predict(X)
		y_pred = (y_pred > 0.55)

		df = pd.DataFrame(y_pred, columns = ['Status'])
		df = df.replace({True: 'Approved', False: 'Rejected'})
		return JsonResponse('Your loan status is: {}'.format(df), safe = False)
	
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def ohevalue(df):
	ohe_col = joblib.load('C:/Users/Hudson Yuen/OneDrive/edits/loan_approval/ohe_col.pkl')
	cat_columns = ['Gender', 'Married', 'Graduated', 'Self_Employed', 'Property_Area']
	df_processed = pd.get_dummies(df, columns = cat_columns)

	new_dict = {}
	for i in ohe_col:
		if i in df_processed.columns:
			new_dict[i] = df_processed[i].values
		else:
			new_dict[i] = 0

	new_df = pd.DataFrame(new_dict)
	return new_df

def userform(request):
	if request.method == 'POST':
		form = ApprovalForm(request.POST)
		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			Dependents = form.cleaned_data['Dependents']
			ApplicantIncome = form.cleaned_data['ApplicantIncome']
			CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
			LoanAmount = form.cleaned_data['LoanAmount']
			Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
			Credit_History = form.cleaned_data['Credit_History']
			Gender = form.cleaned_data['Gender']
			Married = form.cleaned_data['Married']
			Graduated = form.cleaned_data['Graduated']
			Self_Employed = form.cleaned_data['Self_Employed']
			Property_Area = form.cleaned_data['Property_Area']

			Dict = (request.POST).dict()
			df = pd.DataFrame(Dict, index = [0])
			print(approvereject(ohevalue(df)))
	else: 
		form = ApprovalForm()

	return render(request, 'apiform/userform.html', {'form': form})