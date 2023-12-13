from django.shortcuts import render,redirect
from django.contrib.auth import logout, login, authenticate
from .models import Account
from django.contrib import messages
from .forms import formuser
# Create your views here.

def Registerfonc(request):

    form = formuser()

    if request.method == 'POST':

        form = formuser(request.POST)


        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']   
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]

            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            
        return redirect("home-page")

    context = {"formuser":form}
    
    return render(request, 'users/register.html',context)

def loginview(request):
     
     if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']      
        try:
            receiptuser = Account.objects.get(email=email)
        except:
            messages.error(request, 'email not found')

        receiptuser = authenticate(
            request, email=email, password=password)
        
        if receiptuser is not None:

            login(request, receiptuser)

            return redirect("home-page")
        
        else:
            messages.error(request, 'password  is requered')


     return render(request, 'users/login.html')


def logoutfonc(request):

    logout(request)

    return redirect('home-page')


