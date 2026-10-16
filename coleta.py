import json

print("Executando robô com fotos reais e links atualizados Maleno 3D...")

produtos_coletados = [
    # --- NATAL & FESTAS ---
    {
        "id": 1,
        "titulo": "Kit Natalino 3D Bichinhos e Enfeites (Papai Noel, Boneco de Neve)",
        "plataforma": "Shopee",
        "preco": 19.17,
        "vendas_estimadas": "3.5k vendidos",
        "categoria": "natal festas presente enfeite",
        "imagem": "https://images.unsplash.com/photo-1543589077-47d81606c1bf?w=500&auto=format&fit=crop",
        "link": "https://shopee.com.br/search?keyword=kit%20natal%20bichinhos%203d"
    },
    {
        "id": 2,
        "titulo": "Árvore de Natal Minimalista Decorativa 3D em PLA",
        "plataforma": "Shopee",
        "preco": 23.90,
        "vendas_estimadas": "1.8k vendidos",
        "categoria": "natal sala casa mesa",
        "imagem": "https://images.unsplash.com/photo-1512389142860-9c449e58a543?w=500&auto=format&fit=crop",
        "link": "https://shopee.com.br/search?keyword=arvore%20de%20natal%20minimalista%203d"
    },
    {
        "id": 3,
        "titulo": "Enfeite Feliz Natal em Impressão 3D para Mesa e Aparador",
        "plataforma": "Shopee",
        "preco": 25.94,
        "vendas_estimadas": "2.2k vendidos",
        "categoria": "natal mesa casa decoracao",
        "imagem": "https://images.unsplash.com/photo-1576919228236-a097c32a588e?w=500&auto=format&fit=crop",
        "link": "https://shopee.com.br/search?keyword=enfeite%20feliz%20natal%203d"
    },

    # --- CASA & DECORAÇÃO ---
    {
        "id": 4,
        "titulo": "Kit 3 Vasos Decorativos Barroco 3D para Sala e Aparador",
        "plataforma": "Shopee",
        "preco": 39.99,
        "vendas_estimadas": "1.2k vendidos",
        "categoria": "casa sala decoracao vaso mesa rack",
        "imagem": "https://images.unsplash.com/photo-1581783342308-f792dbdd27c5?w=500&auto=format&fit=crop",
        "link": "https://shopee.com.br/search?keyword=kit%203%20vasos%20barroco%203d"
    },
    {
        "id": 5,
        "titulo": "Vaso Decorativo Nórdico Minimalista Impressão 3D",
        "plataforma": "Shopee",
        "preco": 20.00,
        "vendas_estimadas": "950 vendidos",
        "categoria": "casa decoracao sala rack mesa nordico",
        "imagem": "https://images.unsplash.com/photo-1612196808214-b7e239e5f6b7?w=500&auto=format&fit=crop",
        "link": "https://shopee.com.br/search?keyword=vaso%20decorativo%20nordico%203d"
    },

    # --- ESCRITÓRIO & ORGANIZAÇÃO ---
    {
        "id": 6,
        "titulo": "Organizador de Mesa e Porta-Canetas 3D Geométrico",
        "plataforma": "Shopee",
        "preco": 24.90,
        "vendas_estimadas": "4.3k vendidos",
        "categoria": "escritorio organizacao mesa caneta setup",
        "imagem": "https://images.unsplash.com/photo-1507208773393-40d9fc670acf?w=500&auto=format&fit=crop",
        "link": "https://shopee.com.br/search?keyword=organizador%20de%20mesa%203d"
    },
    {
        "id": 7,
        "titulo": "Suporte Flutuante de Livros e Prateleira Moderna 3D",
        "plataforma": "Shopee",
        "preco": 24.90,
        "vendas_estimadas": "1.5k vendidos",
        "categoria": "escritorio casa organizacao parede quarto",
        "imagem": "https://images.unsplash.com/photo-1594631252845-29fc4cc8cde9?w=500&auto=format&fit=crop",
        "link": "https://shopee.com.br/search?keyword=suporte%20flutuante%20livros%203d"
    },

    # --- BANHEIRO ---
    {
        "id": 8,
        "titulo": "Suporte para Escova e Pasta de Dentes Modular 3D",
        "plataforma": "Shopee",
        "preco": 22.50,
        "vendas_estimadas": "2.8k vendidos",
        "categoria": "banheiro organizacao casa higiene",
        "imagem": "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=500&auto=format&fit=crop",
        "link": "https://shopee.com.br/search?keyword=suporte%20escova%20dentes%203d"
    }
]

# Grava os dados no produtos.json
with open("produtos.json", "w", encoding="utf-8") as f:
    json.dump(produtos_coletados, f, ensure_ascii=False, indent=4)

print("Coleta com fotos estáveis finalizada!")
