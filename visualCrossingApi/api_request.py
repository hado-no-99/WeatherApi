import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_weather(url):
	localBaseUrl = "http://localhost:8000/"
	remoteBaseUrl = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
	query_url = str(url).replace(localBaseUrl, remoteBaseUrl)

	api_key = os.getenv("API_KEY")
	api_key_param = {"key": api_key}

	r = requests.get(query_url, params=api_key_param)
	return r.json()