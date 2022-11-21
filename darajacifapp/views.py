from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from darajacifapp.forms import ContactForm
from darajacifapp.models import Blog, Gallery, Projects


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def staff(request):
    return render(request, "staff.html")


def projects(request):
    allproject = Projects.objects.all()
    params = {
        "projects": "Projects",
        "allproject": allproject,
    }
    return render(request, "projects.html", params)
def projectdtls(request):
    allproject = Projects.objects.all()
    params = {
        "projects": "Projects",
        "allproject": allproject,
    }
    return render(request, "projectdtls.html", params)


def programs(request):
    return render(request, "programs.html")


def gallery(request):
  photos = Gallery.objects.all()
  params = {
    'gall': 'Gallery',
    'photos':photos
  }
  return render(request, 'gallery.html', params)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Daraja CIF Website Inquiry"
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())
            try:
                send_mail(
                    subject, message, "admin@example.com", ["darajacivic@gmail.com"]
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("/")

    form = ContactForm()
    return render(request, "contactus.html", {"form": form})

def myblogs(request):
    blogs = Blog.objects.all()

    return render(request,"blogs.html",{'blogs':blogs})

