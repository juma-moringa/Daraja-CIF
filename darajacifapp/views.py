from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from darajacifapp.forms import ContactForm

# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def staff(request):
    return render(request, "staff.html")


def projects(request):
    return render(request, "projects.html")


def programs(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


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
