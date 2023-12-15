from django.shortcuts import render

# Create your views here.
from ..models import Receipt


#the home page function 
def homepage(request):


    return render(request,'receiptinfomation/index.html')

# list of the user receipt  function
def listofReceipt(request):

    receipt = Receipt.objects.filter(owner = request.user)   # select the list of receipt  that have the log in user

    context = {"receipt": receipt}
    
    return render(request, 'receiptinfomation/receiptlist.html', context)

