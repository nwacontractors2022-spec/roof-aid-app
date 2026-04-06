import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Roof-Aid Tech", layout="centered")

# --- RUTAS DE ARCHIVOS ---
LOGO_URL = "Gemini_Generated_Image_i6ft8ji6ft8ji6ft.png"
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS PARA EL LOOK DE INSTAGRAM (AZUL REY) ---
st.markdown(f"""
    <style>
    /* Fondo Azul Rey Total */
    .stApp {{
        background-color: #0047AB !important;
        color: white;
    }}
    
    /* Cabecera Fija con Logo Central */
    .ig-header {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 80px;
        background-color: #0047AB;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        border-bottom: 1px solid rgba(255,255,255,0.2);
    }}
    
    .main-logo {{
        height: 55px;
        width: auto;
    }}
    
    /* Espaciado para que el contenido no quede bajo el logo */
    .main-content {{
        margin-top: 90px;
    }}

    /* Contenedor de Stories */
    .story-scroll-container {{
        display: flex;
        flex-direction: row;
        overflow-x: auto;
        gap: 25px;
        padding: 15px 5px;
        scrollbar-width: none;
    }}
    .story-scroll-container::-webkit-scrollbar {{ display: none; }}

    .story-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        min-width: 90px;
    }}

    /* Círculos 30% más grandes */
    .story-circle {{
        width: 85px;
        height: 85px;
        border-radius: 50%;
        background-color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 4px solid white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }}

    /* Bordes de estado */
    .border-appointment {{ border-color: #28A745 !important; }}
    .border-followup {{ border-color: #FF8C00 !important; }}

    .house-icon-img {{
        width: 50px;
        height: 50px;
    }}

    /* Nombre Owner centrado debajo */
    .owner-label {{
        font-size: 13px;
        color: white !important;
        margin-top: 10px;
        text-align: center;
        font-weight: 600;
        width: 100%;
    }}

    /* Tabs Inferiores */
    .stTabs [data-baseweb="tab-list"] {{
        position: fixed;
        bottom: 0;
        background-color: #003380;
        width: 100%;
        z-index: 1000;
        justify-content: center;
        border-top: 1px solid rgba(255,255,255,0.1);
    }}
    
    /* Forzar color de texto en Tabs */
    button[data-baseweb="tab"] p {{
        color: white !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# 2. Header con Logo
st.markdown(f'<div class="ig-header"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# 3. Contenedor de contenido
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    st.markdown("<h3 style='color:white;'>Potential Customers</h3>", unsafe_allow_html=True)
    
    # Datos de ejemplo
    customers = [
        {"id": 1, "type": "appointment"},
        {"id": 2, "type": "appointment"},
        {"id": 3, "type": "follow_up"},
        {"id": 4, "type": "follow_up"},
        {"id": 5, "type": "follow_up"},
    ]

    # Construcción robusta del HTML de Stories
    stories_html = '<div class="story-scroll-container">'
    for person in customers:
        border_class = "border-appointment" if person['type'] == "appointment" else "border-followup"
        stories_html += f'''
            <div class="story-item">
                <div class="story-circle {border_class}">
                    <img src="{HOUSE_ICON_URL}" class="house-icon-img">
                </div>
                <p class="owner-label">Owner</p>
            </div>
        '''
    stories_html += '</div>'
    
    # Renderizado final
    st.markdown(stories_html, unsafe_allow_html=True)

    st.markdown("<hr style='opacity:0.2;'>", unsafe_allow_html=True)
    
    # Sección Feed
    st.markdown("<h3 style='color:white;'>Feed</h3>", unsafe_allow_html=True)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.write("**Storm Intel:** Hail activity detected in NWA.")

with tab_messages:
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Ready to claim some leads?")

st.markdown('</div>', unsafe_allow_html=True)
