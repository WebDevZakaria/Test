import factory 
from Accounts.models import Account


from Receipt.models import Receipt

class UserFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = Account

    password = "test"    
    email = "test@gmail.com"
    username = "test"
    first_name = "testfirst"
    last_name = "testlastname"
    is_superadmin  = True
    is_staff = True






class ReceiptFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = Receipt

    owner = factory.SubFactory(UserFactory)
    storename = "X"    
    itemlist = "X"
    totalammounts = 123



