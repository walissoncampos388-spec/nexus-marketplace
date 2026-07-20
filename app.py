import streamlit as st
import time

# 1. CONFIGURAÇÃO DE ALTO PADRÃO DA INTERFACE
st.set_page_config(
    page_title="NEXUS INDUSTRIAL | Live & Volumetric Commerce",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ENGENHARIA DE DESIGN NEXT-GEN (CSS e Efeitos Neon)
st.markdown("""
    <style>
    .main { background-color: #08080c; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    [data-testid="stHeader"] { z-index: 999; }
    
    /* HEADER ULTRA MODERNO FLUIDO */
    .header-fixo {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        background: rgba(8, 8, 12, 0.9);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        z-index: 999999;
        padding-bottom: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }
    
    .espacamento-conteudo { margin-top: 165px; }
    
    /* CARDS DA VITRINE CYBERPUNK */
    .nexus-card {
        background: rgba(18, 18, 26, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 16px;
        border: 1px solid rgba(255, 255, 255, 0.03);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        min-height: 590px; /* Alinhamento fixo vertical */
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .nexus-card:hover {
        border-color: #00f2fe;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.15);
        transform: translateY(-5px);
    }
    
    /* RECIPIENTE DE MÍDIA PADRONIZADO (VÍDEO E IMAGEM) */
    .container-midia {
        width: 100%;
        height: 280px;
        overflow: hidden;
        border-radius: 16px;
        margin-bottom: 14px;
        background-color: #000;
        position: relative;
    }
    .container-midia img, .container-midia video {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    /* BOTÃO GLOW DE COMPRA INSTANTÂNEA */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
        color: #000000;
        border-radius: 14px;
        border: none;
        padding: 12px 24px;
        font-weight: 800;
        font-size: 13px;
        letter-spacing: 0.5px;
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
        background: linear-gradient(135deg, #ff0050 0%, #ff5722 100%);
        color: #ffffff;
    }
    
    /* BADGES DE OPERAÇÃO */
    .badge-live {
        background: linear-gradient(90deg, #ff0050 0%, #ff5722 100%);
        color: white;
        padding: 3px 10px;
        border-radius: 8px;
        font-size: 10px;
        font-weight: 900;
        letter-spacing: 0.5px;
        display: inline-block;
        animation: pulse 2s infinite;
    }
    
    .titulo-produto-neon {
        font-size: 15px;
        font-weight: 700;
        color: #ffffff;
        margin: 4px 0;
        height: 44px;
        overflow: hidden;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
    }
    
    .barra-progresso-cyber {
        background-color: #1a1a26;
        border-radius: 10px;
        height: 5px;
        overflow: hidden;
        margin: 6px 0 12px 0;
    }
    .barra-preenchimento {
        background: linear-gradient(90deg, #00f2fe, #4facfe);
        height: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTROLADORES INTERNOS
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []
if 'modalidade' not in st.session_state:
    st.session_state.modalidade = "🛍️ Varejo"

# 4. TOP BAR FIXA E TRANSPARENTE ULTRA-MODERNA
st.markdown("""
    <div class="header-fixo">
        <div style="background: linear-gradient(90deg, #00f2fe 0%, #ff0050 100%); color: black; text-align: center; padding: 4px; font-size: 11px; font-weight: 800; letter-spacing: 1px;">
            🤖 STREAMING ENGINE ATIVO • INTERFACES DE ALTA CONVERSÃO CONSOLIDADAS
        </div>
    </div>
""", unsafe_allow_html=True)

container_topo = st.container()
with container_topo:
    st.markdown("<div style='margin-top: 6px;'></div>", unsafe_allow_html=True)
    col_logo, col_tipo, col_sacola = st.columns([4, 3, 3])
    
    with col_logo:
        st.markdown("<h2 style='margin:0; font-weight:900; letter-spacing:-2px; color:#fff; font-size:28px;'>NEXUS <span style='font-size:9px; font-weight:800; background: #ffffff; color:#000; padding:2px 6px; border-radius:4px; margin-left:2px; vertical-align: middle;'>CORE v3</span></h2>", unsafe_allow_html=True)
        
    with col_tipo:
        st.session_state.modalidade = st.selectbox("Canal Logístico:", ["🛍️ Varejo", "📦 Atacado Distribuição (-35%)"], label_visibility="collapsed")
        
    with col_sacola:
        total_pecas = sum([item['quantidade'] for item in st.session_state.carrinho])
        st.markdown(f"<div style='text-align:right; font-weight:800; font-size:16px; margin-top:4px; color:#00f2fe;'>🛒 BAG [{total_pecas}]</div>", unsafe_allow_html=True)
        
    st.markdown("<div style='margin-top: 4px;'></div>", unsafe_allow_html=True)
    busca_query = st.text_input("Busca", placeholder="⚡ Digite o que procura... (Algoritmo preditivo ativo)", label_visibility="collapsed")

# 5. COMPENSAÇÃO DA ROLAGEM
st.markdown('<div class="espacamento-conteudo"></div>', unsafe_allow_html=True)

# 6. VITRINE DE PRODUTOS E INTEGRAÇÃO DE ARQUIVOS DE VÍDEO
# Nota técnica: Intercalamos vídeos MP4 reais direto de servidores públicos de alta velocidade para garantir o carregamento fluido.
catalogo_produtos = [
    {
        "id": 301, "nome": "Calça Denim Premium Slim Fit Casual", "varejo": 119.90, "atacado": 79.90, "estoque_pct": 82,
        "tipo_midia": "video", "midia_url": "https://assets.mixkit.co/videos/preview/mixkit-girl-in-neon-light-outfit-modelling-40032-large.mp4",
        "criador": "@look_denim", "tags": "Tecido Tecnológico • Caimento"
    },
    {
        "id": 302, "nome": "Jaqueta Jeans Heavy Destroyed Vintage", "varejo": 169.90, "atacado": 115.00, "estoque_pct": 95,
        "tipo_midia": "imagem", "midia_url": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80",
        "criador": "@street_core", "tags": "Alta Gramatura • Urban"
    },
    {
        "id": 303, "nome": "Camiseta Pima Egípcio Minimalist Lux", "varejo": 69.90, "atacado": 45.00, "estoque_pct": 14,
        "tipo_midia": "video", "midia_url": "https://assets.mixkit.co/videos/preview/mixkit-man-holding-a-smartphone-in-a-neon-night-40018-large.mp4",
        "criador": "@basicos_premium", "tags": "Toque Macio • Fibras Nobres"
    },
    {
        "id": 304, "nome": "Shorts Denim Hot Pants Confort Bold", "varejo": 89.90, "atacado": 59.90, "estoque_pct": 48,
        "tipo_midia": "imagem", "midia_url": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=600&auto=format&fit=crop&q=80",
        "criador": "@summer_nexus", "tags": "Lavagem Exclusiva • Verão"
    },
    {
        "id": 305, "nome": "Calça Jogger Tech Jeans com Ajuste Coated", "varejo": 139.90, "atacado": 89.90, "estoque_pct": 65,
        "tipo_midia": "video", "midia_url": "https://assets.mixkit.co/videos/preview/mixkit-woman-dancing-in-a-neon-lit-room-40011-large.mp4",
        "criador": "@tech_wear", "tags": "Cintura Adaptável • Confort"
    },
    {
        "id": 306, "nome": "Bermuda Cargo Industrial Denim Heavy", "varejo": 99.90, "atacado": 65.00, "estoque_pct": 77,
        "tipo_midia": "imagem", "midia_url": "https://images.unsplash.com/photo-1565049033148-18e3a241e7f3?w=600&auto=format&fit=crop&q=80",
        "criador": "@cia_jeans", "tags": "Bolsos Utilitários • Reforçada"
    }
]

# Filtro
produtos_filtrados = [p for p in catalogo_produtos if busca_query.lower() in p["nome"].lower()] if busca_query else catalogo_produtos

# 7. EXIBIÇÃO EM GRID PADRONIZADO
st.markdown("### ⚡ Live Stream Catalog")

colunas_vitrine = st.columns(3) # Grid em 3 colunas para valorizar a escala dos vídeos verticais
for idx, prod in enumerate(produtos_filtrados):
    coluna_atual = colunas_vitrine[idx % 3]
    preco_final = prod["atacado"] if "Atacado" in st.session_state.modalidade else prod["varejo"]
    
    with coluna_atual:
        st.markdown('<div class="nexus-card">', unsafe_allow_html=True)
        
        # Renderização condicional de Mídia (Imagens e Vídeos Intercalados ativos)
        if prod["tipo_midia"] == "video":
            st.markdown(f"""
                <div class="container-midia">
                    <video autoplay loop muted playsinline>
                        <source src="{prod['midia_url']}" type="video/mp4">
                    </video>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="container-midia">
                    <img src="{prod['midia_url']}">
                </div>
            """, unsafe_allow_html=True)
            
        # Conteúdo de Texto e Informações Comerciais
        st.markdown(f"<p style='color:#00f2fe; font-size:12px; font-weight:700; text-align:left; margin:0;'>⚡ {prod['criador']}</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='titulo-produto-neon'>{prod['nome']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#62627a; font-size:11px; text-align:left; margin:0 0 8px 0;'>{prod['tags']}</p>", unsafe_allow_html=True)
        
        st.markdown(f"<div style='text-align:left; margin-bottom:4px;'><span class='badge-live'>● LIVE OFFER</span></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:#ffffff; font-weight:900; text-align:left; margin:0;'>R$ {preco_final:.2f}</h3>", unsafe_allow_html=True)
        
        # Indicadores Shopee Style
        st.markdown(f"""
            <div style='text-align:left; font-size:10px; color:#4facfe; font-weight:bold; margin-top:5px;'>Estoque Crítico: {prod['estoque_pct']}%</div>
            <div class='barra-progresso-cyber'><div class='barra-preenchimento' style='width: {prod['estoque_pct']}%;'></div></div>
        """, unsafe_allow_html=True)
        
        # Seletores Limpos
        c_cor = st.selectbox("Tonalidade:", ["Padrão Industrial", "Raw Black"], key=f"c_{prod['id']}", label_visibility="collapsed")
        c_tam = st.select_slider("Grade:", options=["38", "40", "42", "44"] if "Calça" in prod["nome"] or "Bermuda" in prod["nome"] else ["P", "M", "G", "GG"], key=f"t_{prod['id']}", label_visibility="collapsed")
        
        st.markdown("<div style='margin-top: 4px;'></div>", unsafe_allow_html=True)
        
        # Ação Final
        if st.button("INSTANT BUY", key=f"btn_nk_{prod['id']}"):
            st.session_state.carrinho.append({
                "nome": prod["nome"],
                "preco": preco_final,
                "cor": c_cor,
                "tamanho": c_tam,
                "quantidade": 1
            })
            st.toast("⚡ Item mapeado e adicionado à sacola corporativa!")
            time.sleep(0.3)
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)

# 8. SISTEMA DE FECHAMENTO ULTRA SECURE
if len(st.session_state.carrinho) > 0:
    st.markdown("<br><hr style='border-top:1px solid rgba(255,255,255,0.05);'/><br>", unsafe_allow_html=True)
    st.markdown("### 💳 Secure Industrial Checkout")
    
    col_cart_l, col_cart_r = st.columns([6, 4])
    
    with col_cart_l:
        for idx_c, item in enumerate(st.session_state.carrinho):
            l1, l2, l3, l4 = st.columns([4, 3, 2, 1])
            with l1: st.write(f"**{item['nome']}**")
            with l2: st.write(f"⚙️ `{item['cor']}` / G: `{item['tamanho']}`")
            with l3: st.write(f"R$ {item['preco']:.2f}")
            with l4: 
                if st.button("✕", key=f"rm_{idx_c}"):
                    st.session_state.carrinho.pop(idx_c)
                    st.rerun()
            st.markdown("<hr style='border-top: 1px dashed rgba(255,255,255,0.05); margin:4px 0;'/>", unsafe_allow_html=True)
            
    with col_cart_r:
        subtotal = sum([i['preco'] for i in st.session_state.carrinho])
        st.markdown("<div style='background-color:#12121a; padding:20px; border-radius:20px; border:1px solid rgba(255,255,255,0.05);'>", unsafe_allow_html=True)
        st.write(f"Subtotal dos Lotes: R$ {subtotal:.2f}")
        st.markdown("### Total Líquido: R$ {:.2f}".format(subtotal))
        if st.button("CONFIRMAR E EMITIR FATURA"):
            with st.spinner("Processando ordens e gerando chave PIX corporativa..."):
                time.sleep(1.5)
            st.balloons()
            st.success("🎉 Faturamento concluído! Integração logística ativada.")
            st.session_state.carrinho = []
            time.sleep(1.5)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
