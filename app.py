import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de página
st.set_page_config(page_title="Roof-Aid Tech", layout="centered")

# --- RUTAS DE ARCHIVOS ---
# Asegúrate de que el nombre coincida exactamente en tu repositorio de GitHub
LOGO_URL = "Gemini_Generated_Image_i6ft8ji6ft8ji6ft.png"
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS GLOBAL (AZUL REY Y ESTRUCTURA) ---
st.markdown(f"""
    <style>
    /* Fondo Azul Rey en toda la App */
    .stApp {{
        background-color: #0047AB !important;
        color: white;
    }}
    
    /* Logo Central Superior */
    .ig-header {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px 0;
        width: 100%;
        background-color: #0047AB;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}
    
    .main-logo {{
        height: 70px;
        width: auto;
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
    
    button[data-baseweb="tab"] p {{
        color: white !important;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# 2. RENDERIZADO DEL LOGO CENTRAL
st.markdown(f'<div class="ig-header"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    st.markdown("<h3 style='color:white; margin-top:10px;'>Potential Customers</h3>", unsafe_allow_html=True)
    
    # Simulación de datos de clientes
    customers = [
        {"type": "appointment"},
        {"type": "appointment"},
        {"type": "follow_up"},
        {"type": "follow_up"},
        {"type": "follow_up"}
    ]

    # 3. COMPONENTE DE HISTORIAS (ENCAPSULADO PARA EVITAR ERROR DE TEXTO)
    stories_content = ""
    for person in customers:
        border_color = "#28A745" if person['type'] == "appointment" else "#FF8C00"
        stories_content += f'''
            <div style="display: flex; flex-direction: column; align-items: center; min-width: 95px;">
                <div style="width: 85px; height: 85px; border-radius: 50%; background: white; display: flex; justify-content: center; align-items: center; border: 4px solid {border_color}; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                    <img src="{HOUSE_ICON_URL}" style="width: 50px; height: 50px;">
                </div>
                <div style="font-size: 13px; color: white; margin-top: 10px; font-weight: 600; font-family: sans-serif; text-align: center;">Owner</div>
            </div>
        '''

    # Inyectamos el HTML de las historias de forma aislada
    components.html(f"""
        <div style="display: flex; flex-direction: row; overflow-x: auto; gap: 20px; padding: 10px; scrollbar-width: none;">
            {stories_content}
        </div>
        <style>
            div::-webkit-scrollbar {{ display: none; }}
        </style>
    """, height=160)

    st.markdown("<hr style='opacity:0.2;'>", unsafe_allow_html=True)
    
    # 4. SECCIÓN FEED
    st.markdown("<h3 style='color:white;'>Feed</h3>", unsafe_allow_html=True)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.write("**Storm Intel:** Actividad de granizo detectada en el área de NWA. Revisa tus leads.")

with tab_messages:
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Ready to claim some leads?")
