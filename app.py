import streamlit as st
import time

# Configuração da página para o modo Wide (aproveita melhor a tela) e título moderno
st.set_page_config(
    page_title="NEXUS | Plataforma de Moda Premium",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Customização sutil via CSS para deixar o visual mais clean (Estilo Zara/Dafiti)
st.markdown("""
    <style>
    .main {background-color: #fcfcfc;}
    div.stButton > button:first-child {
        background-color: #000000;
        color: #ffffff;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
        font-weight: bold;
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background-color: #222222;
        color: #ffffff;
    }
    .badge-desconto {
        background-color: #ff4b4b;
        color: white;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. BARRA DE AVISOS SUPERIOR (Inspiração: Shopee/Shein)
st.markdown(
    '<div style="background-color: black; color: white; text-align: center; padding: 6px; font-size: 13px; font-weight: 500;">'
    '⚡ FRETE GRÁTIS a partir de R$ 199 + 10% OFF com o cupom <span style="color: #facc15; font-weight: bold;">PRIMEIRO10</span>'
    '</div>', 
    unsafe_allow_html=True
)

# 2. CABEÇALHO PRINCIPAL
col_logo, col_busca, col_carrinho = st.columns([2, 5, 2])
with col_logo:
    st.markdown("<h2 style='margin-top: 10px; font-weight: 900; letter-spacing: -1px;'>NEXUS <span style='font-size: 12px; background: black; color: white; padding: 2px 6px; border-radius: 4px;'>B2B & VAREJO</span></h2>", unsafe_allow_html=True)

with col_busca:
    busca = st.text_input("", placeholder="Buscar por jeans, camisetas, lançamentos...", label_visibility="collapsed")

# Inicializar carrinho no estado da sessão do Streamlit
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

with col_carrinho:
    qtd_itens = len(st.session_state.carrinho)
    st.markdown(f"<p style='text-align: right; margin-top: 15px; font-weight: bold;'>🛒 Sacola ({qtd_itens})</p>", unsafe_allow_html=True)

st.divider()

# 3. PRODUTOS COMPLETO (Base de dados simulada para Moda)
produtos = [
    {
        "id": 1, "nome": "Calça Denim Premium Slim Fit", "preco": 119.90, "preco_antigo": 199.90, "categoria": "Jeans",
        "img": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500&auto=format&fit=crop&q=60", "tag": "-40% OFF"
    },
    {
        "id": 2, "nome": "Jaqueta Jeans Heavy Destroyed", "preco": 169.90, "preco_antigo": 239.90, "categoria": "Jeans",
        "img": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=500&auto=format&fit=crop&q=60", "tag": "Mais Vendido"
    },
    {
        "id": 3, "nome": "Camiseta Algodão Egípcio Minimalista", "preco": 69.90, "preco_antigo": 99.90, "categoria": "Básicos",
        "img": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=500&auto=format&fit=crop&q=60", "tag": "100% Algodão"
    },
    {
        "id": 4, "nome": "Shorts Jeans Hot Pants Comfort", "preco": 89.90, "preco_antigo": 129.90, "categoria": "Jeans",
        "img": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=500&auto=format&fit=crop&q=60", "tag": "Lançamento"
    }
]

# 4. SIDEBAR - FILTROS INTELIGENTES (Estilo Mercado Livre)
st.sidebar.title("Filtros Avançados")
categoria_selecionada = st.sidebar.multiselect("Categorias", ["Todos", "Jeans", "Básicos"], default="Todos")
preco_max = st.sidebar.slider("Preço Máximo (R$)", 50, 300, 300)

# Filtragem lógica dos produtos
produtos_filtrados = []
for p in produtos:
    # Filtro de texto de busca
    if busca and busca.lower() not in p["nome"].lower():
        continue
    # Filtro de categoria
    if "Todos" not in categoria_selecionada and p["categoria"] not in categoria_selecionada:
        continue
    # Filtro de preço
    if p["preco"] > preco_max:
        continue
    produtos_filtrados.append(p)

# 5. BANNER PRINCIPAL DE CAMPANHA (Dafiti/Zara style)
st.image("https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=1200&auto=format&fit=crop&q=80", 
         caption="Coleção Streetwear Premium 2026 - Conforto e Caimento Sob Medida", use_container_width=True)

# 6. VITRINE DE PRODUTOS EM GRID (Responsivo)
st.subheader("⚡ Ofertas Relâmpago do Dia")

if not produtos_filtrados:
    st.warning("Nenhum produto encontrado com os filtros selecionados.")
else:
    # Divide a tela em 4 colunas para os produtos
    colunas = st.columns(4)
    
    for idx, prod in enumerate(produtos_filtrados):
        col_atual = colunas[idx % 4]
        with col_atual:
            st.image(prod["img"], use_container_width=True)
            st.markdown(f"<span class='badge-desconto'>{prod['tag']}</span>", unsafe_allow_html=True)
            st.markdown(f"**{prod['nome']}**")
            st.markdown(f"<span style='color: gray; text-decoration: line-through; font-size: 12px;'>R$ {prod['preco_antigo']:.2f}</span>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='margin-top:0px; color:black;'>R$ {prod['preco']:.2f}</h4>", unsafe_allow_html=True)
            
            # Botão interativo de compra rápida
            if st.button("Adicionar à Sacola", key=f"btn_{prod['id']}"):
                st.session_state.carrinho.append(prod)
                st.toast(f"✅ {prod['nome']} adicionado à sacola!")
                time.sleep(0.5)
                st.rerun()

# 7. RESUMO DA SACOLA / MINI CHECKOUT INTERATIVO (Rodapé lateral ou inferior)
if len(st.session_state.carrinho) > 0:
    st.divider()
    st.subheader("🛒 Finalizar Compra Rápida")
    c1, c2 = st.columns([2, 1])
    with c1:
        total = sum([item['preco'] for item in st.session_state.carrinho])
        st.write("### Itens na Sacola:")
        for item in st.session_state.carrinho:
            st.write(f"- {item['nome']} (R$ {item['preco']:.2f})")
    with c2:
        st.write(f"### Total: **R$ {total:.2f}**")
        if st.button("💳 Fechar Pedido via PIX / Cartão"):
            with st.spinner("Processando pedido na API segura..."):
                time.sleep(1.5)
            st.success("🎉 Pedido Gerado com Sucesso! Integrando com o centro logístico.")
            st.session_state.carrinho = []
            time.sleep(1)
            st.rerun()