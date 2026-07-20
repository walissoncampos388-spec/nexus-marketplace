import streamlit as st
import time
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA (Interface Imersiva e Otimizada)
st.set_page_config(
    page_title="NEXUS | Atacado & Varejo Premium",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. IDENTIDADE VISUAL E ESTRUTURA FIXA DO HEADER (CSS Avançado)
st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    
    [data-testid="stHeader"] { z-index: 999; }
    
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
    
    .espacamento-conteudo { margin-top: 140px; }
    
    /* Customização dos botões pretos premium */
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
        transform: translateY(-2px);
    }
    
    .badge-oferta {
        background: linear-gradient(135deg, #ff4b4b 0%, #ff2a2a 100%);
        color: white;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 900;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 8px;
    }
    
    .card-produto {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 16px;
        border: 1px solid #eaeaea;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INICIALIZAÇÃO DE ESTADOS DA SESSÃO (Gerenciamento de Persistência)
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []
if 'historico_pedidos' not in st.session_state:
    st.session_state.historico_pedidos = []
if 'cupom_aplicado' not in st.session_state:
    st.session_state.cupom_aplicado = None
if 'desconto_porcentagem' not in st.session_state:
    st.session_state.desconto_porcentagem = 0.0

# 4. CRIAÇÃO DO CABEÇALHO TOTALMENTE FIXO
st.markdown("""
    <div class="header-fixo">
        <div style="background: linear-gradient(90deg, #000000 0%, #1a1a1a 100%); color: white; text-align: center; padding: 6px; font-size: 11px; font-weight: 600; letter-spacing: 1px;">
            ⚡ MODALIDADE HÍBRIDA ATIVA • PREÇOS PROGRESSIVOS PARA CNPJ OU ATACADO ACIMA DE R$ 500
        </div>
    </div>
""", unsafe_allow_html=True)

container_topo = st.container()
with container_topo:
    st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    
    col_logo, col_sacola = st.columns([5, 5])
    with col_logo:
        st.markdown("<h1 style='margin:0; font-weight:900; letter-spacing:-2px; line-height:1; font-size: 28px; color: black;'>NEXUS <span style='font-size:10px; font-weight:700; background-color:#000; color:#fff; padding:3px 8px; border-radius:4px; vertical-align:middle; margin-left:5px;'>ECOMMERCE HUB</span></h1>", unsafe_allow_html=True)
        
    with col_sacola:
        total_itens_sacola = sum([item['quantidade'] for item in st.session_state.carrinho])
        st.markdown(f"<div style='text-align:right; font-weight:800; font-size:16px; margin-top:2px; color: black;'>🛒 Sacola <span style='background-color:#ff4b4b; color:white; padding:2px 8px; border-radius:20px; font-size:12px;'>{total_itens_sacola}</span></div>", unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 5px;'></div>", unsafe_allow_html=True)
    busca_query = st.text_input("Buscar", placeholder="O que você está procurando hoje? Ex: Jeans, Premium, Camiseta...", label_visibility="collapsed")
    st.markdown("<hr style='margin: 12px 0 5px 0; border-top: 1px solid #eee;'/>", unsafe_allow_html=True)

# 5. INÍCIO DO CONTEÚDO ROLÁVEL
st.markdown('<div class="espacamento-conteudo"></div>', unsafe_allow_html=True)

# 6. CONFIGURAÇÕES COMERCIAIS NA SIDEBAR
st.sidebar.markdown("## 📊 Parâmetros Comerciais")
modalidade = st.sidebar.radio("Selecione o Tipo de Compra:", ["🛍️ Varejo", "📦 Atacado (Preços Reduzidos)"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Filtros de Busca")
filtro_categoria = st.sidebar.selectbox("Linha de Produto:", ["Todas as Categorias", "Jeans", "Básicos"])
filtro_preco = st.sidebar.slider("Preço Máximo Unitário (R$)", 50, 300, 300)

# 7. BANCO DE DADOS DE PRODUTOS SIMULADO (Com preços diferenciais)
banco_produtos = [
    {
        "id": 101, "nome": "Calça Denim Premium Slim Fit", "preco_varejo": 119.90, "preco_atacado": 79.90, "categoria": "Jeans",
        "imagem": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600&auto=format&fit=crop&q=80", "tag": "40% OFF",
        "cores": ["Jeans Escuro", "Jeans Claro", "Preto"], "tamanhos": ["38", "40", "42", "44", "46"]
    },
    {
        "id": 102, "nome": "Jaqueta Jeans Heavy Destroyed", "preco_varejo": 169.90, "preco_atacado": 115.00, "categoria": "Jeans",
        "imagem": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=600&auto=format&fit=crop&q=80", "tag": "Mais Vendido",
        "cores": ["Azul Stone", "Preto Estonado"], "tamanhos": ["P", "M", "G", "GG"]
    },
    {
        "id": 103, "nome": "Camiseta Algodão Egípcio Minimalista", "preco_varejo": 69.90, "preco_atacado": 45.00, "categoria": "Básicos",
        "imagem": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600&auto=format&fit=crop&q=80", "tag": "Fibras Longas",
        "cores": ["Branco Off", "Preto", "Mescla"], "tamanhos": ["P", "M", "G", "GG"]
    },
    {
        "id": 104, "nome": "Shorts Denim Hot Pants Comfort", "preco_varejo": 89.90, "preco_atacado": 59.90, "categoria": "Jeans",
        "imagem": "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?w=600&auto=format&fit=crop&q=80", "tag": "Lançamento",
        "cores": ["Jeans Claro", "Branco"], "tamanhos": ["36", "38", "40", "42"]
    }
]

# Regras de Filtragem
produtos_exibidos = []
for p in banco_produtos:
    preco_atual = p["preco_atacado"] if "Atacado" in modalidade else p["preco_varejo"]
    if busca_query and busca_query.lower() not in p["nome"].lower():
        continue
    if filtro_categoria != "Todas as Categorias" and p["categoria"] != filtro_categoria:
        continue
    if preco_current := preco_atual > filtro_preco:
        continue
    produtos_exibidos.append(p)

# 8. EXIBIÇÃO DA VITRINE
st.markdown(f"### 🚀 Catalogo de Lançamentos — Exibindo Preços de **{modalidade.upper()}**")

if not produtos_exibidos:
    st.info("Nenhum produto corresponde aos filtros aplicados.")
else:
    colunas_vitrine = st.columns(4)
    for indice, prod in enumerate(produtos_exibidos):
        coluna_atual = colunas_vitrine[indice % 4]
        preco_venda = prod["preco_atacado"] if "Atacado" in modalidade else prod["preco_varejo"]
        
        with coluna_atual:
            st.markdown(f"<div class='card-produto'>", unsafe_allow_html=True)
            st.image(prod["imagem"], use_container_width=True)
            st.markdown(f"<span class='badge-oferta'>{prod['tag']}</span>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='margin:2px 0; font-size:15px; font-weight:700;'>{prod['nome']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='margin:0 0 10px 0; color:#ff4b4b; font-weight:800;'>R$ {preco_venda:.2f}</h3>", unsafe_allow_html=True)
            
            c_cor = st.selectbox("Cor:", prod["cores"], key=f"cor_{prod['id']}_{indice}")
            c_tam = st.select_slider("Tamanho:", options=prod["tamanhos"], key=f"tam_{prod['id']}_{indice}")
            c_qtd = st.number_input("Qtd:", min_value=1, max_value=100, value=1 if "Varejo" in modalidade else 12, key=f"qtd_{prod['id']}_{indice}")
            
            if st.button("Adicionar à Sacola", key=f"btn_add_{prod['id']}_{indice}"):
                # Verifica se o item com mesma cor/tamanho já está no carrinho
                ja_existe = False
                for item in st.session_state.carrinho:
                    if item['id'] == prod['id'] and item['cor'] == c_cor and item['tamanho'] == c_tam:
                        item['quantidade'] += c_qtd
                        ja_existe = True
                        break
                
                if not ja_existe:
                    st.session_state.carrinho.append({
                        "id": prod["id"], "nome": prod["nome"], "preco": preco_venda,
                        "cor": c_cor, "tamanho": c_tam, "quantidade": c_qtd
                    })
                st.toast("🛒 Sacola Atualizada!")
                time.sleep(0.3)
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

# 9. TELA DE GERENCIAMENTO DO CARRINHO / CHECKOUT
if len(st.session_state.carrinho) > 0:
    st.markdown("<br><hr style='border:1px solid #000;'/><br>", unsafe_allow_html=True)
    st.markdown("## 💳 Painel de Fechamento & Resumo do Pedido")
    
    col_itens, col_resumo = st.columns([6, 4])
    
    with col_itens:
        st.markdown("### 1. Itens na Sacola")
        for idx, item in enumerate(st.session_state.carrinho):
            c_nome, c_detalhe, c_qtd_edit, c_preco, c_deletar = st.columns([3, 2, 2, 2, 1])
            with c_nome:
                st.markdown(f"**{item['nome']}**")
            with c_detalhe:
                st.markdown(f"`{item['cor']}` / `{item['tamanho']}`")
            with c_qtd_edit:
                nova_qtd = st.number_input("Qtd", min_value=1, value=item['quantidade'], key=f"edit_qtd_{idx}", label_visibility="collapsed")
                if nova_qtd != item['quantidade']:
                    item['quantidade'] = nova_qtd
                    st.rerun()
            with c_preco:
                st.markdown(f"**R$ {item['preco'] * item['quantidade']:.2f}**")
            with c_deletar:
                if st.button("❌", key=f"del_{idx}"):
                    st.session_state.carrinho.pop(idx)
                    st.rerun()
            st.markdown("<hr style='margin: 4px 0; border-top: 1px dashed #eee;'/>", unsafe_allow_html=True)
            
    with col_resumo:
        st.markdown("### 2. Resumo da Fatura")
        subtotal = sum([item['preco'] * item['quantidade'] for item in st.session_state.carrinho])
        
        # Validação de regras comerciais para Atacado
        liberado_compra = True
        if "Atacado" in modalidade and subtotal < 500.00:
            st.error(f"⚠️ O pedido mínimo para faturamento em Atacado é de **R$ 500,00**. Faltam R$ {500.00 - subtotal:.2f}")
            liberado_compra = False
            
        cupom = st.text_input("Cupom Corporativo / Promocional:", placeholder="Ex: NEXUS10").strip().upper()
        if cupom == "NEXUS10":
            st.session_state.desconto_porcentagem = 0.10
            st.success("✓ Desconto de 10% aplicado.")
        elif cupom != "":
            st.session_state.desconto_porcentagem = 0.0
            
        total_desconto = subtotal * st.session_state.desconto_porcentagem
        total_geral = subtotal - total_desconto
        
        st.write(f"Subtotal Geral: R$ {subtotal:.2f}")
        st.write(f"Descontos: R$ {total_desconto:.2f}")
        st.markdown(f"### Total Final: **R$ {total_geral:.2f}**")
        
        if st.button("🚀 Finalizar Pedido", disabled=not liberado_compra):
            novo_pedido = {
                "Pedido ID": int(time.time()),
                "Modalidade": modalidade,
                "Itens": sum([i['quantidade'] for i in st.session_state.carrinho]),
                "Valor Faturado": total_geral
            }
            st.session_state.historico_pedidos.append(novo_pedido)
            st.balloons()
            st.success("🎉 Pedido Processado e enviado para a esteira logística!")
            st.session_state.carrinho = []
            time.sleep(1.5)
            st.rerun()

# 10. PAINEL ADMINISTRATIVO (Gestão Interna Corporativa)
if len(st.session_state.historico_pedidos) > 0:
    st.markdown("<br><hr/><br>", unsafe_allow_html=True)
    st.markdown("## 📊 Console de Gestão Operacional (Exclusivo ERP)")
    df_pedidos = pd.DataFrame(st.session_state.historico_pedidos)
    
    c_card1, c_card2 = st.columns(2)
    with c_card1:
        st.metric("Volume de Vendas Faturado", f"R$ {df_pedidos['Valor Faturado'].sum():.2f}")
    with c_card2:
        st.metric("Total de Peças Despachadas", f"{df_pedidos['Itens'].sum()} und")
        
    st.dataframe(df_pedidos, use_container_width=True)
