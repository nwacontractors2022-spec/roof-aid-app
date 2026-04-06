import streamlit as st

# Configuración de página para móviles
st.set_page_config(page_title="Roof-Aid Tech", layout="centered")

# --- RUTAS DE ARCHIVOS ---
# Usando el nombre exacto que mencionaste
LOGO_URL = "Gemini_Generated_Image_i6ft8ji6ft8ji6ft.png"
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS PARA EL LOOK DE INSTAGRAM ---
st.markdown(f"""
    <style>
    /* 1. Fondo Azul Rey Predominante */
    .stApp {{
        background: #0047AB; /* Azul Rey */
        color: white;
    }}
    
    /* 2. Cabecera Fija del Logo Central (Tipo IG) */
    .ig-header {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 110px;
        background: #0047AB;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}
    
    .main-logo {{
        height: 75px; 
        width: auto;
    }}
    
    /* 3. Espaciado del contenido para el header fijo */
    .stMainBlockContainer {{
        padding-top: 130px !important;
    }}

    /* 4. SECCIÓN STORIES (Circulares y 30% más grandes) */
    .story-scroll-container {{
        display: flex;
        overflow-x: auto;
        gap: 25px;
        padding: 10px 0px 20px 0px;
        scrollbar-width: none;
        justify-content: flex-start;
    }}
    .story-scroll-container::-webkit-scrollbar {{ display: none; }}

    .story-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        min-width: 95px; /* Ajuste para el tamaño 30% mayor */
    }}

    /* Círculo de historia (85px es ~30% más que el estándar de 65px) */
    .story-circle {{
        width: 85px;
        height: 85px;
        border-radius: 50%;
        background: white;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        border: 3px solid #ffffff;
    }}

    /* Bordes de color según tipo (Vivo) */
    .border-appointment {{ border: 4px solid #28A745 !important; }} /* Verde */
    .border-followup {{ border: 4px solid #FF8C00 !important; }}    /* Naranja */

    .house-icon-img {{
        width: 50px;
        height: 50px;
    }}

    /* Texto Owner centrado debajo del círculo */
    .owner-label {{
        font-size: 13px;
        font-weight: 500;
        color: white;
        margin-top: 8px;
        text-align: center;
        width: 100%;
    }}

    /* 5. Tabs Inferiores Fijos */
    .stTabs [data-baseweb="tab-list"] {{
        position: fixed;
        bottom: 0;
        background: #003380;
        z-index: 100;
        width: 100%;
        justify-content: center;
        padding-bottom: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 1. Cabecera con Logo Central
st.markdown(f'<div class="ig-header"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- BASE DE DATOS TEMPORAL ---
customers = [
    {"id": 1, "type": "appointment", "name": "John Doe"},
    {"id": 2, "type": "appointment", "name": "Robert Ross"},
    {"id": 3, "type": "follow_up", "name": "Jane Smith"},
    {"id": 4, "type": "follow_up", "name": "Mike Myers"},
    {"id": 5, "type": "follow_up", "name": "Sarah Connor"},
]

# Ordenar prioridad
sorted_customers = sorted(customers, key=lambda x: x['type'] != 'appointment')

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    # Renderizado de Historias Estilo Instagram
    st.write("### Potential Customers")
    
    # Construcción del HTML de stories
    stories_html = '<div class="story-scroll-container">'
    for person in sorted_customers:
        border_class = "border-appointment" if person['type'] == "appointment" else "border-followup"
        stories_html += f'''
            <div class="story-item">
                <div class="story-circle {border_class}">
                    <img src="{HOUSE_ICON_URL}" class="house-icon-img">
                </div>
                <div class="owner-label">Owner</div>
            </div>
        '''
    stories_html += '</div>'
    
    st.markdown(stories_html, unsafe_allow_html=True)

    st.divider()
    
    # Feed de Video
    st.write("### Feed")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.write("**Storm Intel:** Hail activity detected in NWA. Check potential claims.")

with tab_messages:
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Ready to claim some leads?")
