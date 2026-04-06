import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de página
st.set_page_config(page_title="Roof-Aid Tech", layout="centered")

# --- RUTAS DE ARCHIVOS (Ruta directa de GitHub) ---
LOGO_URL = "https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/Gemini_Generated_Image_i6ft8ji6ft8ji6ft.png"
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS GLOBAL (AZUL REY Y ESTILO IG) ---
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
        padding: 15px 0;
        width: 100%;
        background-color: #0047AB;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 10px;
    }}
    
    .main-logo {{
        height: 75px; /* Tamaño del logo */
        width: auto;
    }}

    /* Tabs Inferiores Fixed */
    .stTabs [data-baseweb="tab-list"] {{
        position: fixed;
        bottom: 0;
        background-color: #003380;
        width: 100%;
        z-index: 1000;
        justify-content: center;
        border-top: 1px solid rgba(255,255,255,0.1);
        padding-bottom: 5px;
    }}
    
    button[data-baseweb="tab"] p {{
        color: white !important;
        font-weight: bold;
        font-size: 14px;
    }}

    /* Ocultar elementos innecesarios de Streamlit */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# 2. RENDERIZADO DEL LOGO CENTRAL
st.markdown(f'<div class="ig-header"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    st.markdown("<h4 style='color:white; margin-left: 10px;'>Potential Customers</h4>", unsafe_allow_html=True)
    
    # Datos simulados
    customers = [
        {"type": "appointment"},
        {"type": "appointment"},
        {"type": "follow_up"},
        {"type": "follow_up"},
        {"type": "follow_up"}
    ]

    # 3. COMPONENTE DE HISTORIAS (ENCAPSULADO)
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

    components.html(f"""
        <div style="display: flex; flex-direction: row; overflow-x: auto; gap: 20px; padding: 10px; scrollbar-width: none; -ms-overflow-style: none;">
            {stories_content}
        </div>
        <style>
            div::-webkit-scrollbar {{ display: none; }}
            body {{ margin: 0; padding: 0; background-color: transparent; }}
        </style>
    """, height=160)

    st.markdown("<hr style='opacity:0.2; margin: 10px 0;'>", unsafe_allow_html=True)
    
    # 4. SECCIÓN FEED
    st.markdown("<h4 style='color:white; margin-left: 10px;'>Feed</h4>", unsafe_allow_html=True)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.write("**Storm Intel:** Actividad de granizo detectada en el área de NWA. Revisa tus leads.")

with tab_messages:
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Ready to claim some leads?")
