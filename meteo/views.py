from django.http import JsonResponse
import requests
from django.shortcuts import render
from datetime import date

def index_view(request):
    return render(request, "meteo/index.html")
    
    
def previsao_lisboa_view(request):
    url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    response = requests.get(url)

    if response.status_code == 200:
        allData = response.json()
        todaysData = allData['data'][0]

        todaysWeatherType = todaysData['idWeatherType']
        weatherTypeIcon = '/static/meteo/w_ic_d_' + '0' + str(todaysWeatherType) + 'anim.svg'

        getWeatherTypes = requests.get("https://api.ipma.pt/open-data/weather-type-classe.json")
        weatherTypesData = getWeatherTypes.json()

        for weatherType in weatherTypesData['data']:
            if weatherType['idWeatherType'] == todaysWeatherType:
                finalWeatherType = weatherType['descWeatherTypePT']
                break
            
        context = {'meteorologia': todaysData, 'weatherTypeIcon': weatherTypeIcon, 'finalWeatherType': finalWeatherType}

        return render(request, 'meteo/previsao_lisboa.html', context)
    else:
        context = {'error': 'Dados indisponíveis'}

        return render(request, 'meteo/previsao_lisboa.html', context)
        


def previsao(request):
    response = requests.get('https://api.ipma.pt/open-data/distrits-islands.json')
    cities = response.json().get('data')
    
    context = {'cities': cities}
    
    return render(request, 'meteo/previsao_geral.html', context)
    
    
    
def cidades_view(request):
    response = requests.get('https://api.ipma.pt/open-data/distrits-islands.json')
    cidades = response.json().get('data')
    return JsonResponse({'cidades': cidades})

def previsao_cidade(request, city_id):
    response = requests.get('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{}.json'.format(city_id))
    weathertypesResponse = requests.get('https://api.ipma.pt/open-data/weather-type-classe.json')
    weathertypes = weathertypesResponse.json()

    if response.status_code == 200:
        dic_dados = response.json()
        hoje = date.today().strftime('%Y-%m-%d')
        previsoes_proximos_dias = []
        for item in dic_dados['data']:
            if item['forecastDate'] >= hoje and len(previsoes_proximos_dias) < 5:
                descricao = ''  
                for weather in weathertypes['data']:
                    if item['idWeatherType'] == weather['idWeatherType']:
                        descricao =  weather['descWeatherTypePT']
                        break
                id_weather_type = "%02d" % item['idWeatherType']
                weather_type_url = '/static/meteo/w_ic_d_' + str(id_weather_type) + 'anim.svg'
                
                prev = {
                    'day': item,
                    'weather_type_url': weather_type_url,
                    'weatherDescription': descricao
                }

                previsoes_proximos_dias.append(prev)

    return JsonResponse({'forecast': previsoes_proximos_dias})   
    

def tempo_cidade(request, city_id):
    response = requests.get('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{}.json'.format(city_id))
    if response.status_code == 200:
        dic_dados = response.json()
        hoje = date.today().strftime('%Y-%m-%d')
        previsao_hoje = None
        for item in dic_dados['data']:
            if item['forecastDate'] == hoje:
                previsao_hoje = item
                break      

    nomecidade = ''
    response = requests.get('https://api.ipma.pt/open-data/distrits-islands.json')
    cidades = response.json().get('data', [])
    for cidade in cidades:
        if cidade['globalIdLocal'] == city_id:
            nomecidade = cidade['local']
            break

    apiresponse = dict()

    apiresponse['cidade'] = nomecidade
    apiresponse['temperatura_min'] = previsao_hoje['tMin']
    apiresponse['temperatura_max'] = previsao_hoje['tMax']
    id_weather_type = "%02d" % previsao_hoje['idWeatherType']
    apiresponse['weather_type_url'] = f'https://{request.get_host()}/static/meteo/w_ic_d_' + str(id_weather_type) + 'anim.svg'
    apiresponse['data'] = previsao_hoje['forecastDate']
    apiresponse['precipitaProb'] = previsao_hoje['precipitaProb']

    weathertypes = requests.get('https://api.ipma.pt/open-data/weather-type-classe.json')

    responsejson = weathertypes.json()
    for weather in responsejson['data']:
        if weather['idWeatherType'] == previsao_hoje['idWeatherType']:
            apiresponse['descricao'] =  weather['descWeatherTypePT']
            break


    return JsonResponse({'forecast': apiresponse})