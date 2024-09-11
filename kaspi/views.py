from django.shortcuts import render
from .models import Good
from django.core.cache import cache
from django.http import HttpResponse
from .serializer import GoodSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def CacheTry(request):
    if cache.get("hello", "123123"):
        answer = "Ура, взяли с кэша"
    else:
        cache.set("hello", "123123")
        answer = "дэмн, сами сделали("

    return HttpResponse(f"HELLO - ${answer}")


# @api_view(["GET"])
# def api_good(request):
#     if request.method == "GET":
#         goods = Good.objects.all()
#         serializer = GoodSerializer(goods, many=True)
#         return Response(serializer.data)

#         # return JsonResponse(serializer.data, safe=False)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def api_good_detail(request, pk):
    if request.method == "GET":
        good = Good.objects.get(pk=pk)
        serializer = GoodSerializer(good)
        return Response(serializer.data)
    elif request.method == "PUT" or request.method == "PATCH":
        serializer = GoodSerializer(good, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        good.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def api_goods_2(request):
    if request.method == "GET":
        goods = Good.objects.all()
        serializer = GoodSerializer(goods, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = GoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
