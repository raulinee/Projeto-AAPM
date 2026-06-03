from app.database import Session
from app.models.produto import Produto

PRODUTOS = [
    {"nome": "Semestralidade AAPM", "preco": 100.00},
    {"nome": "Armário + Semestralidade", "preco": 130.00},
    {"nome": "2ª via de crachá", "preco": 15.00},
    {"nome": "Abridor de casa", "preco": 4.00},
    {"nome": "Agulha de máquina Nº11 - pacote c/10un", "preco": 8.00},
    {"nome": "Afinete c/ cabeça colorida", "preco": 2.00},
    {"nome": "Alfinete simples", "preco": 5.00},
    {"nome": "Alicate de Pic", "preco": 30.00},
    {"nome": "Almofada Alfineteira Tomate", "preco": 6.00},
    {"nome": "Apontador", "preco": 3.00},
    {"nome": "Avental", "preco": 58.00},
    {"nome": "Bobina", "preco": 1.00},
    {"nome": "Bolinha de Pebolim (un)", "preco": 5.00},
    {"nome": "Bolinha de Ping Pong (un)", "preco": 2.50},
    {"nome": "Bolinha de Ping Pong (pacote com 4un)", "preco": 9.00},
    {"nome": "Bolsa SENAI", "preco": 36.50},
    {"nome": "Borracha Artística", "preco": 9.00},
    {"nome": "Borracha branca", "preco": 2.00},
    {"nome": "Borracha Caneta", "preco": 11.00},
    {"nome": "Caixa de bobina", "preco": 8.00},
    {"nome": "Calculadora", "preco": 14.00},
    {"nome": "Camiseta malha Branca", "preco": 35.00},
    {"nome": "Camiseta malha Preta", "preco": 35.00},
    {"nome": "Camiseta POLO de malha preta", "preco": 55.00},
    {"nome": "Caneta Bic", "preco": 1.30},
    {"nome": "Caneta Mágica fantasminha colorida", "preco": 8.00},
    {"nome": "Caneta Marca Texto", "preco": 5.00},
    {"nome": "Caneta para desenho Faber Castell 0.4", "preco": 6.00},
    {"nome": "Canetinha colorida c/ 12 cores", "preco": 8.50},
    {"nome": "Carregador de Celular V8 USB", "preco": 14.00},
    {"nome": "Cabo USB tipo C", "preco": 10.00},
    {"nome": "Carretilha cabo de madeira", "preco": 5.00},
    {"nome": "Clips Nr 3/0", "preco": 5.00},
    {"nome": "Cola bastão 10g", "preco": 4.00},
    {"nome": "Corretivo (Fita Corretiva)", "preco": 5.00},
    {"nome": "Cola Líquida", "preco": 4.50},
    {"nome": "Compasso", "preco": 13.00},
    {"nome": "CÓPIA (Preto e branco) unitário", "preco": 2.00},
    {"nome": "Cordão para crachá SENAI", "preco": 4.00},
    {"nome": "Curva Francesa grande 1119", "preco": 19.00},
    {"nome": "Curva Francesa pequena 1105", "preco": 15.00},
    {"nome": "Esfuminho", "preco": 3.00},
    {"nome": "Esquadro", "preco": 4.00},
    {"nome": "Estojo Organizador M", "preco": 17.00},
    {"nome": "Fita Crepe - rolo 18mm x 10m", "preco": 2.00},
    {"nome": "Fita Crepe - rolo 18mm x 50m", "preco": 8.00},
    {"nome": "Fita Métrica", "preco": 3.00},
    {"nome": "Fone de Ouvido", "preco": 8.00},
    {"nome": "Furador", "preco": 5.00},
    {"nome": "Giz lápis marcar tecido cores", "preco": 4.00},
    {"nome": "Grafite Faber Castell e HB", "preco": 5.00},
    {"nome": "Grafite Leo&Leo 0,5 07 e 09mm", "preco": 3.00},
    {"nome": "Grampeador pequeno", "preco": 9.00},
    {"nome": "Grampo para grampeador cx. c/100un", "preco": 2.00},
    {"nome": "Guia Magnético G20", "preco": 4.00},
    {"nome": "Lápis HB nº2 e nº4", "preco": 1.50},
    {"nome": "Lapiseira 0,7mm", "preco": 5.00},
    {"nome": "Lapiseira 0,9mm", "preco": 5.00},
    {"nome": "Lapiseira 2,0mm", "preco": 5.00},
    {"nome": "Lente Conta Fio", "preco": 35.00},
    {"nome": "Óculos de sobrepor 3M", "preco": 28.00},
    {"nome": "Óculos simples 3M", "preco": 15.00},
    {"nome": "Papel Canson", "preco": 12.00},
    {"nome": "Papel Kraft - rolo 10 metros", "preco": 16.00},
    {"nome": "Papel Kraft Folha unitária", "preco": 2.00},
    {"nome": "Papel Sulfite c/100f", "preco": 8.50},
    {"nome": "Passador de linha grande", "preco": 3.00},
    {"nome": "Passador de linha pequeno", "preco": 1.00},
    {"nome": "Pasta com aba e elástico", "preco": 4.00},
    {"nome": "Percevejos", "preco": 5.00},
    {"nome": "Pinça Costura", "preco": 5.00},
    {"nome": "Porta crachá", "preco": 4.00},
    {"nome": "Protetor auricular", "preco": 7.00},
    {"nome": "Régua 15cm", "preco": 3.00},
    {"nome": "Régua 3 em 1", "preco": 65.00},
    {"nome": "Régua 30cm", "preco": 3.00},
    {"nome": "Régua Curvas", "preco": 4.00},
    {"nome": "Régua mm 30cm", "preco": 17.00},
    {"nome": "Régua mm 60cm", "preco": 28.00},
    {"nome": "Tesoura", "preco": 18.00},
    {"nome": "Tesoura Arremate", "preco": 4.00},
    {"nome": "Tesoura de Picotar Profissional", "preco": 39.00},
    {"nome": "Tesoura Picotar escolar", "preco": 12.00},
    {"nome": "Touca protetora (5 un)", "preco": 5.00},
    {"nome": "Vazador 2mm", "preco": 14.00},
]


def seed_produtos():
    db = Session()
    try:
        for item in PRODUTOS:
            existente = db.query(Produto).filter_by(nome=item["nome"]).first()
            if existente:
                print(f"Produto já existe: {item['nome']}")
                continue

            produto = Produto(
                nome=item["nome"],
                preco=item["preco"],
                estoque_atual=10,
                ativo=True,
                imagem_path=None,
                categoria_id=None,
            )
            db.add(produto)

        db.commit()
        print("Inserção de produtos finalizada com sucesso.")
    except Exception as erro:
        db.rollback()
        print(f"Erro ao popular produtos: {erro}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_produtos()
