from django.shortcuts import render

from .forms import DreamsForm


def dreams(request):
    form = DreamsForm(request.POST or {})
    if form.is_valid():
        form.save()
        return redirect("/ok/")
    context = {"form": form}
    return render(request, "dreams/index.html", context)
