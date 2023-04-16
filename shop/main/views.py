from django.shortcuts import render


def index(request):
    context = {'title': 'Main Page'}
    return render(request, 'main/index.html', context=context)
