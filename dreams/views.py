from django.shortcuts import render


def dreams(request):
    return render(request, "dreams/index.html")
