from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactsForm, NameForm


def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data["your_name"]
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))


    else:
        form = NameForm()

    return render(request, "contacts/name.html", {"form": form})


def thanks(request, name):
    return HttpResponse(f"Thanks for submitting your name, {name}!")


def create(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["subject"]
            form.save()
            return HttpResponseRedirect(reverse("contacts:thanks", args=(name,)))
            
    else:
        form = ContactsForm()
    return render(request, "contacts/create.html", {"form": form})