from django.test import TestCase
from django.urls import reverse
from Accounts.models import Account
from Receipt.models import Receipt


class ReceiptCRUDTests(TestCase):
    def setUp(self):
        # Create a test Account
        self.user =Account.objects.create_user(
                first_name="mohamed", last_name="bour", email="mohamed@gmail.com", username="mohamed", password="mohamed123")  
        
        

        # Create an receipt associated with the test account
        self.receipt = Receipt.objects.create(
            owner=self.user,
            storename='Test store',
            itemlist='test item list',
            totalammounts=1234,    
            
        )

        
     #test  receipt list view
    def test_receipt_list_view(self):

        self.client.login(email='mohamed@gmail.com', password='mohamed123')

        response = self.client.get('/listofreceipt/')

        self.assertEqual(response.status_code, 200) # to check if it's successful

        self.assertContains(response, 'Test store')  # check if the list contains the test receipt added


    #test receipt view for create new receipt
    def test_receipt_new(self):

        self.client.login(email='mohamed@gmail.com', password='mohamed123')

        response = self.client.get('/createreceipt/')

        self.assertEqual(response.status_code, 200) # to check if it's successful
    
        response = self.client.post('/createreceipt/', {'storename': 'new Test store', 'itemlist':'new test item','totalammounts': 1332})

        new_receipt = Receipt.objects.get(storename='new Test store')

        self.assertIsNotNone(new_receipt)

        self.assertEqual(new_receipt.owner, self.user)


   