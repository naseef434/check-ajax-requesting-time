from django.shortcuts import render
from django.http import HttpResponse
from time import time
from django.http import JsonResponse
# Create your views here.


def index(request):
    
    if request.is_ajax():
        t = time() 
        return JsonResponse({'seconds' : t}, status=200) 
    return render(request, 'index.html')






#status = request.GET.get('button_text')