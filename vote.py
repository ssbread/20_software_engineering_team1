import django
from django.shorcus import render
from django.http import JsonResponse

def rec(request):
    return JsonResponse({'result':200,'msg':'投票成功'})
