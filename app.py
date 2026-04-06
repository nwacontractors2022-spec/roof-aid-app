import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

# 1. Configuración de página
st.set_page_config(page_title="Roof-Aid Tech", layout="centered")

# --- CONEXIÓN A GOOGLE SHEETS ---
@st.cache_data(ttl=300)
def load_data(url):
    try:
        csv_url = url.replace("/edit#gid=", "/export?format=csv&gid=")
        return pd.read_csv(csv_url)
    except:
        return pd.DataFrame()

# Cargamos datos de clientes
try:
    sheet_url = st.secrets["gsheet_url"]
    df = load_data(sheet_url)
    customers = df.to_dict('records')
except:
    customers = []

# --- CONFIGURACIÓN VISUAL (Azul Rey) ---
LOGO_URL = "https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/Gemini_Generated_Image_i6ft8ji6ft8ji6ft.png"
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

st.markdown(f"""
    <style>
    .stApp {{ background-color: #0047AB !important; color: white; }}
    .ig-header {{ display: flex; justify-content: center; padding: 15px 0; background-color: #0047AB; border-bottom: 1px solid rgba(255,255,255,0.1); }}
    .main-logo {{ height: 80px; width: auto; }}
    .stTabs [data-baseweb="tab-list"] {{ position: fixed; bottom: 0; background-color: #003380; width: 100%; z-index: 1000; justify-content: center; padding-bottom: 10px; }}
    button[data-baseweb="tab"] p {{ color: white !important; font-weight: bold; }}
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<div class="ig-header"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    # SECCIÓN: Potential Customers (Historias)
    st.markdown("<h4 style='margin-left: 10px;'>Potential Customers</h4>", unsafe_allow_html=True)
    if customers:
        stories_html = ""
        for p in customers:
            color = "#28A745" if str(p.get('type', '')).lower() == "appointment" else "#FF8C00"
            full_name = f"{p.get('nombre', '')} {p.get('apellido', '')}".strip()
            stories_html += f'''
                <div style="display: flex; flex-direction: column; align-items: center; min-width: 100px;">
                    <div style="width: 85px; height: 85px; border-radius: 50%; background: white; display: flex; justify-content: center; align-items: center; border: 4px solid {color}; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
                        <img src="{HOUSE_ICON_URL}" style="width: 55px; height: 55px;">
                    </div>
                    <div style="font-size: 11px; color: white; margin-top: 8px; font-weight: 600; text-align: center; width: 95px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                        {full_name if full_name else 'Owner'}
                    </div>
                </div>
            '''
        components.html(f'<div style="display: flex; gap: 15px; overflow-x: auto; padding: 10px; scrollbar-width: none;">{stories_html}</div>', height=165)

    st.markdown("<hr style='opacity:0.2; margin: 10px 0;'>", unsafe_allow_html=True)
    
    # SECCIÓN: Feed Dinámico (Content Media)
    st.markdown("<h4 style='margin-left: 10px;'>Roofing Feed</h4>", unsafe_allow_html=True)
    
    # Ruta local a la carpeta
    MEDIA_DIR = "content media"
    
    if os.path.exists(MEDIA_DIR):
        # Listamos archivos omitiendo el ancla 'keephub'
        files = sorted([f for f in os.listdir(MEDIA_DIR) if f != "keephub"])
        
        if files:
            for file in files:
                file_path = os.path.join(MEDIA_DIR, file)
                # Mostramos videos (.mov o .mp4)
                if file.lower().endswith(('.mp4', '.mov', '.avi')):
                    st.video(file_path)
                    st.markdown(f"<p style='text-align:center; font-size:12px; opacity:0.7;'>{file}</p>", unsafe_allow_html=True)
                # Mostramos imágenes
                elif file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    st.image(file_path, use_column_width=True)
                st.markdown("<hr style='opacity:0.1;'>", unsafe_allow_html=True)
        else:
            st.info("No se encontraron archivos en 'content media'.")
    else:
        st.error(f"No se detectó la carpeta '{MEDIA_DIR}'.")

with tab_messages:
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. hope you're doing today!")

with tab_profile:
    st.subheader("System Status")
    st.write(f"📁 Media Folder: `{MEDIA_DIR}`")
    st.write(f"👥 Leads in Sheet: {len(customers)}")
