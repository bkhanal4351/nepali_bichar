from django.shortcuts import render


def index(request):
  return render(request, 'fixit/index.html')

def add_fix(request):
  return render(request, 'fixit/add_fix')
