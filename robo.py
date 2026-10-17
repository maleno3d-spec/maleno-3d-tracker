import json
import requests

print("🤖 Iniciando o robô da Maleno 3D para buscar produtos reais...")

# Termos de busca focados em Impressão 3D para o seu nicho
termos_busca = [
    "decoracao impressao 3d",
    "vaso decorativo 3d",
    "organizador de mesa 3d",
]

produtos_coletados = []
id_global = 1

for termo in termos_busca:
  # URL da API pública de busca do Mercado Livre
  url = f"https://api.mercadolibre.com/sites/MLB/search?q={termo}&limit=4"

  try:
    print(f"Pesquisando no Mercado Livre por: '{termo}'...")
    resposta = requests.get(url)

    if resposta.status_code == 200:
      dados = resposta.json()
      resultados = dados.get("results", [])

      for item in resultados:
        # Extraindo informações reais da API
        titulo = item.get("title")
        preco = item.get("price")
        link = item.get("permalink")
        # Troca a miniatura por uma imagem de melhor qualidade
        imagem = item.get("thumbnail", "").replace("-I.jpg", "-O.jpg")
        vendidos = item.get("sold_quantity", 0)

        # Formatando texto de vendas
        vendas_texto = f"{vendidos} vendidos" if vendidos > 0 else "Alta demanda"

        produtos_coletados.append({
            "id": id_global,
            "titulo": titulo,
            "plataforma": "Mercado Livre",
            "preco": float(preco),
            "vendas_estimadas": vendas_texto,
            "categoria": termo,
            "imagem": imagem,
            "link": link,
        })
        id_global += 1
    else:
      print(f"⚠️ Erro ao buscar o termo {termo}: Status {resposta.status_code}")

  except Exception as e:
    print(f"❌ Erro de conexão ao buscar '{termo}': {e}")

# Salva os dados fresquinhos no produtos.json
with open("produtos.json", "w", encoding="utf-8") as f:
  json.dump(produtos_coletados, f, ensure_ascii=False, indent=4)

print(
    f"🎉 Sucesso! {len(produtos_coletados)} produtos reais foram coletados e"
    " salvos em 'produtos.json'."
)
