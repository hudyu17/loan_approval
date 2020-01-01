from django.http import JsonResponse

import rest_framework

from sklearn import preprocessing
from sklearn.externals import joblib

import numpy as np 
import pandas as pd 
import pickle 
import json


def calculate(request):
	mdl = joblib.load('C:/Users/Hudson Yuen/OneDrive/edits/loan_approval/loan_model.pkl')
	scalers = joblib.load('C:/Users/Hudson Yuen/OneDrive/edits/loan_approval/scaler.pkl')

	data = request.data
	unit = np.array(list(data.values))
	unit = unit.reshape(-1, 1)

	X = scalers.transform(unit)
	y_pred = mdl.predict(X)
	y_pred = (y_pred > 0.55)

	df = pd.DataFrame(y_pred, columns = ['Status'])
	df = df.replace({True: 'Approved', False: 'Rejected'})

	return JsonResponse('Your loan status is: {}'.format(df), safe = False)