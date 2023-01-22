from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Testimonial
from .form import FeedbackForm
# Create your views here.
def emp_home(request):   

   emps=Emp.objects.all()
   return render(request,"emp/home.html",{
      'emps':emps
   })

def add_emp(request):
   if request.method=="POST":
         # data fetch
         emp_name=request.POST.get("emp_name")
         emp_email=request.POST.get("emp_email")
         emp_mobile=request.POST.get("emp_mobile")
         emp_address=request.POST.get("emp_address")
         emp_department=request.POST.get("emp_department")
         emp_working=request.POST.get("emp_working")
         empid=request.POST.get("empid")
   # validate


   # create model object and set the data
         e=Emp()
         e.name=emp_name
         e.email=emp_email
         e.mobile=emp_mobile
         e.emp_id=empid
         e.department=emp_department
         if emp_working is None:
          e.working=False
         else:
            e.working=True   
         e.address=emp_address

   # save the object 
         e.save()

   # prepare msg
         print("data is comming ")
         # form=EmpForm()
         # form.save()
         return redirect("/emp/home/")
   return render(request,"emp/add_emp.html",{})   


# Delete employeee
def delete_emp(request,empid):
      print(empid)
      emp=Emp.objects.get(pk=empid)
      emp.delete()
      return redirect("/emp/home/")


# Update employeee
def update_emp(request,empid):
      print(empid)
      emp=Emp.objects.get(pk=empid)
      return render(request,"emp/update_emp.html",{
            'emp':emp
            })

def do_update_emp(request,empid):
      if request.method=='POST':
         emp_name=request.POST.get("emp_name")
         emp_email=request.POST.get("emp_email")
         emp_mobile=request.POST.get("emp_mobile")
         emp_address=request.POST.get("emp_address")
         emp_department=request.POST.get("emp_department")
         emp_working=request.POST.get("emp_working")
         empid_temp=request.POST.get("empid")

         e=Emp.objects.get(pk=empid)
         e.name=emp_name
         e.email=emp_email
         e.mobile=emp_mobile
         e.emp_id=empid_temp
         e.department=emp_department
         if emp_working is None:
            e.working=False
         else:
            e.working=True   
         e.address=emp_address
         e.save()
      return redirect("/emp/home/")            


def Testimonials(request):
   testi=Testimonial.objects.all()

   return render(request,"emp/testimonials.html",{
      'testi':testi
   })


# auto creating form by django machine
def Feedback(request):
   if request.method=='POST':
      form=FeedbackForm(request.POST)
      if form.is_valid():
         print(form.cleaned_data['email'])
         print(form.cleaned_data['name'])
         print(form.cleaned_data['feedback'])
         print("Data save")
      else:
         return render(request,"emp/feedback.html",{'form':form})   
   else:
      form=FeedbackForm()
   return render(request,"emp/feedback.html",{'form':form})   