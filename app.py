import streamlit as st

# Configuración de página para móviles
st.set_page_config(page_title="Roof-Aid App", layout="centered")

# URL de tu logo (ya verificado de tus capturas)
LOGO_URL = "https://nwacontractors2022-spec/repo/image_9.png" # Si esta URL cambia, actualízala aquí

# URL del icono de casa genérico (estilo trazo negro)
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS PERSONALIZADO (Look Premium & Colores de Marca) ---
st.markdown(f"""
    <style>
    /* 1. Fondo Azul Metálico y Letras Blancas en toda la App */
    .stApp {{
        background: radial-gradient(circle, #203a5c 0%, #152033 100%);
        color: white;
    }}
    
    /* Forzar color blanco en títulos y subtítulos */
    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}
    
    /* 2. Logotipo en la esquina superior derecha (fixed) */
    .main-logo {{
        position: fixed;
        top: 60px; /* Ajuste para la barra de streamlit */
        right: 15px;
        width: 100px;
        z-index: 999;
    }}
    
    /* 3. Estilo de los círculos de historias (Instagram Style) */
    .story-circle {{
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: 65px;
        height: 65px;
        padding: 3px;
        background-color: white; /* Fondo blanco para que resalte la casa negra */
    }}
    
    /* Bordes dinámicos */
    .orange-border {{ 
        border: 4px solid #F57C00; /* Naranja (Follow-ups) */
        box-shadow: 0 0 10px rgba(245, 124, 0, 0.5);
    }} 
    .green-border {{ 
        border: 4px solid #28A745; /* Verde IG (Appointments) */
        box-shadow: 0 0 10px rgba(40, 167, 69, 0.5);
    }}
    
    /* Icono de la casa dentro del círculo */
    .house-icon {{
        width: 50px;
        margin-top: 5px;
    }}

    /* 4. Ajuste de la navegación inferior (Fondo azul oscuro para integrarse) */
    .stTabs [data-baseweb="tab-list"] {{
        position: fixed;
        bottom: 0;
        background: linear-gradient(180deg, #152033 0%, #101826 100%);
        z-index: 100;
        width: 100%;
        justify-content: center;
        border-top: 1px solid rgba(255,255,255,0.1);
    }}
    
    /* Estilo de los botones de historias */
    .stButton>button {{
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.2);
        background-color: rgba(255,255,255,0.05);
        color: white;
    }}
    .stButton>button:hover {{
        background-color: #F57C00; /* Efecto naranja al pasar */
        border-color: #F57C00;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- INYECCIÓN DEL LOGO ---
# Se inyecta como HTML para posicionarlo en la esquina
st.markdown(f'<img src="{LOGO_URL}" class="main-logo">', unsafe_allow_html=True)

# --- NAVEGACIÓN INFERIOR (Módulos IG) ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

# --- MÓDULO 1: HOME (STORIES & FEED) ---
with tab_home:
    # 1. SECCIÓN STORIES (Renombrada a Potential Customers)
    st.write("### Potential Customers")
    s_col1, s_col2, s_col3, s_col4 = st.columns(4)
    
    # Historias simuladas con la lógica de color solicitada
    with s_col1:
        # Borde Naranja (Follow-up)
        st.markdown(f'<div class="story-circle orange-border"><img src="{HOUSE_ICON_URL}" class="house-icon"></div>', unsafe_allow_html=True)
        st.caption("Portland")
        st.button("Follow", key="f1")

    with s_col2:
        # Borde Verde (Appointment)
        st.markdown(f'<div class="story-circle green-border"><img src="{HOUSE_ICON_URL}" class="house-icon"></div>', unsafe_allow_html=True)
        st.caption("Corpus")
        st.button("Get Appt", key="a1")

    with s_col3:
        # Borde Naranja (Follow-up)
        st.markdown(f'<div class="story-circle orange-border"><img src="{HOUSE_ICON_URL}" class="house-icon"></div>', unsafe_allow_html=True)
        st.caption("Mobile")
        st.button("Follow", key="f2")

    with s_col4:
        # Borde Verde (Appointment)
        st.markdown(f'<div class="story-circle green-border"><img src="{HOUSE_ICON_URL}" class="house-icon"></div>', unsafe_allow_html=True)
        st.caption("Arkansas")
        st.button("Get Appt", key="a2")

    st.divider()

    # 2. SECCIÓN FEED (Renombrada a Feed)
    st.write("### Feed")
    # Video simulado (El conejo de prueba)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4") 
    st.write("**Storm Intel:** Granizo detectado en NWA. 120 reclamos de seguro potenciales.")
    
    # Imagen de Marketing simulada
    st.image("https://via.placeholder.com/600x400/1a1a1a/ffffff?text=Insurance+Restoration+Data", use_container_width=True)

# --- MÓDULO 2: MESSAGES (BUZÓN CENTRAL) ---
with tab_messages:
    st.write("### Communications Center")
    st.info("⚠️ Alerta Especial: Tormenta de granizo en Corpus Christi.")
    st.chat_message("assistant").write("Hola! Soy tu soporte técnico. ¿Tienes dudas con una licencia?")

# --- MÓDULO 3: PROFILE (LICENCIA AUDITABLE) ---
with tab_profile:
    st.write("### Contractor Profile")
    p_col1, p_col2 = st.columns([1, 2])
    with p_col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90)
    with p_col2:
        st.write("#### Roofer Pro ✅")
        st.write("**License:** #TX-99812-RC")
    
    st.divider()
    st.write(f"**Tier:** Premium ($600/mo)")
