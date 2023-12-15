from django.shortcuts import render

# Create your views here.
from ..models import Receipt


#show detail of the selected receipt function
def showreceiptdetail(request, pk):

    receiptdetail = Receipt.objects.get(id=pk)   

    context = {"receiptdetail": receiptdetail}

    return render(request, 'receiptinfomation/receiptdetail.html', context)

