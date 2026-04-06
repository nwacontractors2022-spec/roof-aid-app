import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

# 1. Configuración de página
st.set_page_config(page_title="Roof-Aid Tech", layout="centered")

# --- CONEXIÓN A GOOGLE SHEETS ---
@st.cache_data(ttl=60)  # Se actualiza cada minuto para ver cambios rápido
def load_data(url):
    try:
        # Transformamos link de edición a link de exportación directa
        csv_url = url.replace("/edit", "/export?format=csv")
        # Ajuste para Sheets con múltiples pestañas (usa el gid de tu captura)
        if "gid=" in url and "gid=" not in csv_url:
            gid = url.split("gid=")[-1]
            csv_url += f"&gid={gid}"
        
        data = pd.read_csv(csv_url)
        return data
    except Exception as e:
        return pd.DataFrame()

# Intentamos cargar desde Secrets
sheet_url = st.secrets.get("gsheet_url", "")
df = load_data(sheet_url)

if not df.empty:
    customers = df.to_dict('records')
else:
    # Datos de cortesía por si el enlace falla momentáneamente
    customers = [{"First Name": "Check", "Last Name": "Connection", "type": "FOLLOW UP"}]

# --- CONFIGURACIÓN VISUAL (Estilo Instagram Dark) ---
LOGO_URL = "https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/Gemini_Generated_Image_i6ft8ji6ft8ji6ft.png"
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #0047AB !important; color: white; }}
    .ig-header {{ display: flex; justify-content: center; padding: 15px 0; background-color: #0047AB; border-bottom: 1px solid rgba(255,255,255,0.1); }}
    .main-logo {{ height: 80px; width: auto; }}
    .stTabs [data-baseweb="tab-list"] {{ position: fixed; bottom: 0; background-color: #003380; width: 100%; z-index: 1000; justify-content: center; padding-bottom: 10px; }}
    button[data-baseweb="tab"] p {{ color: white !important; font-weight: bold; font-size: 14px; }}
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# Logo de Cabecera
st.markdown(f'<div class="ig-header"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- SISTEMA DE PESTAÑAS (TABS) ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    # SECCIÓN: Potential Customers (Historias Dinámicas)
    st.markdown("<h4 style='margin-left: 10px; margin-top: 10px;'>Potential Customers</h4>", unsafe_allow_html=True)
    
    stories_html = ""
    for p in customers:
        # Lógica de color: Verde para Citas, Naranja para Follow Ups
        status_type = str(p.get('type', '')).upper()
        border_color = "#28A745" if "APPOINTMENT" in status_type else "#FF8C00"
        
        # Nombre y Apellido desde tu Excel
        f_name = p.get('First Name', 'Owner')
        l_name = p.get('Last Name', '')
        
        stories_html += f'''
            <div style="display: flex; flex-direction: column; align-items: center; min-width: 95px;">
                <div style="width: 75px; height: 75px; border-radius: 50%; background: white; display: flex; justify-content: center; align-items: center; border: 4px solid {border_color}; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                    <img src="{HOUSE_ICON_URL}" style="width: 45px; height: 45px;">
                </div>
                <div style="font-size: 10px; color: white; margin-top: 8px; font-weight: 600; text-align: center; width: 90px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; font-family: sans-serif;">
                    {f_name}<br>{l_name}
                </div>
            </div>
        '''

    # Contenedor de historias con scroll horizontal
    components.html(f'''
        <div style="display: flex; gap: 12px; overflow-x: auto; padding: 5px 10px; scrollbar-width: none; -ms-overflow-style: none;">
            {stories_html}
        </div>
        <style>div::-webkit-scrollbar {{ display: none; }} body {{ margin: 0; background: transparent; }}</style>
    ''', height=140)

    st.markdown("<hr style='opacity:0.2; margin: 5px 0;'>", unsafe_allow_html=True)
    
    # SECCIÓN: Feed (Tus Videos e Imágenes)
    st.markdown("<h4 style='margin-left: 10px;'>Roofing Feed</h4>", unsafe_allow_html=True)
    
    MEDIA_DIR = "content media"
    if os.path.exists(MEDIA_DIR):
        # Listamos archivos omitiendo el archivo oculto keephub
        files = sorted([f for f in os.listdir(MEDIA_DIR) if f != "keephub"], reverse=True)
        
        if files:
            for file in files:
                file_path = os.path.join(MEDIA_DIR, file)
                if file.lower().endswith(('.mp4', '.mov')):
                    st.video(file_path)
                elif file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    st.image(file_path, use_column_width=True)
                st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
        else:
            st.info("La carpeta 'content media' está vacía.")
    else:
        st.error(f"Error: No se encontró la carpeta '{MEDIA_DIR}'")

with tab_messages:
    # Saludo de Riley configurado
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. hope you're doing today!")
    st.write("---")
    st.write("📩 *Lead updates will appear here.*")

with tab_profile:
    st.subheader("System Status")
    st.write(f"📊 **Total Leads:** {len(customers)}")
    st.write(f"📁 **Media Folder:** {MEDIA_DIR}")
    if st.button("Recargar Datos"):
        st.cache_data.clear()
        st.rerun()
