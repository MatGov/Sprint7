from flask import Flask, jsonify

app = Flask(__name__)

AVALIACOES = [
    {"produto_id": 1, "usuario": "Maria", "nota": 5, "comentario": "Fantástico, vale a pena!"},
    {"produto_id": 2, "usuario": "João", "nota": 4, "comentario": "Um bom vinho para o dia a dia."}
]

@app.route('/avaliacoes/<int:produto_id>', methods=['GET'])
def buscar_avaliacoes(produto_id):
    print(f"Requisição recebida para avaliações do produto {produto_id}")
    # Filtra as avaliações para o produto específico
    resultado = [a for a in AVALIACOES if a['produto_id'] == produto_id]
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8082)