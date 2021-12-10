import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def hello(request, nome, idade):
    return JsonResponse({'app': 'hello world', 'nome': nome, 'idade': idade})
