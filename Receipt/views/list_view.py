from django.shortcuts import render

# Create your views here.
from ..models import Receipt



def homepage(request):


    return render(request,'receiptinfomation/index.html')



def listofReceipt(request):

    receipt = Receipt.objects.filter(owner = request.user)

    context = {"receipt": receipt}
    
    return render(request, 'receiptinfomation/receiptlist.html', context)

