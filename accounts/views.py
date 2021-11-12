from django.shortcuts import render


def accounts(request):
    """Display the user's profile."""

    template = "accounts/accounts.html"
    context = {}

    return render(request, template, context)
