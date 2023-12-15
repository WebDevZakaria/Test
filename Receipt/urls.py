from django.urls import path

from Receipt.views import list_view,form_view,detail_view

urlpatterns = [

    path('', list_view.homepage, name='home-page'),
    path('listofreceipt/', list_view.listofReceipt, name='receipt-list'),
    path('delete/<str:pk>', form_view.deletereceipt, name='delete-receipt'),
    path('createreceipt/', form_view.createreceipt, name='create-receipt'),
    path('updatereceipt/<str:pk>', form_view.updatereceipt, name='update-receipt'),
    path('showdetail/<str:pk>', detail_view.showreceiptdetail, name='show-receipt'),


]
