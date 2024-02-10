from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Product
from .models import MainProduct

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method== 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        
        if password==confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Registered')
                return redirect('signup')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('signup')
            
            else:
                user =User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login2')
        else:
            messages.info(request,'Password Not Matched')
            return render(request,'signup.html')
   
    else:    
        return render(request,'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login2')
    else:
        return render(request,'login2.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def products(request):
    product= Product.objects.all()
    
    
    return render(request, 'products.html', {'product': product})

def cart(request):
    
    return render(request,'cart.html')
    
def mainproducts(request):
    mproduct= MainProduct.objects.all()
    
    
    return render(request, 'index.html', {'mproduct': mproduct})