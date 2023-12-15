from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def saludar():
    return '¡Hola! Bienvenido a mi aplicación Flask.'

@app.route('/mensaje', methods=['POST'])
def recibir_mensaje():
    if request.method == 'POST':
        data = request.get_json() 
        print('Datos recibidos:', data)

        return jsonify({'mensaje': 'Datos recibidos correctamente'}), 200
    else:
        return jsonify({'error': 'Método no permitido'}), 405

if __name__ == '__main__':
    app.run(debug=True)
