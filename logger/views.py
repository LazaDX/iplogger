from django.http import HttpResponse, HttpResponseRedirect
from .models import Visit
import django.shortcuts as render
from user_agents import parse
import requests
import logging

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = response.json()
        return data.get('country', ''), data.get('city', '')
    except:
        return '', ''

def track_ip(request):
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
    ua = parse(user_agent)
    device_type = 'Mobile' if ua.is_mobile else 'Tablet' if ua.is_tablet else 'PC'
    device_model = ua.device.model or ''
    device_brand = ua.device.brand or ''
    country, city = get_location(ip)
    Visit.objects.create(
        ip_address=ip,
        user_agent=user_agent,
        device_type=device_type,
        device_model=device_model,
        device_brand=device_brand,
        country=country,
        city=city
    )
    
    return HttpResponseRedirect('https://www.google.com')



    # message = (
    #     f"IP Address: {ip}, User Agent: {user_agent}<br>"
    #     f"Device Type: {device_type}, Model: {device_model or 'N/A'}, Brand: {device_brand or 'N/A'}<br>"
    #     f"Location: {city or 'N/A'}, {country or 'N/A'}<br>"
    # )
    
    # return HttpResponse(message)
    
    