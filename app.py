import streamlit as st

# Configuración de página para móviles
st.set_page_config(page_title="Roof-Aid App", layout="centered")

# --- RUTA DEL LOGO (Basado en el archivo subido a GitHub) ---
# Se utiliza el nombre exacto del archivo que mencionaste
LOGO_URL = "WhatsApp Image 2026-02-21 at 9.25.44 PM.jpeg"

# Icono de casa para las historias
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS PERSONALIZADO (Estilo Instagram Premium) ---
st.markdown(f"""
    <style>
    .stApp {{
        background: radial-gradient(circle, #203a5c 0%, #152033 100%);
        color: white;
    }}
    
    /* Contenedor del Logo en la parte superior derecha */
    .logo-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: -60px;
        margin-bottom: 20px;
    }}
    .main-logo {{
        width: 110px;
        border-radius: 10px;
    }}
    
    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}
    
    /* Estilo de los círculos de historias */
    .story-wrapper {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
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
        margin-bottom: 5px;
    }}
    
    .orange-border {{ border: 4px solid #F57C00; box-shadow: 0 0 10px rgba(245, 124, 0, 0.3); }} 
    .green-border {{ border: 4px solid #28A745; box-shadow: 0 0 10px rgba(40, 167, 69, 0.3); }}
    
    .house-icon {{ width: 45px; }}

    /* Texto centrado debajo del círculo */
    .owner-label {{
        font-size: 12px;
        font-weight: 500;
        margin-top: 2px;
        white-space: nowrap;
    }}

    /* Ocultar botones de navegación nativos si fuera necesario y ajustar tabs */
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

# 1. Inyección del Logo de la empresa
st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- NAVEGACIÓN INFERIOR ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    st.write("### Potential Customers")
    
    # Creamos 4 columnas para las historias
    cols = st.columns(4)
    
    # Datos de ejemplo (Luego esto vendrá de tu base de datos)
    stories = [
        {"name": "Owner", "border": "orange-border"},
        {"name": "Owner", "border": "green-border"},
        {"name": "Owner", "border": "orange-border"},
        {"name": "Owner", "border": "green-border"}
    ]
    
    for i, story in enumerate(stories):
        with cols[i]:
            st.markdown(f"""
                <div class="story-wrapper">
                    <div class="story-circle {story['border']}">
                        <img src="{HOUSE_ICON_URL}" class="house-icon">
                    </div>
                    <div class="owner-label">{story['name']}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()
    
    st.write("### Feed")
    # Video del feed (reemplazar link por el real de tu avatar de IA después)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4") 
    st.write("**Storm Intel:** Hail activity detected in your area. Check potential claims below.")

with tab_messages:
    st.write("### Messages")
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Hope you're doing today!")

with tab_profile:
    st.write("### Profile")
    st.write("**Account Type:** Storm Restoration Professional")
    st.write("**Status:** Active ✅")
