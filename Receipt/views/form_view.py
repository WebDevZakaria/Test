from django.shortcuts import render,redirect
from datetime import datetime
# Create your views here.
from ..models import Receipt

from ..forms import ReceiptForm

def deletereceipt(request, pk):

    receipt = Receipt.objects.get(id=pk)

    receipt.delete()

    return redirect('receipt-list')



def createreceipt(request):

    receiptform = ReceiptForm()

    if request.method == "POST" :

        receiptform = ReceiptForm(request.POST)

        if receiptform.is_valid():

            receiptforms = receiptform.save(commit=False)

            receiptforms.owner = request.user

            receiptforms.save()

            return redirect('receipt-list')


    context = {'receiptform':receiptform}

    return render(request, 'receiptinfomation/createreceipt.html',context)



def updatereceipt(request,pk):

    receipt = Receipt.objects.get(id=pk)
    receiptform = ReceiptForm(instance=receipt)
    
    if request.method == "POST" :

        receiptform = ReceiptForm(request.POST,instance=receipt)

        if receiptform.is_valid():

            receiptforms = receiptform.save(commit=False)

            receiptforms.dateofpurchase = datetime.now() 

            receiptforms.save()

            return redirect('receipt-list')

    context = {'receiptform':receiptform,"receipt":receipt}

    return render(request, 'receiptinfomation/updatereceipt.html',context)




