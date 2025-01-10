#This is my views.py file
from django.shortcuts import render


def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75082&distance=20&API_KEY=2C004E4B-01BF-4362-B814-DEA6EB3F1A2A")
	error_msg = "Oops we have an error.."

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = error_msg

	return render(request, 'home.html', {'api' : api})

def about(request):
	return render(request, 'about.html', {})