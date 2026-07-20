import streamlit as st
import time
import pandas as pd

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE
st.set_page_config(
    page_title="NEXUS | Social & Flash Commerce",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ENGENHARIA DE DESIGN E INTERFACE FLUIDA (CSS Customizado)
st.markdown("""
    <style>
    .main { background-color: #0b0b0f; color: #ffffff; }
    
    [data-testid="stHeader"] { z-index: 999; }
    
    /* HEADER FIXO - ESTILO MERCADO LIVRE / TIKTOK */
    .header-fixo {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        background-color: #0b0b0f;
        border-bottom: 1px solid #1f1f2e;
        z-index: 999999;
        padding-bottom: 10px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }
    
    .espacamento-conteudo { margin-top: 155px; }
    
    /* CARD DE VÍDEO / TIKTOK FEED */
    .tiktok-card {
        background-color: #12121a;
        border-radius: 20px;
        padding: 12px;
        border: 1px solid #1f1f2e;
        text-align: center;
        transition: all 0.3s ease;
    }
    .tiktok-card:hover {
        border-color: #ff0050; /* Cor característica TikTok */
        transform: translateY(-3px);
    }
    
    /* BOTÕES DE COMPRA PREMIUM E FLUIDOS */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff0050 0%, #00f2fe 100%);
        color: #ffffff;
        border-radius: 12px;
        border: none;
        padding: 10px 20px;
        font-weight: 800;
        font-size: 13px;
        width: 100%;
        transition: all 0.2s ease;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
    }
    
    /* BADGES DE OFERTA FLASH - ESTILO SHOPEE */
    .badge-shopee {
        background: #ff5722;
        color: white;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 10px;
        font-weight: 900;
        text-transform: uppercase;
        display: inline-block;
    }
    
    .progresso-estoque {
        background-color: #2a2a3a;
        border-radius: 10px;
        height: 6px;
        overflow: hidden;
        margin-top: 5px;
    }
    .progresso-barra {
        background: #ff5722;
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTROLE DE ESTADOS DO COMPRADOR
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []
if 'modalidade' not in st.session_state:
    st.session_state.modalidade = "🛍️ Varejo"

# 4. CABEÇALHO INTEGRADO FIXO NO TOPO
st.markdown("""
    <div class="header-fixo">
        <div style="background: linear-gradient(90deg, #ff5722 0%, #ff0050 100%); color: white; text-align: center; padding: 6px; font-size: 11px; font-weight: 700; letter-spacing: 0.5px;">
            🔥 NOVO FEED INTERATIVO: ASSISTA, COMPRE E GANHE MOEDAS BÔNUS!
        </div>
    </div>
""", unsafe_allow_html=True)

container_topo = st.container()
with container_topo:
    st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    col_logo, col_tipo, col_sacola = st.columns([4, 3, 3])
    
    with col_logo:
        st.markdown("<h2 style='margin:0; font-weight:900; letter-spacing:-1.5px; color:#fff; font-size:26px;'>NEXUS <span style='font-size:10px; font-weight:800; background: linear-gradient(90deg, #ff0050, #00f2fe); color:#fff; padding:2px 6px; border-radius:4px; margin-left:2px;'>LIVE</span></h2>", unsafe_allow_html=True)
        
    with col_tipo:
        # Alternância entre Atacado e Varejo direto no Header (Estilo B2B Ágil)
        tipo_compra = st.selectbox("Canal:", ["🛍️ Varejo", "📦 Atacado (-35%)"], label_visibility="collapsed")
        st.session_state.modalidade = tipo_compra
        
    with col_sacola:
        total_pecas = sum([item['quantidade'] for item in st.session_state.carrinho])
        st.markdown(f"<div style='text-align:right; font-weight:800; font-size:15px; margin-top:5px;'>🛒 Sacola ({total_pecas})</div>", unsafe_allow_html=True)
        
    st.markdown("<div style='margin-top: 3px;'></div>", unsafe_allow_html=True)
    busca_query = st.text_input("Busca", placeholder="🔎 Buscar tendências do TikTok, roupas ou lojas oficiais...", label_visibility="collapsed")

# 5. AJUSTE DE ESPAÇAMENTO DO CONTEÚDO ROLÁVEL
st.markdown('<div class="espacamento-conteudo"></div>', unsafe_allow_html=True)

# 6. BANCO DE DADOS HÍBRIDO (Preço Varejo vs Preço Atacado Comercial)
catalogo_produtos = [
    {
        "id": 201, "nome": "Calça Denim Premium Slim", "varejo": 119.90, "atacado": 79.90, "estoque_pct": 75,
        "video_placeholder": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600&auto=format&fit=crop&q=80",
        "criador": "@lookjeans_oficial", "tags": "Jeans Premium • Caimento Perfeito"
    },
    {
        "id": 202, "nome": "Jaqueta Jeans Destroyed", "varejo": 169.90, "atacado": 115.00, "estoque_pct": 92,
        "video_placeholder": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80",
        "criador": "@styledenim", "tags": "Tendência Inverno • Streetwear"
    },
    {
        "id": 203, "nome": "Camiseta Algodão Egípcio", "varejo": 69.90, "atacado": 45.00, "estoque_pct": 30,
        "video_placeholder": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600&auto=format&fit=crop&q=80",
        "criador": "@basicos_nexus", "tags": "Algodão Premium • Fibras Longas"
    },
    {
        "id": 204, "nome": "Shorts Denim Hot Pants", "varejo": 89.90, "atacado": 59.90, "estoque_pct": 45,
        "video_placeholder": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=600&auto=format&fit=crop&q=80",
        "criador": "@modaverao_br", "tags": "Lançamento • Conforto Todo Dia"
    }
]

# 7. FILTRAGEM DINÂMICA
produtos_filtrados = [p for p in catalogo_produtos if busca_query.lower() in p["nome"].lower()] if busca_query else catalogo_produtos

# 8. MÓDULO 1: OFERTAS RELÂMPAGO DO DIA (Estilo Shopee)
st.markdown("### ⚡ Ofertas Relâmpago Exclusivas")
col_cronometro, col_espaco = st.columns([3, 7])
with col_cronometro:
    st.markdown("<p style='color:#ff5722; font-weight:bold; font-size:14px; margin:0;'>⏰ Termina em: <span style='background:#1f1f2e; padding:3px 6px; border-radius:4px;'>01</span> : <span style='background:#1f1f2e; padding:3px 6px; border-radius:4px;'>42</span> : <span style='background:#1f1f2e; padding:3px 6px; border-radius:4px;'>19</span></p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 9. MÓDULO 2: FEED DE VÍDEOS DE PRODUTOS / LOOKS (Estilo TikTok Reels)
st.markdown("### 🎬 Feed Trends — Assista e Adicione em 1-Clique")

colunas_feed = st.columns(4)
for idx, prod in enumerate(produtos_filtrados):
    coluna_atual = colunas_feed[idx % 4]
    preco_exibido = prod["atacado"] if "Atacado" in st.session_state.modalidade else prod["varejo"]
    
    with coluna_atual:
        # Iniciando o Card de Visual TikTok
        st.markdown(f"<div class='tiktok-card'>", unsafe_allow_html=True)
        
        # Elemento Visual Central Simulando o Vídeo/Demonstração
        st.image(prod["video_placeholder"], use_container_width=True)
        
        # Metadados do TikTok Social Commerce
        st.markdown(f"<p style='color:#00f2fe; font-size:12px; font-weight:700; text-align:left; margin:5px 0 2px 0;'>🎥 {prod['criador']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#a0a0b0; font-size:11px; text-align:left; margin:0 0 8px 0;'>{prod['tags']}</p>", unsafe_allow_html=True)
        
        # Informações de Preço e Selo Shopee
        st.markdown(f"<div style='text-align:left; margin-bottom:5px;'><span class='badge-shopee'>🔥 FLASH DEALS</span></div>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#fff; font-weight:800; text-align:left; margin:0;'>R$ {preco_exibido:.2f}</h4>", unsafe_allow_html=True)
        
        # Barra de Estoque Dinâmica Shopee
        st.markdown(f"""
            <div style='text-align:left; font-size:10px; color:#ff5722; font-weight:bold; margin-top:5px;'>{prod['estoque_pct']}% Vendido</div>
            <div class='progresso-estoque'><div class='progresso-barra' style='width: {prod['estoque_pct']}%;'></div></div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Seleção Prática de Grades
        c_cor = st.selectbox("Cor:", ["Padrão"] + [c for c in ["Claro", "Escuro"] if "Jeans" in prod["nome"]], key=f"feed_cor_{prod['id']}", label_visibility="collapsed")
        c_tam = st.select_slider("Tam:", options=["P", "M", "G", "GG"] if "Jaqueta" in prod["nome"] or "Camiseta" in prod["nome"] else ["38", "40", "42", "44"], key=f"feed_tam_{prod['id']}")
        
        # Ação Direta de Compra Instantânea
        if st.button("⚡ COMPRA RÁPIDA", key=f"btn_tk_{prod['id']}"):
            st.session_state.carrinho.append({
                "nome": prod["nome"],
                "preco": preco_exibido,
                "cor": c_cor,
                "tamanho": c_tam,
                "quantidade": 1
            })
            st.toast("🛒 Adicionado à sua sacola de compras!")
            time.sleep(0.3)
            st.rerun()
            
        st.markdown("</div>", unsafe_allow_html=True)

# 10. INTERFACE DE CHECKOUT SIMPLIFICADA (Estilo Mercado Livre de Confiança)
if len(st.session_state.carrinho) > 0:
    st.markdown("<br><hr style='border-top:1px solid #1f1f2e;'/><br>", unsafe_allow_html=True)
    st.markdown("### 📦 Sacola de Compras Protegida")
    
    col_carrinho_lista, col_carrinho_resumo = st.columns([6, 4])
    
    with col_carrinho_lista:
        for idx_cart, item in enumerate(st.session_state.carrinho):
            c1, c2, c3, c4 = st.columns([4, 3, 2, 1])
            with c1:
                st.markdown(f"**{item['nome']}**")
            with c2:
                st.markdown(f"✨ `{item['cor']}` / T: `{item['tamanho']}`")
            with c3:
                st.markdown(f"R$ {item['preco']:.2f}")
            with c4:
                if st.button("🗑️", key=f"del_feed_{idx_cart}"):
                    st.session_state.carrinho.pop(idx_cart)
                    st.rerun()
            st.markdown("<hr style='border-top: 1px dotted #2a2a3a; margin:5px 0;'/>", unsafe_allow_html=True)
            
    with col_carrinho_resumo:
        subtotal_pedido = sum([i['preco'] * i['quantidade'] for i in st.session_state.carrinho])
        
        st.markdown("<div style='background-color:#12121a; padding:15px; border-radius:15px; border:1px solid #1f1f2e;'>", unsafe_allow_html=True)
        st.markdown(f"<h4>Resumo do Pedido ({st.session_state.modalidade})</h4>", unsafe_allow_html=True)
        st.write(f"Produtos Selecionados: R$ {subtotal_pedido:.2f}")
        st.markdown("<p style='color:#00f2fe; font-size:12px;'>✓ Compra Garantida Nexus: Seu dinheiro está seguro</p>", unsafe_allow_html=True)
        st.markdown(f"### Total: R$ {subtotal_pedido:.2f}")
        
        if st.button("💳 CONCLUIR E PAGAR"):
            with st.spinner("Conectando ao banco central de pagamentos..."):
                time.sleep(1.5)
            st.balloons()
            st.success("🎉 Compra aprovada! Preparando separação de estoque no hub logístico.")
            st.session_state.carrinho = []
            time.sleep(1.5)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
