from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    return HttpResponse('Posts')

def post_detail(request):
    return HttpResponse('Post')

def test_view(request):
    return HttpResponse('Post')