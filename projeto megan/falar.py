import speech_recognition as sr
from gtts import gTTS
import os 
import requests
from bs4 import BeautifulSoup
from googlesearch import search

# termo de busca
query = "Pokémon XY Detonado"

# número de resultados a serem retornados
num_results = 10

# pesquisa no Google
for url in search(query, num_results=2):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string.strip() if soup.title else "N/A"
    description = soup.find("meta", {"name": "description"})["content"].strip() if soup.find("meta", {"name": "description"}) else "N/A"
    print(f"Title: {title}")

API_KEY = '6fa075125c2a4a329ff707c1f429ddf0'
cidade = 'Rio Pomba'
url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(url)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(descricao, f'{temperatura} Celsius')
#Funcao responsavel por ouvir e reconhecer a fala
def falarTempo():
    ptexto = f'Temperatura atual em {cidade}: {temperatura} graus Celsius. Clima: {descricao}'
    tts = gTTS(text = ptexto, lang='pt')
    tts.save("tempo.mp3")
    os.system("tempo.mp3")

def ouvirMicrofone():
#Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
    #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
    #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
    #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)
    try:
    #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')
    #Após alguns segundos, retorna a frase falada
        print("Você disse: " + frase)
        if (frase == 'Megan ligar' or frase == 'Mega ligar'):
            tts = gTTS(text = "Ligando.... Olá, Gustavo. O que posso fazer por você?", lang='pt')
            tts.save("mensagens.mp3")
            os.system("mensagens.mp3")
    #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnkownValueError:
        print("Não entendi")
    return frase

falarTempo()