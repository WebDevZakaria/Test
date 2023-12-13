from django.shortcuts import render

# Create your views here.
from ..models import Receipt

def showreceiptdetail(request, pk):

    receiptdetail = Receipt.objects.get(id=pk)

    context = {"receiptdetail": receiptdetail}

    return render(request, 'receiptinfomation/receiptdetail.html', context)

