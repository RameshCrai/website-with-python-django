from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    isActive=True
    if request.method=='POST':
        check=request.POST.get('check')
        print(check)
        if check is None : isActive=False
        else:
            isActive=True

    date=datetime.datetime.now()

    name="Raycoding"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number ',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triagle'
    ]
    
    students={
        'student_name':"ramesh",
        'student_college':"NMC",
        'student_city':"KTM",
    }
    #return HttpResponse("<h1>This is checking system of python</h1>"+str(date))
    data={
      'date':date,
      'isActive':isActive,
      'name':name,
      'list_of_programs':list_of_programs,
      'students_data':students,
    }
    return render(request,"home.html",data)

def services(request):
    #return HttpResponse("<h1>This is Services area </h1>")
    return render(request,"services.html",{})

def about(request):
    #return HttpResponse("<h3>This is checking system of python</h3>")   
    return render(request,"about.html",{}) 