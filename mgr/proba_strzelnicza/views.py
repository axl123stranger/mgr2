from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return render(request, "proba_strzelnicza/index.html", {
        "proba_strzelnicza": ProbaStrzelnicza.objects.all()
    })


def proba_strzelnicza(request, id_proby):
    proba_strzelnicza = ProbaStrzelnicza.objects.get(pk=id_proby)
    return render(request, "proba_strzelnicza/proba_strzelnicza.html", {
        "proba_strzelnicza": proba_strzelnicza




    })
