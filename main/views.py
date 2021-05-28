from django.shortcuts import render
import json
import requests
from datetime import date
from django.contrib import messages
from requests.api import request

today = date.today()




url = "https://covid-193.p.rapidapi.com/history"

headers = {
        'x-rapidapi-key': "92ce0f305bmsh5ea19e21d98ea2bp18b840jsncbe3d54b37a9",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }



# Create your views here.
def home(request):
    try:
        country_name = request.POST.get('search')
        if country_name:
            querystring = {"country":country_name ,"day":today}
        else:
            querystring = {"country":'Nepal' ,"day":today}   
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        d = response['response']
        s= d[0]
        context = {
            'date_time':s['time'] ,
            'continent': s['continent'],
            'country' : s['country'],
            'total_population': s['population'],
            'new_cases': s['cases']['new'],
            'active_cases': s['cases']['active'],
            'critical_cases': s['cases']['critical'],
            'total_recovered': s['cases']['recovered'],
            'total_cases': s['cases']['total'],
            'new_deaths': s['deaths']['new'],
            'total_deaths':s['deaths']['total'],
            'total_tests' : s['tests']['total'],
        }
        return render(request,'main/home.html',context)
    except:
        messages.error(request, "Sorry...Something Went Wrong...")

    return render(request,'main/home.html')   
