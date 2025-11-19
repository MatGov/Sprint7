from flask import Flask, jsonify

app = Flask(__name__)

VINHOS = [
    {"id": 1, "nome": "Agnello Reserva Especial", "safra": 2018, "preco": 150.00},
    {"id": 2, "nome": "Agnello Tinto Clássico", "safra": 2020, "preco": 85.00}
]

@app.route('/vinhos', methods=['GET'])
def listar_vinhos():
    print("Requisição recebida para listar vinhos.")
    return jsonify(VINHOS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)