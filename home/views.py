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
            return contact_form(form, request)
    form = ContactForm()
    return render(request, "home/contact.html", {"form": form})


# TODO Rename this here and in `contact`
def contact_form(form, request):
    subject = "Daniela's Art Shop - Contact Request"
    body = {
        "full_name": form.cleaned_data["full_name"],
        "email": form.cleaned_data["email_address"],
        "message": form.cleaned_data["message"],
    }
    message = "\n".join(body.values())

    contact_guest_email = form["email_address"].value()
    try:
        send_mail(subject, message, contact_guest_email, [settings.EMAIL_HOST_USER])
        messages.success(
            request,
            "Your message has been successfully sent. We will be in touch as soon as possible",
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    return redirect("home")
