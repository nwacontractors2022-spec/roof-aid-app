import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

# 1. Configuración de la aplicación (Modo Móvil)
st.set_page_config(page_title="Roof-Aid Tech", layout="centered")

# --- CARGA DE DATOS DESDE GOOGLE SHEETS ---
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

# --- LÓGICA DE NAVEGACIÓN ---
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

# --- DISEÑO UI PERSONALIZADO (CSS) ---
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0047AB !important; color: white; }}
    .ig-header {{ display: flex; justify-content: center; padding: 15px 0; background-color: #0047AB; border-bottom: 1px solid rgba(255,255,255,0.1); }}
    .main-logo {{ height: 70px; width: auto; }}
    
    /* Estilo de la Tarjeta de Vista Previa */
    .preview-card {{
        background: white;
        color: #1e1e1e;
        border-radius: 20px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    .client-title {{ font-size: 26px; font-weight: bold; color: #0047AB; margin-bottom: 5px; }}
    .data-label {{ font-size: 11px; color: #888; text-transform: uppercase; margin-top: 10px; }}
    .data-value {{ font-size: 16px; color: #333; font-weight: 500; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
    
    #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# Encabezado con Logo
st.markdown(f'<div class="ig-header"><img src="https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/Gemini_Generated_Image_i6ft8ji6ft8ji6ft.png" class="main-logo"></div>', unsafe_allow_html=True)

# --- VISTA: DETALLE DEL CLIENTE (LA LÓGICA) ---
if st.session_state.view == "preview" and st.session_state.selected_idx is not None:
    p = customers[st.session_state.selected_idx]
    
    if st.button("⬅️ Back to Feed"):
        show_feed()
        st.rerun()

    st.markdown(f"""
        <div class="preview-card">
            <div class="client-title">{p.get('First Name', '')} {p.get('Last Name', '')}</div>
            <div style="color: #FF8C00; font-weight: bold; font-size: 13px; margin-bottom: 20px;">● {p.get('type', 'FOLLOW UP')}</div>
            
            <div class="data-label">Phone Number</div>
            <div class="data-value">📱 {p.get('Phone Number', 'N/A')}</div>
            
            <div class="data-label">Full Address</div>
            <div class="data-value">🏠 {p.get('Full Address', 'N/A')}</div>
            
            <div class="data-label">City & Zip</div>
            <div class="data-value">📍 {p.get('City', '')}, {p.get('State', '')} {p.get('Zip Code', '')}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Botón de acción real
    st.link_button(f"📞 CALL {p.get('First Name', '').upper()}", f"tel:{p.get('Phone Number', '')}", use_container_width=True)

# --- VISTA: DISEÑO DEL FEED PRINCIPAL ---
else:
    tab_home, tab_msg, tab_prof = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])
    
    with tab_home:
        st.markdown("<h4 style='margin: 10px 0 0 10px;'>Potential Customers</h4>", unsafe_allow_html=True)
        
        # DISEÑO: Círculos de Historias (Visual solamente para evitar errores de alineación)
        stories_html = ""
        for p in customers:
            status = str(p.get('type', '')).upper()
            color = "#28A745" if "APPOINTMENT" in status else "#FF8C00"
            name = p.get('First Name', 'Owner')
            
            stories_html += f'''
                <div style="display: inline-block; text-align: center; margin-right: 18px;">
                    <div style="width: 60px; height: 60px; border-radius: 50%; border: 3px solid {color}; background: white; display: flex; align-items: center; justify-content: center; margin-bottom: 5px;">
                        <img src="https://cdn-icons-png.flaticon.com/512/619/619153.png" style="width: 32px;">
                    </div>
                    <div style="font-size: 10px; font-weight: bold; width: 65px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{name}</div>
                </div>
            '''
        
        # Contenedor con Scroll Horizontal
        components.html(f'''
            <div style="display: flex; overflow-x: auto; padding: 10px; white-space: nowrap; scrollbar-width: none; -ms-overflow-style: none;">
                {stories_html}
            </div>
            <style>div::-webkit-scrollbar {{ display: none; }} body {{ margin:0; }}</style>
        ''', height=110)

        # LÓGICA: Selector para entrar a la vista previa
        st.markdown("<p style='font-size: 12px; margin-left: 10px; opacity: 0.7;'>Select a customer to view details:</p>", unsafe_allow_html=True)
        nombres = [f"{c.get('First Name')} {c.get('Last Name')}" for c in customers]
        seleccion = st.selectbox("Search leads:", ["--- Select ---"] + nombres, label_visibility="collapsed")
        
        if seleccion != "--- Select ---":
            idx = next(i for i, c in enumerate(customers) if f"{c.get('First Name')} {c.get('Last Name')}" == seleccion)
            show_customer(idx)
            st.rerun()

        st.markdown("<hr style='opacity:0.2; margin: 15px 0;'>", unsafe_allow_html=True)
        
        # SECCIÓN: Roofing Feed
        st.markdown("<h4 style='margin-left: 10px;'>Roofing Feed</h4>", unsafe_allow_html=True)
        MEDIA_DIR = "content media"
        if os.path.exists(MEDIA_DIR):
            files = sorted([f for f in os.listdir(MEDIA_DIR) if f != "keephub"], reverse=True)
            for file in files:
                file_path = os.path.join(MEDIA_DIR, file)
                if file.lower().endswith(('.mp4', '.mov')):
                    st.video(file_path)
                elif file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    st.image(file_path, use_column_width=True)

    with tab_msg:
        st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Select a customer from the list to see their info!")

    with tab_prof:
        st.subheader("App Configuration")
        if st.button("🔄 Sync with Google Sheets"):
            st.cache_data.clear()
            st.rerun()
