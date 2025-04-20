from django.http import HttpResponse, HttpResponseRedirect
from .models import Visit
import django.shortcuts as render
from user_agents import parse
import requests
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location(ip):
    try:
        api_token = os.environ.get('IPINFO_TOKEN', '')
        url = f"https://ipinfo.io/{ip}/json"
        if api_token:
            url += f"?token={api_token}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        logger.debug(f"ipinfo.io response: {data}")
        return data.get('country', ''), data.get('city', '')
    except Exception as e:
        logger.error(f"Erreur ipinfo.io pour IP {ip}: {str(e)}")
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
    
    