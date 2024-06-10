from django.shortcuts import render

def welcome_view(request):
    return render(request, 'welcome/welcome.html')

def mebyme_view(request):
    return render(request, 'welcome/mebyme.html')

def about_view(request):
    return render(request, 'welcome/about.html')












