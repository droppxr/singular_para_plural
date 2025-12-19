from flask import Flask, jsonify, url_for

app = Flask(__name__)

app.json.ensure_ascii = False

@app.route('/')
def home():
    url = url_for('api', _external=True)
    return f'Rodrigo, o endpoint da API é <a href="{url}">{url}</a>'

@app.route("/plural")
def api():
    url = url_for("api", _external=True)
    return f'ENDPOINT: {url}/{'{singular}'}'

@app.route("/plural/<string:singular>")
def singular_para_plural(singular):

    dict = {'singular': '',
            'plural': ''}
    # Terminadas em ÃO
    if singular[-2:].lower() == 'ão':
        plural = singular[0:-2:] + 'ões'
        dict['plural'] = plural

    # Terminadas em A, E, I, O, U
    if singular[-1] in "aeiou":
        plural = singular + 's'
        dict = {'singular': singular,
                'plural': plural}
        
    # Terminadas em X
    elif singular[-1] == 'x':
        dict['plural'] = singular
    
    # Terminadas em R, Z

    # Terminadas em S

    # Terminadas em M

    # Terminadas em L

    # Terminadas em IL

    # Se for terminar de qualquer outra forma
    else:
        return (f'ERRO: Não conseguimos converter a palavra "{singular}" para plural')

    dict['singular'] = singular
    return jsonify (dict)

if __name__ == '__main__':
    app.run(debug=True, port=1234)
