import requests
import matplotlib.pyplot as plt
url = 'https://api.open-meteo.com/v1/forecast?latitude=-18.729616262361755&longitude=-39.8445161110831&hourly=cloud_cover&timezone=America%2FSao_Paulo&forecast_days=3'
response = requests.get(url)
if response.status_code == 200: # caso ele tenha conseguido se comunicar
    data = response.json() # guarda meus dados em um formato json
    time = data["hourly"]["time"]
    cloud_cover = data["hourly"]["cloud_cover"]
    # O '[]' no meio do for significa que a cada item que adiciono, ele já sai no formato de lista
    form_time = [t.split('T')[1] for t in time] # no tempo, divido em 2 strings a partir do caractere 'T', e depois pego o item 1 dessa string separada
    # Plot do gráfico
    plt.figure()
    plt.plot(form_time, cloud_cover, marker='o', linestyle='-', color='b')
    plt.show()
elif response.status_code == 404:
    print('Não encontrado!')
else: 
    print('Ocorreu outro erro...')