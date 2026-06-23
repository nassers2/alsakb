from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def index(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "تم استلام طلبك بنجاح، سنتواصل معك قريباً.")
            return redirect("landing:thank_you")
    else:
        form = RegistrationForm()

    return render(request, "landing/index.html", {"form": form})


def thank_you(request):
    return render(request, "landing/thank_you.html")
