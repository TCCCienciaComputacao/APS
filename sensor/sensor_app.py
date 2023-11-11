from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Variável global para armazenar o nível de ruído
current_noise_level = 0.0

@app.route('/')
def index():
    return render_template('index.html')

# Adicionamos uma rota /status para receber o status do ruído
@app.route('/status', methods=['POST'])
def update_status():
    global current_noise_level  # Avisamos ao Python que estamos usando a variável global
    noise_status = request.form.get('noiseStatus', 'Aguardando medição...')
    print(f"Novo status do ruído: {noise_status}")
    return 'OK'

# Adicionamos uma rota /get_noise_level para fornecer o nível de ruído atual

@app.route('/get_noise_level')
def get_noise_level():
    global current_noise_level  # Avisamos ao Python que estamos usando a variável global
    print(current_noise_level)
    return jsonify({'noiseLevel': current_noise_level})

# Adicionamos uma rota /update_noise_level para receber atualizações do nível de ruído
@app.route('/update_noise_level', methods=['POST'])
def update_noise_level():
    global current_noise_level  # Avisamos ao Python que estamos usando a variável global
    data = request.get_json()
    current_noise_level = data['noiseLevel']
    print(current_noise_level)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)
