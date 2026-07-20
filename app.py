import streamlit as st
import time

# 1. CONFIGURAÇÃO PREMIUM DA INTERFACE
st.set_page_config(
    page_title="NEXUS SOCIAL | O Futuro do E-Commerce",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ENGENHARIA DE DESIGN SOCIAL APP (CSS e Visual Dark)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    [data-testid="stHeader"] { z-index: 999; }
    
    /* HEADER FIXO DE REDE SOCIAL */
    .header-fixo {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        background: rgba(0, 0, 0, 0.9);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        z-index: 999999;
        padding-bottom: 12px;
    }
    
    .espacamento-conteudo { margin-top: 160px; }
    
    /* CARD DE POST DA REDE SOCIAL */
    .post-card {
        background: #121212;
        border-radius: 24px;
        padding: 16px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        min-height: 640px; /* Alinhamento fixo vertical */
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .post-card:hover {
        border-color: #ff0050;
    }
    
    /* RECIPIENTE DE MÍDIA DE ALTO IMPACTO (REELS/POST) */
    .container-midia {
        width: 100%;
        height: 320px;
        overflow: hidden;
        border-radius: 18px;
        margin-bottom: 14px;
        background-color: #080808;
    }
    .container-midia img, .container-midia video {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    
    /* METRICS DA REDE SOCIAL */
    .social-metrics {
        display: flex;
        gap: 15px;
        font-size: 13px;
        color: #a0a0a0;
        margin: 8px 0;
    }
    
    /* BOTÃO COMPRAR LOOK DO POST */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff0050 0%, #ff5722 100%);
        color: #ffffff;
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
        box-shadow: 0 0 20px rgba(255, 0, 80, 0.4);
    }
    
    .perfil-usuario {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 10px;
    }
    .perfil-avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: linear-gradient(45deg, #facc15, #ff0050);
        padding: 2px;
    }
    .perfil-avatar img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
    }
    
    .tag-produto {
        background: rgba(255, 255, 255, 0.1);
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 11px;
        font-weight: 600;
        display: inline-block;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CONTROLADORES INTERNOS (ESTADOS DA REDE)
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []
if 'likes' not in st.session_state:
    st.session_state.likes = {}
if 'modalidade' not in st.session_state:
    st.session_state.modalidade = "🛍️ Varejo"

# 4. TOP BAR FIXA DA REDE SOCIAL
st.markdown("""
    <div class="header-fixo">
        <div style="background: linear-gradient(90deg, #ff0050 0%, #00f2fe 100%); color: black; text-align: center; padding: 4px; font-size: 11px; font-weight: 800; letter-spacing: 1px;">
            🔥 SOCIAL SHOPPING FEED • ASSISTA OS LOOKS DAS INFLUENCIADORES E GARANTA O SEU
        </div>
    </div>
""", unsafe_allow_html=True)

container_topo = st.container()
with container_topo:
    st.markdown("<div style='margin-top: 6px;'></div>", unsafe_allow_html=True)
    col_logo, col_tipo, col_sacola = st.columns([4, 3, 3])
    
    with col_logo:
        st.markdown("<h2 style='margin:0; font-weight:900; letter-spacing:-2px; color:#fff; font-size:28px;'>NEXUS <span style='font-size:9px; font-weight:800; background: #ff0050; color:#fff; padding:2px 6px; border-radius:4px; margin-left:2px; vertical-align: middle;'>FEED</span></h2>", unsafe_allow_html=True)
        
    with col_tipo:
        st.session_state.modalidade = st.selectbox("Comprar em:", ["🛍️ Compra Individual (Varejo)", "📦 Pedido Coletivo / Lojista (Atacado)"], label_visibility="collapsed")
        
    with col_sacola:
        total_pecas = sum([item['quantidade'] for item in st.session_state.carrinho])
        st.markdown(f"<div style='text-align:right; font-weight:800; font-size:16px; margin-top:4px; color:#ff0050;'>🛒 Sacola [{total_pecas}]</div>", unsafe_allow_html=True)
        
    st.markdown("<div style='margin-top: 4px;'></div>", unsafe_allow_html=True)
    busca_query = st.text_input("Busca", placeholder="🔎 Buscar criadores, hashtags (#jeans, #streetwear) ou roupas...", label_visibility="collapsed")

# 5. COMPENSAÇÃO DA ROLAGEM
st.markdown('<div class="espacamento-conteudo"></div>', unsafe_allow_html=True)

# 6. BASE DE DADOS SOCIAL (POSTS + PRODUTOS VINCULADOS)
feed_posts = [
    {
        "id": 501, "criador": "amanda_silva", "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&auto=format&fit=crop&q=80",
        "legenda": "Montando o look perfeito com essa calça slim premium! O caimento dela é surreal 🥵🔥 #moda #jeans #streetwear",
        "likes_base": 1240, "comentarios": 84, "tipo_midia": "video",
        "midia_url": "https://assets.mixkit.co/videos/preview/mixkit-girl-in-neon-light-outfit-modelling-40032-large.mp4",
        "produto": {"nome": "Calça Denim Premium Slim Fit", "varejo": 119.90, "atacado": 79.90}
    },
    {
        "id": 502, "criador": "pedro_urban", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&auto=format&fit=crop&q=80",
        "legenda": "Jaqueta jeans destroyed pesada demais pro rolê de hoje à noite. Quem curtiu comenta aí! 🤟⚡ #aesthetic #outfit",
        "likes_base": 956, "comentarios": 42, "tipo_midia": "imagem",
        "midia_url": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80",
        "produto": {"nome": "Jaqueta Jeans Heavy Destroyed", "varejo": 169.90, "atacado": 115.00}
    },
    {
        "id": 503, "criador": "carol_trends", "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&auto=format&fit=crop&q=80",
        "legenda": "Básico não precisa ser sem graça. Essa t-shirt de algodão egípcio é a prova disso ✨ Comfy & chic. #basic #lookdodia",
        "likes_base": 3120, "comentarios": 195, "tipo_midia": "video",
        "midia_url": "https://assets.mixkit.co/videos/preview/mixkit-woman-dancing-in-a-neon-lit-room-40011-large.mp4",
        "produto": {"nome": "Camiseta Algodão Egípcio Minimalista", "varejo": 69.90, "atacado": 45.00}
    },
    {
        "id": 504, "criador": "gabi_moraes", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80",
        "legenda": "Shorts hot pants pra curtir o final de semana no mood certo! ☀️🌊 Quem mais ama o verão? #summer #denim",
        "likes_base": 1845, "comentarios": 67, "tipo_midia": "imagem",
        "midia_url": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=600&auto=format&fit=crop&q=80",
        "produto": {"nome": "Shorts Denim Hot Pants Comfort", "varejo": 89.90, "atacado": 59.90}
    }
]

# Filtro simplificado
posts_filtrados = [p for p in feed_posts if busca_query.lower() in p["legenda"].lower() or busca_query.lower() in p["criador"].lower()] if busca_query else feed_posts

# 7. EXIBIÇÃO EM GRID DE FEED SOCIAL (3 COLUNAS)
st.markdown("### 🎬 Tendências da Comunidade")

colunas_feed = st.columns(3)
for idx, post in enumerate(posts_filtrados):
    coluna_atual = colunas_feed[idx % 3]
    preco_final = post["produto"]["atacado"] if "Atacado" in st.session_state.modalidade else post["produto"]["varejo"]
    
    # Inicializa estado individual do like se não existir
    if post["id"] not in st.session_state.likes:
        st.session_state.likes[post["id"]] = False
        
    with coluna_atual:
        st.markdown('<div class="post-card">', unsafe_allow_html=True)
        
        # 1. Topo do Post: Perfil do Criador
        st.markdown(f"""
            <div class="perfil-usuario">
                <div class="perfil-avatar"><img src="{post['avatar']}"></div>
                <div style="font-weight:700; font-size:14px;">{post['criador']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # 2. Mídia Central (Vídeo Reels ou Imagem)
        if post["tipo_midia"] == "video":
            st.markdown(f"""
                <div class="container-midia">
                    <video autoplay loop muted playsinline>
                        <source src="{post['midia_url']}" type="video/mp4">
                    </video>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="container-midia">
                    <img src="{post['midia_url']}">
                </div>
            """, unsafe_allow_html=True)
            
        # 3. Métricas Sociais e Interatividade
        c_like, c_coment = st.columns([1, 1])
        with c_like:
            texto_like = "❤️ Curtido" if st.session_state.likes[post["id"]] else "🤍 Curtir"
            num_likes = post['likes_base'] + (1 if st.session_state.likes[post["id"]] else 0)
            if st.button(f"{texto_like} ({num_likes})", key=f"lk_{post['id']}"):
                st.session_state.likes[post["id"]] = not st.session_state.likes[post["id"]]
                st.rerun()
        with c_coment:
            st.markdown(f"<p style='margin-top:8px; text-align:right;'>💬 {post['comentarios']} comentários</p>", unsafe_allow_html=True)
            
        # 4. Legenda do Post
        st.markdown(f"<p style='font-size:13px; color:#e0e0e0; margin:10px 0; min-height:40px;'>{post['legenda']}</p>", unsafe_allow_html=True)
        
        # 5. Box de Venda Vinculado ao Look do Post
        st.markdown("<div style='background:rgba(255,255,255,0.03); padding:12px; border-radius:14px; margin-bottom:10px;'>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:12px; font-weight:700; color:#ff0050;'>🛒 PEÇA DO LOOK:</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:13px; font-weight:600;'>{post['produto']['nome']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:16px; font-weight:800; margin-top:4px;'>R$ {preco_final:.2f}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Seletores Rápidos de Tamanho
        c_tam = st.select_slider("Tamanho:", options=["38", "40", "42", "44"] if "Calça" in post["produto"]["nome"] or "Shorts" in post["produto"]["nome"] else ["P", "M", "G", "GG"], key=f"t_{post['id']}", label_visibility="collapsed")
        
        st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
        
        # 6. Ação de Compra Social
        if st.button("🛍️ COMPRAR ESTE LOOK", key=f"btn_shop_{post['id']}"):
            st.session_state.carrinho.append({
                "nome": post["produto"]["nome"],
                "preco": preco_final,
                "tamanho": c_tam,
                "quantidade": 1
            })
            st.toast(f"🛒 Look da @{post['criador']} adicionado à sacola!")
            time.sleep(0.3)
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)

# 8. SISTEMA DE CHECKOUT SEGURO
if len(st.session_state.carrinho) > 0:
    st.markdown("<br><hr style='border-top:1px solid rgba(255,255,255,0.1);'/><br>", unsafe_allow_html=True)
    st.markdown("### 🛒 Sacola do Social Commerce")
    
    col_cart_l, col_cart_r = st.columns([6, 4])
    
    with col_cart_l:
        for idx_c, item in enumerate(st.session_state.carrinho):
            l1, l2, l3, l4 = st.columns([4, 3, 2, 1])
            with l1: st.write(f"**{item['nome']}**")
            with l2: st.write(f"✨ Tamanho: `{item['tamanho']}`")
            with l3: st.write(f"R$ {item['preco']:.2f}")
            with l4: 
                if st.button("✕", key=f"rm_{idx_c}"):
                    st.session_state.carrinho.pop(idx_c)
                    st.rerun()
            st.markdown("<hr style='border-top: 1px dashed rgba(255,255,255,0.05); margin:4px 0;'/>", unsafe_allow_html=True)
            
    with col_cart_r:
        subtotal = sum([i['preco'] for i in st.session_state.carrinho])
        st.markdown("<div style='background-color:#12121a; padding:20px; border-radius:20px; border:1px solid rgba(255,255,255,0.05);'>", unsafe_allow_html=True)
        st.write(f"Subtotal dos Looks: R$ {subtotal:.2f}")
        st.markdown("### Total Final: R$ {:.2f}".format(subtotal))
        if st.button("🔒 IR PARA O PAGAMENTO"):
            with st.spinner("Conectando e processando ordens sociais..."):
                time.sleep(1.5)
            st.balloons()
            st.success("🎉 Pedido recebido com sucesso! Seu look já está na esteira de despacho.")
            st.session_state.carrinho = []
            time.sleep(1.5)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
