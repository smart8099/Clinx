from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import  *
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout
from .forms import PatientInfo_Form,OPD_DataForm
from .models import PatientInfo
from django.contrib import messages

# Create your views here.
def trial (request):
    return render(request,"welcome.html")

"""admin methods """
def registerUser(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "that username is already taken")
                return redirect('adduser')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "that email is already taken")
                    return redirect('adduser')
                else:
                    new_user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                                        email=email, username=username, password=password)
                    messages.success(request,'account created successfully')
                    return redirect('adduser')



        else:
            # message that passwords don't match
            messages.error(request, 'Passwords do not match')
            return redirect('adduser')

        # check user

    else:
        return render(request, 'admin/register.html')    


"""OPD functionality section"""
def opd_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,f'welcome{user.username} ')
            return redirect('patient')

        else:
            messages.error(request,"invalid credentials")  
            return redirect('ologin')

    else:

        return render(request,"opd/opdlogin.html")   


def add_patient_info(request):
    if request.method == "GET":
        form = PatientInfo_Form()
        return render(request,'opd/opd_registration.html',{"form":form})
    else:
        form = PatientInfo_Form(request.POST)
        print(form.is_valid())
        print(form.errors.as_text)
        
        if form.is_valid():
            messages.success(request,'data added successfully')
            form.save()
        else:
            messages.error(request,'there are errors in your form')    
        return redirect('patient')           
    
        
def opd_dataview(request):
    context = {"Medical_Record":PatientInfo.objects.all()}
    
    
    return render(request,'opd/opd_data.html',context)

def opd_graphview(request):
    return render(request,'opd/opd_graph.html')    


def medical_info(request):
    if request.method == "GET":
        form = OPD_DataForm()
        return render(request,'opd/medical.html',{"form":form})    

def searchUser(request):
    search_value = request.POST['search']
    print(search_value)
    results= PatientInfo.objects.filter(Index_number = search_value)
    
    return render(request,'opd/search.html',{'results':results})  


def signout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"Goodbye")
        return redirect('trial')    



"""physician functionalities"""
def physician_login(request):
    return render(request,"physician/physicianlogin.html")

def physician_dataview(request):
    
    return render(request,'physician/phy_data.html')

def physician_graphview(request):
    return render(request,'physician/phy_graph.html')    


"""pharmacy functionalities"""
def pharmacy_login(request):
    return render(request,"pharmacy/pharmacylogin.html")

def pharmacy_dataview(request):
    
    return render(request,'pharmacy/pharm_data.html')

def pharmacy_graphview(request):
    return render(request,'pharmacy/pharm_graph.html')    




"""lab functionalities"""
def lab_login(request):
    return render(request,"lab/lablogin.html")

def lab_dataview(request):
    
    return render(request,'lab/lab_data.html')

def lab_graphview(request):
    return render(request,'lab/lab_graph.html')        