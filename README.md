Test Receipt Application

Setup


first thing to do is to clone repository :

         git clone https://github.com/WebDevZakaria/Test.git 
         
         cd Test


Create a virtual environment to install dependencies in and activate it:

         virtualenv venv
         
         venv\Scripts\activate

Then install the dependencies:

        (venv)  pip install -r requirements.txt

Note the (venv) should be  in the front of the prompt. this indicate that the terminal session is in a virtual env

Once downloading the dependencies  has finished  you can start the server by running:

    (env) python manage.py runserver


And go to your browser and navigate to http://127.0.0.1:8000.

    To run the view test run this command in your terminal:
    
     python manage.py test Receipt.tests.receipt.test_view


   
  
