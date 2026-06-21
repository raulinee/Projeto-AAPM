"""
Script para criar categorias e associar todos os produtos de uma vez.
Rode com: python popular_categorias.py
"""

from app.database import Session
from app.models.categoria import Categoria
from app.models.produto import Produto

# ── Mapeamento: Categoria → lista de nomes de produtos ──────────────────────
CATEGORIAS_PRODUTOS = {
    "Serviços e Taxas": [
        "Semestralidade AAPM",
        "Armário + Semestralidade",
        "2ª via de crachá",
        "CÓPIA (Preto e branco) unitário",
    ],

    "Material Escolar": [
        "Caneta Bic",
        "Caneta Marca Texto",
        "Caneta Mágica fantasminha colorida",
        "Canetinha colorida c/ 12 cores",
        "Lápis HB nº2 e nº4",
        "Lapiseira 0,7mm",
        "Lapiseira 0,9mm",
        "Lapiseira 2,0mm",
        "Grafite Faber Castell e HB",
        "Grafite Leo&Leo 0,5 07 e 09mm",
        "Borracha branca",
        "Borracha Artística",
        "Borracha Caneta",
        "Apontador",
        "Cola bastão 10g",
        "Cola Líquida",
        "Corretivo (Fita Corretiva)",
        "Compasso",
        "Grampeador pequeno",
        "Grampo para grampeador cx. c/100un",
        "Clips Nr 3/0",
        "Percevejos",
        "Furador",
        "Calculadora",
        "Tesoura",
    ],

    "Costura e Têxtil": [
        "Agulha de máquina Nº11 - pacote c/10un",
        "Abridor de casa",
        "Afinete c/ cabeça colorida",
        "Alfinete simples",
        "Alicate de Pic",
        "Almofada Alfineteira Tomate",
        "Avental",
        "Bobina",
        "Caixa de bobina",
        "Carretilha cabo de madeira",
        "Fita Métrica",
        "Giz lápis marcar tecido cores",
        "Guia Magnético G20",
        "Lente Conta Fio",
        "Passador de linha grande",
        "Passador de linha pequeno",
        "Pinça Costura",
        "Tesoura Arremate",
        "Tesoura de Picotar Profissional",
        "Tesoura Picotar escolar",
        "Vazador 2mm",
    ],

    "Desenho Técnico": [
        "Caneta para desenho Faber Castell 0.4",
        "Curva Francesa grande 1119",
        "Curva Francesa pequena 1105",
        "Esfuminho",
        "Esquadro",
        "Régua 15cm",
        "Régua 30cm",
        "Régua 3 em 1",
        "Régua Curvas",
        "Régua mm 30cm",
        "Régua mm 60cm",
    ],

    "Papelaria e Organização": [
        "Papel Sulfite c/100f",
        "Papel Canson",
        "Papel Kraft - rolo 10 metros",
        "Papel Kraft Folha unitária",
        "Fita Crepe - rolo 18mm x 10m",
        "Fita Crepe - rolo 18mm x 50m",
        "Pasta com aba e elástico",
        "Estojo Organizador M",
    ],

    "Vestuário e Identificação": [
        "Camiseta malha Branca",
        "Camiseta malha Preta",
        "Camiseta POLO de malha preta",
        "Bolsa SENAI",
        "Cordão para crachá SENAI",
        "Porta crachá",
    ],

    "Eletrônicos e EPI": [
        "Carregador de Celular V8 USB",
        "Cabo USB tipo C",
        "Fone de Ouvido",
        "Óculos de sobrepor 3M",
        "Óculos simples 3M",
        "Protetor auricular",
        "Touca protetora (5 un)",
    ],

    "Lazer e Recreação": [
        "Bolinha de Pebolim (un)",
        "Bolinha de Ping Pong (un)",
        "Bolinha de Ping Pong (pacote com 4un)",
    ],
}


def popular_categorias():
    db = Session()
    try:
        total_associados = 0
        total_categorias_criadas = 0

        for nome_categoria, produtos_lista in CATEGORIAS_PRODUTOS.items():
            # Buscar ou criar a categoria
            categoria = db.query(Categoria).filter_by(nome=nome_categoria).first()
            if not categoria:
                categoria = Categoria(nome=nome_categoria, ativo=True)
                db.add(categoria)
                db.flush()  # para gerar o ID
                total_categorias_criadas += 1
                print(f"✅ Categoria criada: {nome_categoria}")
            else:
                print(f"⏭️  Categoria já existe: {nome_categoria}")

            # Associar os produtos à categoria
            for nome_produto in produtos_lista:
                produto = db.query(Produto).filter_by(nome=nome_produto).first()
                if produto:
                    produto.categoria_id = categoria.id
                    total_associados += 1
                else:
                    print(f"   ⚠️  Produto não encontrado: {nome_produto}")

        db.commit()
        print(f"\n{'='*50}")
        print(f"🎉 Finalizado!")
        print(f"   Categorias criadas: {total_categorias_criadas}")
        print(f"   Produtos associados: {total_associados}")
        print(f"{'='*50}")

    except Exception as erro:
        db.rollback()
        print(f"❌ Erro: {erro}")
    finally:
        db.close()


if __name__ == "__main__":
    popular_categorias()
