import streamlit as st

# Configuración de página
st.set_page_config(page_title="Roof-Aid App", layout="centered")

# --- CONFIGURACIÓN DE RUTAS ---
LOGO_URL = "https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/WhatsApp%20Image%202026-02-21%20at%209.25.44%20PM.jpeg".replace(" ", "%20")
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS PARA EL CARRUSEL TIPO IG ---
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

    /* CONTENEDOR CARRUSEL HORIZONTAL */
    .story-container {{
        display: flex;
        overflow-x: auto;
        padding: 10px 0;
        gap: 20px;
        white-space: nowrap;
        scrollbar-width: none; /* Ocultar scroll en Firefox */
    }}
    .story-container::-webkit-scrollbar {{ display: none; }} /* Ocultar scroll en Chrome/Safari */

    .story-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        min-width: 80px;
    }}

    .story-circle {{
        border-radius: 50%;
        width: 70px;
        height: 70px;
        padding: 3px;
        background-color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }}
    
    .orange-border {{ border: 4px solid #F57C00; }} 
    .green-border {{ border: 4px solid #28A745; }}
    
    .house-icon {{ width: 40px; }}
    .owner-label {{ font-size: 12px; margin-top: 5px; font-weight: bold; color: white; }}

    /* Estilo del Formulario / Modal */
    .data-card {{
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.2);
        margin-top: 10px;
    }}

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

# 1. Mostrar Logo
st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    st.write("### Potential Customers")
    
    # DATOS SIMULADOS (Estos vendrán de tu Google Sheet)
    # Priority 1: Appointment (Green), Priority 2: Follow-up (Orange)
    raw_data = [
        {"id": 1, "type": "appointment", "name": "John Doe", "address": "123 Sky Lane", "phone": "555-0101", "sqft": "2,400"},
        {"id": 2, "type": "follow_up", "name": "Jane Smith", "address": "456 Oak St", "phone": "555-0202", "sqft": "1,800"},
        {"id": 3, "type": "appointment", "name": "Robert Ross", "address": "789 Pine Rd", "phone": "555-0303", "sqft": "3,100"},
        {"id": 4, "type": "follow_up", "name": "Mike Myers", "address": "101 Lake Dr", "phone": "555-0404", "sqft": "2,000"},
        {"id": 5, "type": "follow_up", "name": "Sarah Connor", "address": "202 Term St", "phone": "555-0505", "sqft": "2,200"},
    ]

    # Ordenar por prioridad: Appointments primero
    sorted_data = sorted(raw_data, key=lambda x: x['type'] != 'appointment')

    # RENDERIZADO DEL CARRUSEL (HTML/CSS)
    story_html = '<div class="story-container">'
    for person in sorted_data:
        border_class = "green-border" if person['type'] == "appointment" else "orange-border"
        story_html += f'''
            <div class="story-item">
                <div class="story-circle {border_class}">
                    <img src="{HOUSE_ICON_URL}" class="house-icon">
                </div>
                <div class="owner-label">Owner</div>
            </div>
        '''
    story_html += '</div>'
    st.markdown(story_html, unsafe_allow_html=True)

    # LÓGICA DE INTERACCIÓN (Dándole clic al Owner para ver detalles)
    st.write("---")
    selected_owner = st.selectbox("Select Owner to View Details", [p['name'] for p in sorted_data], index=0)
    
    # Buscar datos del dueño seleccionado
    owner_info = next(item for item in sorted_data if item["name"] == selected_owner)
    
    with st.container():
        st.markdown(f"""
            <div class="data-card">
                <h4>📋 Property Details</h4>
                <p><b>Name:</b> {owner_info['name']}</p>
                <p><b>Address:</b> {owner_info['address']}</p>
                <p><b>Phone:</b> {owner_info['phone']}</p>
                <p><b>Roof Size:</b> {owner_info['sqft']} SqFt</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Botón GET con enlace de correo electrónico
        subject = f"GET LEAD: {owner_info['name']}"
        body = f"I want to claim this lead:%0D%0AOwner: {owner_info['name']}%0D%0AAddress: {owner_info['address']}%0D%0ASize: {owner_info['sqft']} SqFt"
        mail_link = f"mailto:admin@roofaid.com?subject={subject}&body={body}"
        
        st.markdown(f'<a href="{mail_link}" target="_blank" style="text-decoration:none;"><div style="background-color:#28A745; color:white; padding:10px; text-align:center; border-radius:10px; font-weight:bold; margin-top:10px;">GET LEAD</div></a>', unsafe_allow_html=True)

    st.divider()
    st.write("### Feed")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")

with tab_messages:
    st.write("### Messages")
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Ready to claim some roofs?")
