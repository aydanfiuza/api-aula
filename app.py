from flask import Flask, jsonify, request

app = Flask(__name__)

words_english = {
    'fazer' : 'do',
    'vermelho' : 'red',
    'azul' : 'blue'
}

words_french = {
    'fazer' : 'faire',
    'vermelho' : 'rouge',
    'azul' : 'bleu'
}

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    word = data['word']
    option = data['option']

    if option == 'en':
        translated_word = words_english.get(word)
    elif option == 'fr':
        translated_word = words_french.get(word)
    else:
        return jsonify(error = 'Idioma não encontrado.')

    if translated_word:
        return jsonify(translated_word = translated_word)
    else:
        return jsonify(error = 'Palavra não encontrada')

if __name__ == '__main__':
    app.run()