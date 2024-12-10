from django.shortcuts import render
from django.http import HttpResponse


def domingo(request):
    return HttpResponse("Ler Livro sobre Django")


def segunda(request):
    return HttpResponse("Assistir Série Breaking Bad")


def terça(request):
    return HttpResponse("Estudar programação Python")


# def quarta(request):
#     return HttpResponse("Fazer um curso de Design Gráfico")


# def quinta(request):
#     return HttpResponse("Praticar um Esporte")


# def sexta(request):
#     return HttpResponse("none")


# def sabado(request):
#     return HttpResponse("Ir a Igreja")
