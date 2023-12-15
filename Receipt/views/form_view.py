from django.shortcuts import render,redirect
from datetime import datetime
# Create your views here.
from ..models import Receipt

from ..forms import ReceiptForm


#delete receipt function
def deletereceipt(request, pk):

    receipt = Receipt.objects.get(id=pk)

    receipt.delete()

    return redirect('receipt-list')


#create receipt fonction 
def createreceipt(request):

    receiptform = ReceiptForm()

    if request.method == "POST" :

        receiptform = ReceiptForm(request.POST)

        if receiptform.is_valid():

            receiptforms = receiptform.save(commit=False) # use commit to make changes to the form data or perform additional logic before saving it to the database
            
            receiptforms.owner = request.user

            receiptforms.save()

            return redirect('receipt-list')


    context = {'receiptform':receiptform}

    return render(request, 'receiptinfomation/createreceipt.html',context)


#update the receipt fonction
def updatereceipt(request,pk):

    receipt = Receipt.objects.get(id=pk)

    receiptform = ReceiptForm(instance=receipt)
    
    if request.method == "POST" :

        receiptform = ReceiptForm(request.POST,instance=receipt)

        if receiptform.is_valid():

            receiptforms = receiptform.save(commit=False)

            receiptforms.dateofpurchase = datetime.now()   # we use datetime to update date of purchase to the current datetime you submit the updated form 

            receiptforms.save()

            return redirect('receipt-list')

    context = {'receiptform':receiptform,"receipt":receipt}

    return render(request, 'receiptinfomation/updatereceipt.html',context)





