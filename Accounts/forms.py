
#from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Account

class formuser(ModelForm):

    class Meta:

        model = Account

        fields = ['first_name', 'last_name', 'password','email']





