from django.shortcuts import render , redirect

def redirecter(request):
    return redirect('/hash_api')