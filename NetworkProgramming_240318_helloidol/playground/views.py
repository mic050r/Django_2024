from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello")

def say_hello_html(request):
    return render(request, 'playground/hello.html', {'name' : '준수야', 'greeting' : '안녕'})

def say_bye_html(request):
    context = {
        'title': 'Loving You Keeps Me Alive',
        'singer': '김준수, 정선아',
    }
    return render(request, 'playground/bye.html', context=context)