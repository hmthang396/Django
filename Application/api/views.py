from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_home(request,*arg,**kwargs):
    return JsonResponse({"message":"Test"})