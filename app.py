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
    option_str = str(option)

    if option_str.lower() == 'fr':
        translated_word = words_french.get(word)
    else:
        translated_word = words_english.get(word)


    if translated_word:
        return jsonify(translated_word = translated_word)
    else:
        return jsonify(error = 'Palavra não encontrada')

if __name__ == '__main__':
    app.run()