from django.shortcuts import render
from .models import Good
from django.core.cache import cache
from django.http import HttpResponse


def CacheTry(request):
    if cache.get("hello", "123123"): 
        answer = "Ура, взяли с кэша"
    else: 
        cache.set("hello", "123123")
        answer = "дэмн, сами сделали("

    return HttpResponse(f"HELLO - ${answer}")

    
    
