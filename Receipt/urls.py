from django.urls import path

from Receipt.views import list_view as listviews
from Receipt.views import form_view as formviews
from Receipt.views import detail_view as detailviews


urlpatterns = [

    path('', listviews.homepage, name='home-page'),
    path('listofrecipt/', listviews.listofReceipt, name='receipt-list'),
    path('showdetail/<str:pk>', detailviews.showreceiptdetail, name='show-receipt'),

    path('delete/<str:pk>', formviews.deletereceipt, name='delete-receipt'),
    path('createreceipt/', formviews.createreceipt, name='create-receipt'),
    path('updatereceipt/<str:pk>', formviews.updatereceipt, name='update-receipt'),
       
]
