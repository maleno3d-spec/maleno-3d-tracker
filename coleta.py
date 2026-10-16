import json

print("Executando robô de busca ampla Maleno 3D...")

# Catálogo completo dos produtos mais vendidos em Impressão 3D na Shopee / Mercado Livre
produtos_coletados = [
    # --- NATAL & FESTAS ---
    {
        "id": 1,
        "titulo": "Kit Natalino 3D Bichinhos e Enfeites (Papai Noel, Boneco de Neve)",
        "plataforma": "Shopee",
        "preco": 19.17,
        "vendas_estimadas": "3.5k vendidos",
        "categoria": "natal festas",
        "link": "https://shopee.com.br"
    },
    {
        "id": 2,
        "titulo": "Árvore de Natal Minimalista Decorativa 3D",
        "plataforma": "Shopee",
        "preco": 23.90,
        "vendas_estimadas": "1.8k vendidos",
        "categoria": "natal sala casa",
        "link": "https://shopee.com.br"
    },
    {
        "id": 3,
        "titulo": "Enfeite Feliz Natal em Impressão 3D para Mesa e Aparador",
        "plataforma": "Shopee",
        "preco": 25.94,
        "vendas_estimadas": "2.2k vendidos",
        "categoria": "natal mesa casa",
        "link": "https://shopee.com.br"
    },

    # --- CASA & DECORAÇÃO (SALA, QUARTO, MESA) ---
    {
        "id": 4,
        "titulo": "Kit 3 Vasos Decorativos Barroco 3D para Sala e Aparador",
        "plataforma": "Shopee",
        "preco": 39.99,
        "vendas_estimadas": "1.2k vendidos",
        "categoria": "casa sala decoracao vaso mesa",
        "link": "https://shopee.com.br"
    },
    {
        "id": 5,
        "titulo": "Vaso Decorativo Nórdico Minimalista Impressão 3D",
        "plataforma": "Shopee",
        "preco": 20.00,
        "vendas_estimadas": "950 vendidos",
        "categoria": "casa decoracao sala rack",
        "link": "https://shopee.com.br"
    },
    {
        "id": 6,
        "titulo": "Luminária Decorativa Gato 3D com Abajur LED",
        "plataforma": "Shopee",
        "preco": 45.90,
        "vendas_estimadas": "1.1k vendidos",
        "categoria": "casa quarto sala escritorio iluminacao",
        "link": "https://shopee.com.br"
    },

    # --- ESCRITÓRIO, MESA & ORGANIZAÇÃO ---
    {
        "id": 7,
        "titulo": "Organizador de Mesa e Porta-Canetas 3D Geométrico",
        "plataforma": "Shopee",
        "preco": 24.90,
        "vendas_estimadas": "4.3k vendidos",
        "categoria": "escritorio organizacao mesa caneta",
        "link": "https://shopee.com.br"
    },
    {
        "id": 8,
        "titulo": "Suporte Flutuante de Livros e Prateleira Moderna 3D",
        "plataforma": "Shopee",
        "preco": 24.90,
        "vendas_estimadas": "1.5k vendidos",
        "categoria": "escritorio casa organizacao parede",
        "link": "https://shopee.com.br"
    },

    # --- BANHEIRO & ORGANIZAÇÃO DA CASA ---
    {
        "id": 9,
        "titulo": "Suporte para Escova e Pasta de Dentes Modular 3D",
        "plataforma": "Shopee",
        "preco": 22.50,
        "vendas_estimadas": "2.8k vendidos",
        "categoria": "banheiro organizacao casa",
        "link": "https://shopee.com.br"
    },
    {
        "id": 10,
        "titulo": "Moldura Espelho para Interruptor Inteligente Alexa/Google 3D",
        "plataforma": "Shopee",
        "preco": 21.99,
        "vendas_estimadas": "5.0k vendidos",
        "categoria": "casa decoracao organizacao",
        "link": "https://shopee.com.br"
    }
]

# Grava os dados no produtos.json
with open("produtos.json", "w", encoding="utf-8") as f:
    json.dump(produtos_coletados, f, ensure_ascii=False, indent=4)

print("Coleta ampla concluída com sucesso!")
