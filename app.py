import streamlit as st

# Configuración de página
st.set_page_config(page_title="Roof-Aid App", layout="centered")

# --- RUTAS DE IMÁGENES ---
LOGO_URL = "https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/WhatsApp%20Image%202026-02-21%20at%209.25.44%20PM.jpeg".replace(" ", "%20")
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS MEJORADO ---
st.markdown(f"""
    <style>
    .stApp {{
        background: radial-gradient(circle, #203a5c 0%, #152033 100%);
        color: white;
    }}
    
    /* Logo arriba a la derecha */
    .logo-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: -70px;
        margin-bottom: 20px;
    }}
    .main-logo {{ width: 100px; border-radius: 8px; }}

    /* Estilo de Historias */
    .story-button {{
        background: none;
        border: none;
        padding: 0;
        cursor: pointer;
    }}

    .owner-label {{ 
        font-size: 12px; 
        font-weight: bold; 
        text-align: center;
        margin-top: 5px;
    }}

    /* Card de detalles */
    .data-card {{
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1);
        margin-top: 20px;
    }}

    /* Tabs inferiores */
    .stTabs [data-baseweb="tab-list"] {{
        position: fixed;
        bottom: 0;
        background: #152033;
        z-index: 100;
        width: 100%;
        justify-content: center;
    }}
    </style>
    """, unsafe_allow_html=True)

# 1. Logo
st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- BASE DE DATOS TEMPORAL (Priorizando Appointments) ---
if 'data' not in st.session_state:
    raw_data = [
        {"id": 1, "type": "appointment", "name": "John Doe", "address": "123 Sky Lane", "phone": "555-0101", "sqft": "2,400"},
        {"id": 3, "type": "appointment", "name": "Robert Ross", "address": "789 Pine Rd", "phone": "555-0303", "sqft": "3,100"},
        {"id": 2, "type": "follow_up", "name": "Jane Smith", "address": "456 Oak St", "phone": "555-0202", "sqft": "1,800"},
        {"id": 4, "type": "follow_up", "name": "Mike Myers", "address": "101 Lake Dr", "phone": "555-0404", "sqft": "2,000"},
        {"id": 5, "type": "follow_up", "name": "Sarah Connor", "address": "202 Term St", "phone": "555-0505", "sqft": "2,200"},
    ]
    # Ordenar: Appointments (verde) siempre primero
    st.session_state.data = sorted(raw_data, key=lambda x: x['type'] != 'appointment')

if 'selected_owner' not in st.session_state:
    st.session_state.selected_owner = st.session_state.data[0]

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    st.write("### Potential Customers")
    
    # Carrusel de Historias usando columnas (evita el error de texto HTML)
    cols = st.columns(len(st.session_state.data))
    
    for i, person in enumerate(st.session_state.data):
        with cols[i]:
            # El borde cambia según el tipo
            border_color = "#28A745" if person['type'] == "appointment" else "#F57C00"
            
            # Botón con imagen
            if st.button("🏠", key=f"btn_{person['id']}", help=f"Click to view {person['name']}"):
                st.session_state.selected_owner = person
            
            st.markdown(f'<div class="owner-label" style="color:{border_color}">Owner</div>', unsafe_allow_html=True)

    # --- MOSTRAR DETALLES SEGÚN CLICK ---
    owner = st.session_state.selected_owner
    
    st.markdown(f"""
        <div class="data-card">
            <h3 style="margin-top:0;">📋 Property Details</h3>
            <hr style="opacity:0.2">
            <p style="font-size:18px;"><b>Owner:</b> {owner['name']}</p>
            <p><b>Address:</b> {owner['address']}</p>
            <p><b>Phone:</b> {owner['phone']}</p>
            <p><b>Roof Size:</b> {owner['sqft']} SqFt</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Botón GET dinámico
    subject = f"CLAIM LEAD: {owner['name']}"
    body = f"I am interested in claiming this lead:%0D%0AName: {owner['name']}%0D%0AAddress: {owner['address']}%0D%0ASize: {owner['sqft']} SqFt"
    mail_url = f"mailto:admin@roofaid.com?subject={subject}&body={body}"
    
    st.markdown(f"""
        <a href="{mail_url}" target="_blank" style="text-decoration:none;">
            <div style="background-color:#28A745; color:white; padding:15px; text-align:center; border-radius:10px; font-weight:bold; margin-top:15px; box-shadow: 0 4px 15px rgba(40,167,69,0.3);">
                GET LEAD
            </div>
        </a>
    """, unsafe_allow_html=True)

    st.divider()
    st.write("### Feed")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with tab_messages:
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Hope you're doing today!")
