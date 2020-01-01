#handles HTTP requests, converts info in models to json file

from rest_framework import serializers 
from . models import approvals #model name

class ApprovalsSerializer(serializers.ModelSerializer):
	class Meta:
		model = approvals
		#fields by default has all 
