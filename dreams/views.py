from django.shortcuts import render, redirect

from .forms import DreamsForm


def dreams(request):
    if request.session.get('voted'):
        return redirect("/thankyou/")

    form = DreamsForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        request.session['voted'] = True
        return redirect("/thankyou/")

    context = {"form": form}
    return render(request, "dreams/index.html", context)


def thankyou(request):
    return render(request, "dreams/thankyou.html")
