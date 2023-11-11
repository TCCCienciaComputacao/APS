from flask import Flask, render_template, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def status():
    return render_template('status.html')

# Adicionamos uma rota /get_status para obter o status real do ruído do servidor principal
@app.route('/get_status')
def get_status():
    try:
        response = requests.get('http://localhost:5000/get_noise_level')
        if response.status_code == 200:
            noise_level = response.json().get('noiseLevel')
            print(noise_level)
            status = get_status_text(noise_level)
            print(status)

        else:
            status = 'Erro ao obter status'
    except Exception as e:
        print(f"Erro na solicitação para obter status: {e}")
        status = 'Erro na solicitação'

    return jsonify({'status': status})

def get_status_text(noise_level):
    if noise_level > 5:
        return 'Muito Barulho'
    elif noise_level > 2:
        return 'Barulho'
    elif noise_level > 1:
        return 'Adequado'
    elif noise_level > 0.5:
        return 'Baixo'
    else:
        return 'Sem Ruído'

if __name__ == '__main__':
    app.run(host='IPLOCAL', port=8080, debug=True)
