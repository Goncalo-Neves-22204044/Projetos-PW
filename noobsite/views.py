from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def helloWorld(request):
    return HttpResponse("Hello world!")

def getName(request):
    return HttpResponse("O meu nome é Gonçalo Neves!")

def getAge(request):
    return HttpResponse("Tenho 21 anos!")

