from django.conf import settings
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm


def index(request):
    """
    Render the homepage view
    """
    return render(request, "home/index.html")


def about(request):
    """
    Render the about view
    """
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "full_name": form.cleaned_data["full_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            contact_guest_email = form["email_address"].value()
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [contact_guest_email])
                messages.success(
                    request, "Your message has been successfully sent. We will be in touch as soon as possible"
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("home")

    form = ContactForm()
    return render(request, "home/contact.html", {"form": form})
