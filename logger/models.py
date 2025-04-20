from django.db import models
import uuid

class Visit(models.Model):
       ip_address = models.GenericIPAddressField()
       user_agent = models.TextField()
       timestamp = models.DateTimeField(auto_now_add=True)
       device_type = models.CharField(max_length=50, blank=True)  
       device_model = models.CharField(max_length=100, blank=True)  
       device_brand = models.CharField(max_length=100, blank=True) 
       country = models.CharField(max_length=100, blank=True) 
       city = models.CharField(max_length=100, blank=True)  
       redirect_url = models.URLField(blank=True)  
       link_id = models.CharField(max_length=36, blank=True, default=uuid.uuid4) 
def __str__(self):
    return f"Visit from {self.ip_address} ({self.device_type}) at {self.timestamp}"