from django.shortcuts import render, redirect
from django.contrib.auth import models, authenticate
from django.contrib.auth import login as djangoLogin
from django.contrib.auth import logout as djangoLogout

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['nome']
        last_name = request.POST['apelido']
        password = request.POST['password']

        if models.User.objects.filter(username=username).exists():
            return render(request, 'autenticacao/registo.html', {'mensagem': 'Username already exists'})

        user = models.User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        djangoLogin(request, user)
        return redirect('welcome')

    return render(request, 'autenticacao/registo.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            djangoLogin(request, user)
            return redirect('welcome')
        else:
            return render(request, 'autenticacao/login.html', {'mensagem': 'Invalid credentials'})

    return render(request, 'autenticacao/login.html')

def logout(request):
    djangoLogout(request)
    return redirect('welcome')