from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import hash_serializer
from rest_framework.response import Response
from django.http import JsonResponse
from .models import save_data
from rest_framework import status


@api_view(["POST", "GET"])
def hash_serializer_view(request):

    if request.method == 'POST':
        hashes = save_data.objects.filter(word=request.data["word"]).first()
        if hashes == None:
            serializer = hash_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        hashes = save_data.objects.all()
        serializer = hash_serializer(hashes, many=True)
        return JsonResponse(serializer.data, safe=False)


def hash_checker(request, Hash, hash_type):
    if hash_type == "md5":
        Object = save_data.objects.filter(md5_hash=Hash)
    elif hash_type == "sha256":
        Object = save_data.objects.filter(sha256_hash=Hash)
    elif hash_type == "sha224":
        Object = save_data.objects.filter(sha224_hash=Hash)
    context = {
        "word": '',
        "error": False
    }
   
    if Object.first() is None:
        context["error"] = True
    elif Object.first() != None:
        context["word"] = Object.first().word
  
    return JsonResponse({"word":context["word"] , "error":context["error"]})
