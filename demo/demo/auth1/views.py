from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from auth1.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.db.models import F

from .models import Department, Employees

qs = Employees.objects.all()

# Create your views here.

def index(request):
    template = loader.get_template('auth1/index.html')
    return render(request, 'auth1/index.html',{'STATIC_URL': settings.STATIC_URL})


def department(request,department_id):
    no_of_employees = Employees.objects.filter(department=department_id).count()
    #output = ', '.join([d.department_name for d in Department.objects.all().filter(department_id=department_id)]).join(', ').join(no_of_employees)
    return HttpResponse(no_of_employees)

#def main(request):
   # rform1 = forms.RegistrationForm()
   # return render_to_response("auth1/", {'form1': rform1})
def register_user(request):
    return render(request,'auth1/pages/register_user.html')

def register_department(request):
    return render(request,'auth1/pages/register_department.html')

def register(request):
    return render(request,'auth1/pages/register.html')

def login(request):
    return render(request,'auth1/pages/register.html')


#def register(request):
#    if request.method == 'POST':
#        rform1 = RegistrationForm(request.POST)
#        if rform1.is_valid():
#            post = form.save(commit=False)
#            post.user_name = form.cleanded_data['user']
#            post.password = form.cleaned_data['pass']
#            post.save()
#    else:
#        rform1 = RegistrationForm()
#           # return HttpResponseRedirect("/register-success/")
#        return render("auth1/pages/register.html",{'form':rform1})


def employee_success(request):
    if request.method == 'POST':
        u = request.POST['user']
        p = request.POST['pass']
        d1 = request.POST['dep']
        if Employees.objects.filter(user_name=u).count()==1:
            return render(request,'auth1/pages/register_user.html', {'error': 'Username already exists'})
        else:
            Department.objects.filter(department_name=d1).update(no_of_employees=F('no_of_employees')+1)
            e = Employees(user_name = u, password = p,department_name = d1, join_date = datetime.now())
            e.save()
            return render(request,'auth1/pages/employee_success.html', {'answer': u})

def department_success(request):
    if request.method == 'POST':
        u = request.POST['name']
        no = Employees.objects.filter(department_name=u).count()
        d = Department(department_name = u,no_of_employees = no)
        d.save()
        return render(request,'auth1/pages/department_success.html', {'answer': u})

def profile(request):
    if request.method == 'POST':
        u = request.POST['user']
        p = request.POST['pass']
        
        if get_object_or_404(Employees,password=p,user_name=u):
            request.session['logged_in'] = u
            #deps = Employees.objects.values('department_name').filter(user_name=u)
            deps = Employees.objects.get(user_name=u)
            deps1 = deps.department_name
            return render(request,'auth1/pages/profile.html', {'deps1': deps1, 'answer': u})
        else:
            return render(request,'auth1/pages/login.html', {'error': 'Username or Password is incorrect'})

def logout(request):
    if 'logged_in' in request.session:
        del request.session['logged_in']
        return render(request,'auth1/index.html', {'error': 'Logged out'})
    
