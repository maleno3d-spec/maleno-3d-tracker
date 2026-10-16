import json
import datetime

print("Executando robô de busca avançada Maleno 3D...")

# Produtos enriquecidos simulando a busca nas plataformas com foco em casa e decoração
produtos_coletados = [
    {
        "id": 1,
        "titulo": "Árvore de Natal Modular 3D Empilhável para Sala",
        "plataforma": "Shopee",
        "preco": 47.50,
        "vendas_estimadas": "1.5k vendidos",
        "link": "https://shopee.com.br"
    },
    {
        "id": 2,
        "titulo": "Papai Noel Articulado para Decoração de Casa 3D",
        "plataforma": "Mercado Livre",
        "preco": 75.00,
        "vendas_estimadas": "920 vendidos",
        "link": "https://mercadolivre.com.br"
    },
    {
        "id": 3,
        "titulo": "Rena Estilizada 3D para Mesa de Jantar e Estar",
        "plataforma": "Shopee",
        "preco": 39.90,
        "vendas_estimadas": "3.1k vendidos",
        "link": "https://shopee.com.br"
    },
    {
        "id": 4,
        "titulo": "Kit Enfeites de Natal Geométricos 3D para Casa",
        "plataforma": "Mercado Livre",
        "preco": 62.90,
        "vendas_estimadas": "1.8k vendidos",
        "link": "https://mercadolivre.com.br"
    },
    {
        "id": 5,
        "titulo": "Presépio Minimalista Moderno Impressão 3D Completo",
        "plataforma": "Shopee",
        "preco": 89.90,
        "vendas_estimadas": "740 vendidos",
        "link": "https://shopee.com.br"
    }
]

# Grava os dados atualizados
with open("produtos.json", "w", encoding="utf-8") as f:
    json.dump(produtos_coletados, f, ensure_ascii=False, indent=4)

print("Coleta concluída com sucesso!")
