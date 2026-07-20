import streamlit as st
import time

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
    
    /* CARD DE VÍDEO / TIKTOK FEED COM ALTO PADRÃO DE ALINHAMENTO */
    .tiktok-card {
        background-color: #12121a;
        border-radius: 20px;
        padding: 16px;
        border: 1px solid #1f1f2e;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        min-height: 540px; /* Altura mínima fixada para garantir o alinhamento em grid */
        transition: all 0.3s ease;
    }
    .tiktok-card:hover {
        border-color: #ff0050; 
        transform: translateY(-3px);
    }
    
    /* Limitador e padronizador da caixa de imagem */
    .container-imagem {
        width: 100%;
        height: 250px;
        overflow: hidden;
        border-radius: 12px;
        margin-bottom: 12px;
    }
    .container-imagem img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    /* BOTÕES DE COMPRA PREMIUM */
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
        margin-bottom: 10px;
    }
    .progresso-barra {
        background: #ff5722;
        height: 100%;
    }
    
    /* Forçar alinhamento de textos longos */
    .titulo-produto {
        font-size: 15px;
        font-weight: 700;
        color: #ffffff;
        margin: 5px 0;
        height: 44px; /* Fixa a altura do título para até 2 linhas */
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
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
        tipo_compra = st.selectbox("Canal:", ["🛍️ Varejo", "📦 Atacado (-35%)"], label_visibility="collapsed")
        st.session_state.modalidade = tipo_compra
        
    with col_sacola:
        total_pecas = sum([item['quantidade'] for item in st.session_state.carrinho])
        st.markdown(f"<div style='text-align:right; font-weight:800; font-size:15px; margin-top:5px;'>🛒 Sacola ({total_pecas})</div>", unsafe_allow_html=True)
        
    st.markdown("<div style='margin-top: 3px;'></div>", unsafe_allow_html=True)
    busca_query = st.text_input("Busca", placeholder="🔎 Buscar tendências do TikTok, roupas ou lojas oficiais...", label_visibility="collapsed")

# 5. AJUSTE DE ESPAÇAMENTO DO CONTEÚDO ROLÁVEL
st.markdown('<div class="espacamento-conteudo"></div>', unsafe_allow_html=True)

# 6. BANCO DE DADOS EXPANDIDO COM MAIS PRODUTOS (Preços Híbridos)
catalogo_produtos = [
    {
        "id": 201, "nome": "Calça Denim Premium Slim Fit Masculina", "varejo": 119.90, "atacado": 79.90, "estoque_pct": 75,
        "imagem": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600&auto=format&fit=crop&q=80",
        "criador": "@lookjeans_oficial", "tags": "Jeans Premium • Conforto"
    },
    {
        "id": 202, "nome": "Jaqueta Jeans Heavy Destroyed unissex", "varejo": 169.90, "atacado": 115.00, "estoque_pct": 92,
        "imagem": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80",
        "criador": "@styledenim", "tags": "Tendência Inverno • Streetwear"
    },
    {
        "id": 203, "nome": "Camiseta Algodão Egípcio Minimalista Fibras", "varejo": 69.90, "atacado": 45.00, "estoque_pct": 30,
        "imagem": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600&auto=format&fit=crop&q=80",
        "criador": "@basicos_nexus", "tags": "Algodão Premium • Fibras Longas"
    },
    {
        "id": 204, "nome": "Shorts Denim Hot Pants Comfort Feminino", "varejo": 89.90, "atacado": 59.90, "estoque_pct": 45,
        "imagem": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=600&auto=format&fit=crop&q=80",
        "criador": "@modaverao_br", "tags": "Lançamento • Conforto Todo Dia"
    },
    {
        "id": 205, "nome": "Calça Jogger Jeans Com Elástico Confort", "varejo": 139.90, "atacado": 89.90, "estoque_pct": 60,
        "imagem": "https://images.unsplash.com/photo-1554568218-0f1715e72254?w=600&auto=format&fit=crop&q=80",
        "criador": "@streetwear_nexus", "tags": "Estilo Urbano • Casual Denim"
    },
    {
        "id": 206, "nome": "Bermuda Cargo Jeans Heavy Duty Masculina", "varejo": 99.90, "atacado": 65.00, "estoque_pct": 82,
        "imagem": "https://images.unsplash.com/photo-1565049033148-18e3a241e7f3?w=600&auto=format&fit=crop&q=80",
        "criador": "@cia_do_jeans", "tags": "Utilitário Cargo • Alta Durabilidade"
    },
    {
        "id": 207, "nome": "Camisa Jeans Slim Fit Manga Longa Luxury", "varejo": 149.90, "atacado": 99.00, "estoque_pct": 20,
        "imagem": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?w=600&auto=format&fit=crop&q=80",
        "criador": "@premium_closet", "tags": "Linha Executiva • Denim Macio"
    },
    {
        "id": 208, "nome": "Top Cropped Jeans Estruturado Vintage", "varejo": 79.90, "atacado": 49.90, "estoque_pct": 52,
        "imagem": "https://images.unsplash.com/photo-1509319117193-57bab727e09d?w=600&auto=format&fit=crop&q=80",
        "criador": "@fashion_reels", "tags": "Corte Ajustado • Tendência Balada"
    }
]

# 7. FILTRAGEM DINÂMICA
produtos_filtrados = [p for p in catalogo_produtos if busca_query.lower() in p["nome"].lower()] if busca_query else catalogo_produtos

# 8. MÓDULO 1: OFERTAS RELÂMPAGO DO DIA (Estilo Shopee)
st.markdown("### ⚡ Ofertas Relâmpago Exclusivas")
st.markdown("<p style='color:#ff5722; font-weight:bold; font-size:14px; margin:0;'>⏰ Termina em: <span style='background:#1f1f2e; padding:3px 6px; border-radius:4px;'>01</span> : <span style='background:#1f1f2e; padding:3px 6px; border-radius:4px;'>42</span> : <span style='background:#1f1f2e; padding:3px 6px; border-radius:4px;'>19</span></p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 9. MÓDULO 2: FEED DE PRODUTOS TOTALMENTE ALINHADO (Estilo TikTok Reels / Mercado Livre)
st.markdown(f"### 🎬 Feed Trends — Exibindo Catálogo de Lançamentos ({st.session_state.modalidade})")

# Renderização do Grid Simétrico (4 Colunas fixas)
colunas_feed = st.columns(4)
for idx, prod in enumerate(produtos_filtrados):
    coluna_atual = colunas_feed[idx % 4]
    preco_exibido = prod["atacado"] if "Atacado" in st.session_state.modalidade else prod["varejo"]
    
    with coluna_atual:
        # Iniciando o Card Alinhado
        st.markdown(f"<div class='tiktok-card'>", unsafe_allow_html=True)
        
        # Bloco Padronizado de Imagem
        st.markdown(f"""
            <div class='container-imagem'>
                <img src='{prod["imagem"]}'>
            </div>
        """, unsafe_allow_html=True)
        
        # Conteúdo Textual Metrificado
        st.markdown(f"<p style='color:#00f2fe; font-size:12px; font-weight:700; text-align:left; margin:0;'>🎥 {prod['criador']}</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='titulo-produto'>{prod['nome']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#a0a0b0; font-size:11px; text-align:left; margin:0 0 8px 0;'>{prod['tags']}</p>", unsafe_allow_html=True)
        
        # Preços e Estoques
        st.markdown(f"<div style='text-align:left; margin-bottom:5px;'><span class='badge-shopee'>🔥 FLASH DEALS</span></div>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#fff; font-weight:800; text-align:left; margin:0;'>R$ {preco_exibido:.2f}</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style='text-align:left; font-size:10px; color:#ff5722; font-weight:bold; margin-top:5px;'>{prod['estoque_pct']}% Vendido</div>
            <div class='progresso-estoque'><div class='progresso-barra' style='width: {prod['estoque_pct']}%;'></div></div>
        """, unsafe_allow_html=True)
        
        # Atributos compactos para não quebrar layout
        c_cor = st.selectbox("Cor:", ["Padrão", "Estonado", "Preto"], key=f"feed_cor_{prod['id']}", label_visibility="collapsed")
        c_tam = st.select_slider("Tamanho:", options=["38", "40", "42", "44"] if "Calça" in prod["nome"] or "Bermuda" in prod["nome"] else ["P", "M", "G", "GG"], key=f"feed_tam_{prod['id']}", label_visibility="collapsed")
        
        st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
        
        # Ação Direta
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

# 10. INTERFACE DE CHECKOUT PROTEGIDA
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
            st.success("🎉 Compra aprovada! Enviando para separação física.")
            st.session_state.carrinho = []
            time.sleep(1.5)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
