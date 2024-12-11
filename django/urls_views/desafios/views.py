from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def desafio_semana_numero(request, dia):
    return HttpResponse(dia)
    

def desafio_semana(request, dia):
    desafio = ""
    if dia == 'domingo':
        desafio = 'Ler Livro sobre django'
    elif dia == 'segunda':
        desafio = 'Assistir Série Breacker bad'
    elif dia == 'terça':
        desafio = 'Estudar programação em python'
    else:
        return HttpResponseNotFound("Não há desafio para esse dia informado")
    
    return HttpResponse(desafio)
