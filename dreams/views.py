from django.shortcuts import render

from .forms import DreamsForm


def dreams(request):
    context = {"form": DreamsForm()}
    return render(request, "dreams/index.html", context)
