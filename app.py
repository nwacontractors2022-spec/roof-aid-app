import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

# 1. Configuración de la aplicación
st.set_page_config(page_title="Roof-Aid Tech", layout="centered")

# --- CARGA DE DATOS ---
@st.cache_data(ttl=60)
def load_data(url):
    try:
        data = pd.read_csv(url)
        data.columns = data.columns.str.strip()
        return data
    except:
        return pd.DataFrame()

sheet_url = st.secrets.get("gsheet_url", "")
df = load_data(sheet_url)
customers = df.to_dict('records') if not df.empty else []

# --- ESTADO DE NAVEGACIÓN ---
if 'view' not in st.session_state:
    st.session_state.view = "feed"
if 'selected_idx' not in st.session_state:
    st.session_state.selected_idx = None

def show_customer(idx):
    st.session_state.view = "preview"
    st.session_state.selected_idx = idx

def show_feed():
    st.session_state.view = "feed"
    st.session_state.selected_idx = None

# --- DISEÑO UI (CSS) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0047AB !important; color: white; }}
    .ig-header {{ display: flex; justify-content: center; padding: 15px 0; background-color: #0047AB; border-bottom: 1px solid rgba(255,255,255,0.1); }}
    .main-logo {{ height: 70px; width: auto; }}
    
    /* Estilo de la Tarjeta de Vista Previa */
    .preview-container {{
        background: white;
        color: #1e1e1e;
        border-radius: 20px;
        padding: 25px;
        margin-top: 10px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    }}
    .client-name {{ font-size: 28px; font-weight: bold; color: #0047AB; margin-bottom: 5px; }}
    .status-tag {{
        display: inline-block;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 20px;
    }}
    .info-row {{ margin-bottom: 15px; border-bottom: 1px solid #f0f0f0; padding-bottom: 10px; }}
    .info-label {{ font-size: 12px; color: #666; text-transform: uppercase; }}
    .info-value {{ font-size: 17px; font-weight: 500; color: #333; }}
    
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# Encabezado con Logo
st.markdown(f'<div class="ig-header"><img src="https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/Gemini_Generated_Image_i6ft8ji6ft8ji6ft.png" class="main-logo"></div>', unsafe_allow_html=True)

# --- VISTA: PREVIA DEL CLIENTE ---
if st.session_state.view == "preview" and st.session_state.selected_idx is not None:
    p = customers[st.session_state.selected_idx]
    
    if st.button("⬅️ Volver al Feed"):
        show_feed()
        st.rerun()

    status = str(p.get('type', 'FOLLOW UP')).upper()
    bg_color = "#D4EDDA" if "APPOINTMENT" in status else "#FFF3CD"
    txt_color = "#155724" if "APPOINTMENT" in status else "#856404"

    st.markdown(f"""
        <div class="preview-container">
            <div class="client-name">{p.get('First Name', '')} {p.get('Last Name', '')}</div>
            <div class="status-tag" style="background-color: {bg_color}; color: {txt_color};">
                ● {status}
            </div>
            
            <div class="info-row">
                <div class="info-label">Teléfono</div>
                <div class="info-value">📱 {p.get('Phone Number', 'Sin número')}</div>
            </div>
            
            <div class="info-row">
                <div class="info-label">Dirección</div>
                <div class="info-value">🏠 {p.get('Full Address', 'N/A')}</div>
            </div>
            
            <div class="info-row">
                <div class="info-label">Ubicación</div>
                <div class="info-value">📍 {p.get('City', '')}, {p.get('State', '')} {p.get('Zip Code', '')}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Botón de llamada real
    tel = str(p.get('Phone Number', '')).replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    st.link_button(f"📞 LLAMAR A {p.get('First Name', '').upper()}", f"tel:{tel}", use_container_width=True)

# --- VISTA: FEED PRINCIPAL ---
else:
    tab_home, tab_msg, tab_prof = st.tabs(["🏠 Feed", "📩 Mensajes", "👤 Perfil"])
    
    with tab_home:
        st.markdown("<h4 style='margin-top:10px;'>Potential Customers</h4>", unsafe_allow_html=True)
        
        # Carrusel de Historias Clickeables
        if customers:
            # Creamos una fila horizontal con scroll usando HTML/JS
            cols = st.columns(len(customers))
            for i, p in enumerate(customers):
                with cols[i]:
                    status = str(p.get('type', '')).upper()
                    color = "#28A745" if "APPOINTMENT" in status else "#FF8C00"
                    
                    # Botón invisible sobre el círculo para detectar el click
                    if st.button(f"{p.get('First Name')}", key=f"user_{i}"):
                        show_customer(i)
                        st.rerun()
                    
                    st.markdown(f'''
                        <div style="text-align: center; margin-top: -10px;">
                            <div style="width: 55px; height: 55px; border-radius: 50%; border: 3px solid {color}; background: white; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
                                <img src="https://cdn-icons-png.flaticon.com/512/619/619153.png" style="width: 30px;">
                            </div>
                        </div>
                    ''', unsafe_allow_html=True)

        st.markdown("<hr style='opacity:0.2;'>", unsafe_allow_html=True)
        
        # Roofing Feed
        st.markdown("<h4>Roofing Feed</h4>", unsafe_allow_html=True)
        MEDIA_DIR = "content media"
        if os.path.exists(MEDIA_DIR):
            files = sorted([f for f in os.listdir(MEDIA_DIR) if f != "keephub"], reverse=True)
            for file in files:
                file_path = os.path.join(MEDIA_DIR, file)
                if file.lower().endswith(('.mp4', '.mov')):
                    st.video(file_path)
                elif file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    st.image(file_path)

    with tab_msg:
        st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Selecciona un cliente arriba para ver sus detalles.")

    with tab_prof:
        st.subheader("Configuración")
        if st.button("🔄 Sincronizar con Google Sheets"):
            st.cache_data.clear()
            st.rerun()
