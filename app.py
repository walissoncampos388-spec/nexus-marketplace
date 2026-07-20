import streamlit as st
import time

# 1. CONFIGURAÇÃO DA PÁGINA (Interface Imersiva e Otimizada)
st.set_page_config(
    page_title="NEXUS B2B & VAREJO | O Melhor do E-commerce",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. IDENTIDADE VISUAL E ESTRUTURA FIXA DO HEADER (CSS Avançado)
st.markdown("""
    <style>
    /* Estilização geral de fundo */
    .main { background-color: #fafafa; }
    
    /* BLOCO EXTRAORDINÁRIO: Trava o cabeçalho no topo e permite rolagem por baixo */
    [data-testid="stHeader"] {
        z-index: 999;
    }
    
    .header-fixo {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        background-color: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(10px);
        z-index: 999999;
        border-bottom: 1px solid #eaeaea;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        padding-bottom: 10px;
    }
    
    /* Compensação de espaço para o conteúdo não começar atrás do cabeçalho */
    .espacamento-conteudo {
        margin-top: 140px;
    }
    
    /* Customização dos botões pretos premium (Estilo Zara / Dafiti) */
    div.stButton > button:first-child {
        background-color: #000000;
        color: #ffffff;
        border-radius: 10px;
        border: 1px solid #000000;
        padding: 10px 20px;
        font-weight: 700;
        font-size: 14px;
        letter-spacing: 0.5px;
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #1e1e1e;
        border-color: #1e1e1e;
        color: #ffffff;
        transform: translateY(-2px);
    }
    
    /* Badges de Desconto Estilo Shopee/Shein */
    .badge-oferta {
        background: linear-gradient(135deg, #ff4b4b 0%, #ff2a2a 100%);
        color: white;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: inline-block;
        margin-bottom: 8px;
    }
    
    /* Card de Produto Customizado */
    .card-produto {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 16px;
        border: 1px solid #eaeaea;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIALIZAÇÃO DE ESTADOS DA SESSÃO
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []
if 'cupom_aplicado' not in st.session_state:
    st.session_state.cupom_aplicado = None
if 'desconto_porcentagem' not in st.session_state:
    st.session_state.desconto_porcentagem = 0.0

# 4. CRIAÇÃO DO CABEÇALHO TOTALMENTE FIXO
# Renderiza a estrutura HTML que prende os elementos no topo da tela
st.markdown("""
    <div class="header-fixo">
        <div style="background: linear-gradient(90deg, #000000 0%, #1a1a1a 100%); color: white; text-align: center; padding: 6px; font-size: 11px; font-weight: 600; letter-spacing: 1px;">
            ⚡ LOGÍSTICA EXPRESSA DISPONÍVEL • 10% OFF EXTRA NO PIX COM O CUPOM: <span style="color: #facc15; font-weight: 800;">NEXUS10</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Para manter os elementos nativos do Streamlit alinhados dentro da área fixa do topo
container_topo = st.container()
with container_topo:
    st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    
    # Linha 1: Logo e Sacola nas Extremidades
    col_logo, col_sacola = st.columns([5, 5])
    with col_logo:
        st.markdown("<h1 style='margin:0; font-weight:900; letter-spacing:-2px; line-height:1; font-size: 28px; color: black;'>NEXUS <span style='font-size:10px; font-weight:700; background-color:#000; color:#fff; padding:3px 8px; border-radius:4px; vertical-align:middle; margin-left:5px;'>MARKETPLACE</span></h1>", unsafe_allow_html=True)
        
    with col_sacola:
        total_itens_sacola = len(st.session_state.carrinho)
        st.markdown(f"<div style='text-align:right; font-weight:800; font-size:16px; margin-top:2px; color: black;'>🛒 Sacola <span style='background-color:#ff4b4b; color:white; padding:2px 8px; border-radius:20px; font-size:12px;'>{total_itens_sacola}</span></div>", unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    
    # Linha 2: Caixa de pesquisa fixa abaixo
    busca_query = st.text_input("Buscar", placeholder="O que você está procurando hoje? Ex: Jeans, Premium, Camiseta...", label_visibility="collapsed")

# 5. INÍCIO DO CONTEÚDO ROLÁVEL (Aplicando a margem de compensação)
st.markdown('<div class="espacamento-conteudo"></div>', unsafe_allow_html=True)

# BANCO DE DADOS DE PRODUTOS SIMULADO
banco_produtos = [
    {
        "id": 101, "nome": "Calça Denim Premium Slim Fit", "preco": 119.90, "preco_antigo": 199.90, "categoria": "Jeans",
        "imagem": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600&auto=format&fit=crop&q=80", "tag": "40% OFF",
        "cores": ["Jeans Escuro", "Jeans Claro", "Preto"], "tamanhos": ["38", "40", "42", "44", "46"]
    },
    {
        "id": 102, "nome": "Jaqueta Jeans Heavy Destroyed", "preco": 169.90, "preco_antigo": 249.90, "categoria": "Jeans",
        "imagem": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80", "tag": "Mais Vendido",
        "cores": ["Azul Stone", "Preto Estonado"], "tamanhos": ["P", "M", "G", "GG"]
    },
    {
        "id": 103, "nome": "Camiseta Algodão Egípcio Minimalista", "preco": 69.90, "preco_antigo": 99.90, "categoria": "Básicos",
        "imagem": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600&auto=format&fit=crop&q=80", "tag": "Fibras Longas",
        "cores": ["Branco Off", "Preto", "Mescla"], "tamanhos": ["P", "M", "G", "GG"]
    },
    {
        "id": 104, "nome": "Shorts Denim Hot Pants Comfort", "preco": 89.90, "preco_antigo": 139.90, "categoria": "Jeans",
        "imagem": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=600&auto=format&fit=crop&q=80", "tag": "Lançamento",
        "cores": ["Jeans Claro", "Branco"], "tamanhos": ["36", "38", "40", "42"]
    }
]

# 6. FILTROS AVANÇADOS NA SIDEBAR
st.sidebar.markdown("### 🔍 Central de Filtros")
filtro_categoria = st.sidebar.radio("Selecione a Linha:", ["Todas as Categorias", "Jeans", "Básicos"])
filtro_preco = st.sidebar.slider("Filtrar até que valor? (R$)", 50, 300, 300)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🚚 Simular Frete Integrado")
cep_input = st.sidebar.text_input("Digite seu CEP:", placeholder="75400-000")
if cep_input:
    st.sidebar.success("✓ Envio Próprio Nexus: **Chega em até 3 dias úteis**")

# Regra de negócio dos filtros
produtos_exibidos = []
for p in banco_produtos:
    if busca_query and busca_query.lower() not in p["nome"].lower():
        continue
    if filtro_categoria != "Todas as Categorias" and p["categoria"] != filtro_categoria:
        continue
    if p["preco"] > filtro_preco:
        continue
    produtos_exibidos.append(p)

# 7. VITRINE DE PRODUTOS
st.markdown("### 🚀 Vitrine Principal de Lançamentos")

if not produtos_exibidos:
    st.info("Nenhum produto corresponde aos filtros aplicados. Tente ajustar a busca na barra superior!")
else:
    colunas_vitrine = st.columns(4)
    
    for indice, prod in enumerate(produtos_exibidos):
        coluna_atual = colunas_vitrine[indice % 4]
        
        with coluna_atual:
            st.markdown(f"<div class='card-produto'>", unsafe_allow_html=True)
            st.image(prod["imagem"], use_container_width=True)
            st.markdown(f"<span class='badge-oferta'>{prod['tag']}</span>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='margin:2px 0; font-size:15px; font-weight:700;'>{prod['nome']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#a0a0a0; text-decoration:line-through; font-size:12px;'>De: R$ {prod['preco_antigo']:.2f}</span>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='margin:0 0 10px 0; color:#000000; font-weight:800;'>Por: R$ {prod['preco']:.2f}</h3>", unsafe_allow_html=True)
            
            cor_escolhida = st.selectbox("Cor:", prod["cores"], key=f"cor_{prod['id']}_{indice}")
            tamanho_escolhido = st.select_slider("Tamanho:", options=prod["tamanhos"], key=f"tam_{prod['id']}_{indice}")
            
            if st.button("Adicionar à Sacola", key=f"btn_add_{prod['id']}_{indice}"):
                item_carrinho = {
                    "id": prod["id"],
                    "nome": prod["nome"],
                    "preco": prod["preco"],
                    "cor": cor_escolhida,
                    "tamanho": tamanho_escolhido
                }
                st.session_state.carrinho.append(item_carrinho)
                st.toast(f"🛍️ {prod['nome']} ({tamanho_escolhido}/{cor_escolhida}) adicionado!")
                time.sleep(0.4)
                st.rerun()
                
            st.markdown("</div>", unsafe_allow_html=True)

# 8. SISTEMA DE CHECKOUT E PROCESSAMENTO
if len(st.session_state.carrinho) > 0:
    st.markdown("<br><hr style='border:1px solid #000;'/><br>", unsafe_allow_html=True)
    st.markdown("## 💳 Finalização de Compra Avançada")
    
    col_checkout_itens, col_checkout_resumo = st.columns([6, 4])
    
    with col_checkout_itens:
        st.markdown("### 1. Itens Selecionados na Sacola")
        for idx_item, item in enumerate(st.session_state.carrinho):
            c_item_nome, c_item_detalhe, c_item_preco, c_item_acao = st.columns([4, 3, 2, 1])
            with c_item_nome:
                st.markdown(f"**{item['nome']}**")
            with c_item_detalhe:
                st.markdown(f"🔹 Cor: `{item['cor']}` | Tam: `{item['tamanho']}`")
            with c_item_preco:
                st.markdown(f"**R$ {item['preco']:.2f}**")
            with c_item_acao:
                if st.button("❌", key=f"del_{idx_item}"):
                    st.session_state.carrinho.pop(idx_item)
                    st.rerun()
            st.markdown("<hr style='margin: 5px 0; border-top: 1px dashed #ccc;'/>", unsafe_allow_html=True)
            
    with col_checkout_resumo:
        st.markdown("### 2. Resumo Financeiro")
        subtotal_geral = sum([i['preco'] for i in st.session_state.carrinho])
        
        cupom_digitado = st.text_input("Tem um cupom de desconto?", placeholder="Digite aqui...").strip().upper()
        if cupom_digitado == "NEXUS10":
            st.session_state.cupom_aplicado = "NEXUS10"
            st.session_state.desconto_porcentagem = 0.10
            st.success("🎉 Cupom NEXUS10 ativo! 10% de desconto aplicado.")
        elif cupom_digitado != "":
            st.error("Cupom inválido ou expirado.")
            st.session_state.cupom_aplicado = None
            st.session_state.desconto_porcentagem = 0.0
            
        valor_desconto = subtotal_geral * st.session_state.desconto_porcentagem
        total_final = subtotal_geral - valor_desconto
        
        st.write(f"Subtotal dos Produtos: R$ {subtotal_geral:.2f}")
        if valor_desconto > 0:
            st.write(f"(-) Desconto Cupom: R$ {valor_desconto:.2f}")
        st.markdown(f"### Valor Total: <span style='color:#000;'>R$ {total_final:.2f}</span>", unsafe_allow_html=True)
        
        if st.button("🔥 Confirmar e Gerar Pedido"):
            with st.spinner("Conectando ao gateway de pagamento e reservando estoque..."):
                time.sleep(1.8)
            st.balloons()
            st.success("🎉 Pedido recebido com sucesso!")
            st.session_state.carrinho = []
            st.session_state.cupom_aplicado = None
            st.session_state.desconto_porcentagem = 0.0
            time.sleep(2.0)
            st.rerun()
