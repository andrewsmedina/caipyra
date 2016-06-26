from django.shortcuts import render, redirect

from .forms import DreamsForm


def dreams(request):
    form = DreamsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/thankyou/")
    context = {"form": form}
    return render(request, "dreams/index.html", context)


def thankyou(request):
    return render(request, "dreams/thankyou.html")
