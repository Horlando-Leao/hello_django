import json

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


# Create your views here.
def hello(request, nome, idade):
    return JsonResponse({'app': 'hello world', 'nome': nome, 'idade': idade})


def multiplicar(request, valor1, valor2):
    rs = dict()
    rs['operacao'] = 'multiplicar'
    rs['resultado'] = valor1 * valor2
    return JsonResponse(rs)

def dividir(request, valor1, valor2):
    rs = dict()
    rs['operacao'] = 'dividir'
    rs['resultado'] = valor1 / valor2
    return JsonResponse(rs)

def somar(request, valor1, valor2):
    rs = dict()
    rs['operacao'] = 'somar'
    rs['resultado'] = valor1 + valor2
    return JsonResponse(rs)

def subtrair(request, valor1, valor2):
    rs = dict()
    rs['operacao'] = 'subtrair'
    rs['resultado'] = valor1 - valor2
    return JsonResponse(rs)