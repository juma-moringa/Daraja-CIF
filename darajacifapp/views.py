from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def staff(request):
    return render(request,'staff.html')
def projects(request):
    return render(request,'projects.html')
def contact(request):
    return render(request,'contactus.html')
def programs(request):
    return render(request,'programs.html')