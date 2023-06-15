import requests

url = 'http://127.0.0.1:5000/translate'

word_input = input("Informe uma palavra que você gostaria de traduzir: ")
option_input = input("Escolha uma opção de idioma (en para inglês ou fr para francês): ")

data = {'word': word_input, 'option': option_input} 

response = requests.post(url, json=data)

if response.status_code == 200:
    data = response.json()
    translated_word = data['translated_word']
    print(f'A palavra traduzida é: {translated_word}')
else:
    print('Erro ao fazer a solicitação.')