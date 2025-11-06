from flask import Flask, render_template

app = Flask(__name__)

peliculas = {
    'suspenso' : [
        {'titulo' : 'El silencio de los inocentes',
         'sinopsis': 'Una joven agente del FBI busca la ayuda de un asesino encarcelado para atrapar a otro.'},
        {'titulo': 'perdida',
         'sinopsis': 'Un hombre se convierte en el principal sospechoso cuando su esposa desaparece.'},
    ],
    'terror':[
        {'titulo': 'El exorcista',
        'sinopsis': 'una niña es poseida por una entidad demoniaca.'},
        {'titulo': 'Hereditary',
         'sinopsis': 'Una familia es atormentada tras la muerte de su matriarca.'},
    ],
    'romance' : [
        {'titulo' : 'Orgullo y prejuicio',
         'sinopsis': 'Elizabeth bennet se enfrenta al arrogante Sr. Darcy en la inglaterra del siglo XIX.'},
        {'titulo': 'LA LA Land',
         'sinopsis': 'Un pianista de jazz y una aspirante a actriz persiguen sus sueños en Los Angeles.'},
    ],
    'Infantil':[
        {'titulo': 'Toy Story',
        'sinopsis': 'un grupo de jugetes cobran vida cuando su dueño no esta .'},
        {'titulo': 'Mi Vecino Totoro',
         'sinopsis': 'Dos hermanas se mudan al campo y se hasen amigas de un espiritu del bosque.'},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suspenso')
def suspenso():
    return render_template('suspenso.html', peliculas=peliculas['suspenso'])

@app.route('/terror')
def terror():
    return render_template('terror.html', peliculas=peliculas['terror'])

@app.route('/romance')
def romance():
    return render_template('romance.html', peliculas=peliculas['romance'])

@app.route('/infantil')
def infantil():
    return render_template('infantil.html', peliculas=peliculas['Infantil'])

if __name__== '__main__':
    app.run(debug=True)