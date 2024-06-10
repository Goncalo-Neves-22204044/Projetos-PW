from django.shortcuts import render
from datetime import datetime

def index_view(request):
    return render(request, "pwsite/index.html")

def about_view(request):
    return render(request, "pwsite/sobre.html")

def interests_view(request):
    current_date = datetime.now().date()
    context = {'current_date': current_date}
    return render(request, "pwsite/pw.html", context)