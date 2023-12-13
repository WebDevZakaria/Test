from django.db import models
#from django.contrib.auth.models import User

from Accounts.models import Account

import uuid
# Create your models here.
class Receipt(models.Model):

    owner = models.ForeignKey(
       Account, on_delete=models.CASCADE, null=True, blank=True)
    storename = models.CharField(max_length=200, blank=True, null=True) 
    itemlist = models.TextField(blank=False, null=True) # blank false to force user to write somthing
    totalammounts = models.FloatField()
    dateofpurchase = models.DateTimeField(auto_now_add=True)
    
    id = models.UUIDField(default=uuid.uuid4, unique=True,  
                        primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.storename)
    

    