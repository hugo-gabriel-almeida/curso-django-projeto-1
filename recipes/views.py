from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Hugo Almeida',
    })


def contact_us(request):
    return HttpResponse('contact us')


def about(request):
    return HttpResponse('about')
