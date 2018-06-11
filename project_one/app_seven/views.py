from django.shortcuts import render


def index(request):
    return render(request, 'index.html')   # if they request index pass in index.html


def other(request):
    return render(request, 'other.html')


def relative(request):
    return render(request, 'relative_url_templates.html')
