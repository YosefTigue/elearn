from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import SignupForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, "core/home.html", )

def department(request):
    
    return render(request, "core/department.html",{
        "departments": Department.objects.all()
    })
    
def about(request):
    return render(request, "core/about.html")

def detail(request, pk):
    dept = get_object_or_404(Department, pk =pk)
    return render(request, "core/dept.html", {
        "dept": dept
    })
    

def signup(request):
    if request.method =="POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html',{
        'form': form
    })
    
def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('index')
    



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name' ]
            email=form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            html= render_to_string('core/emails/contactform.html',{
                'name': name,
                'email': email,
                'content': content 
                
            })
            send_mail('the contact form subject', 'This is the message', 'yoseftigue21@gmail.com', ['yoseftigue21@gmail.com'], html_message= html )
            
            return redirect('index')
            
    else:
        form = ContactForm()   
               
    return render(request,"core/contact.html",{
        "form": form
        
    })