import streamlit as st

# Configuración de página
st.set_page_config(page_title="Roof-Aid App", layout="centered")

# --- RUTA DEL LOGO (Basado en tu repositorio) ---
# Los navegadores necesitan %20 en lugar de espacios
LOGO_URL = "https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/WhatsApp%20Image%202026-02-21%20at%209.25.44%20PM.jpeg".replace(" ", "%20")

# Icono de casa para las historias
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS PERSONALIZADO ---
st.markdown(f"""
    <style>
    .stApp {{
        background: radial-gradient(circle, #203a5c 0%, #152033 100%);
        color: white;
    }}
    
    /* Contenedor del Logo ajustado arriba a la derecha */
    .logo-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: -70px;
        margin-bottom: 30px;
    }}
    .main-logo {{
        width: 100px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }}
    
    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}
    
    /* Centrado total de Historias */
    .story-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-bottom: 20px;
    }}

    .story-circle {{
        border-radius: 50%;
        width: 70px;
        height: 70px;
        padding: 3px;
        background-color: white;
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    
    .orange-border {{ border: 4px solid #F57C00; }} 
    .green-border {{ border: 4px solid #28A745; }}
    
    .house-icon {{ 
        width: 45px; 
        height: 45px; 
        object-fit: contain; 
    }}

    /* Estilo del texto Owner centrado */
    .owner-label {{
        font-size: 13px;
        font-weight: 600;
        margin-top: 8px;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }}

    /* Barra de navegación inferior */
    .stTabs [data-baseweb="tab-list"] {{
        position: fixed;
        bottom: 0;
        background: #152033;
        z-index: 100;
        width: 100%;
        justify-content: center;
        border-top: 1px solid rgba(255,255,255,0.1);
    }}
    </style>
    """, unsafe_allow_html=True)

# 1. Mostrar Logo
st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    st.write("### Potential Customers")
    
    # Historias en 4 columnas
    cols = st.columns(4)
    stories = [
        {"border": "orange-border"},
        {"border": "green-border"},
        {"border": "orange-border"},
        {"border": "green-border"}
    ]
    
    for i, story in enumerate(stories):
        with cols[i]:
            st.markdown(f"""
                <div class="story-wrapper">
                    <div class="story-circle {story['border']}">
                        <img src="{HOUSE_ICON_URL}" class="house-icon">
                    </div>
                    <div class="owner-label">Owner</div>
                </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.write("### Feed")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4") 
    st.write("**Storm Intel:** Hail activity detected. Potential claims identified.")

with tab_messages:
    st.write("### Messages")
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Hope you're doing today!")
