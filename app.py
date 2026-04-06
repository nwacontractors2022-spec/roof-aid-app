import streamlit as st

# Configuración de página
st.set_page_config(page_title="Roof-Aid App", layout="centered")

# --- RUTAS DE IMÁGENES ---
LOGO_URL = "https://raw.githubusercontent.com/nwacontractors2022-spec/roof-aid-app/main/WhatsApp%20Image%202026-02-21%20at%209.25.44%20PM.jpeg".replace(" ", "%20")
HOUSE_ICON_URL = "https://cdn-icons-png.flaticon.com/512/619/619153.png"

# --- CSS PARA EL LOOK DE INSTAGRAM ---
st.markdown(f"""
    <style>
    .stApp {{
        background: radial-gradient(circle, #203a5c 0%, #152033 100%);
        color: white;
    }}
    
    .logo-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: -70px;
        margin-bottom: 20px;
    }}
    .main-logo {{ width: 100px; border-radius: 8px; }}

    /* Carrusel de historias */
    .story-container {{
        display: flex;
        overflow-x: auto;
        gap: 15px;
        padding-bottom: 10px;
        scrollbar-width: none;
    }}
    .story-container::-webkit-scrollbar {{ display: none; }}

    .owner-label {{
        font-size: 12px;
        font-weight: bold;
        text-align: center;
        margin-top: 4px;
    }}

    /* Tabs inferiores fixed */
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

# --- VENTANA EMERGENTE (POP-UP) ---
@st.dialog("Property Details")
def show_owner_details(person):
    st.markdown(f"""
        <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);">
            <p style="font-size: 18px; margin-bottom: 5px;"><b>Owner:</b> {person['name']}</p>
            <p style="margin: 0;"><b>Address:</b> {person['address']}</p>
            <p style="margin: 0;"><b>Phone:</b> {person['phone']}</p>
            <p style="margin: 0;"><b>Roof Size:</b> {person['sqft']} SqFt</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    
    # Lógica del botón GET (Envío de correo)
    subject = f"CLAIM LEAD: {person['name']}"
    body = f"I want to claim this lead:%0D%0AOwner: {person['name']}%0D%0AAddress: {person['address']}%0D%0ASize: {person['sqft']} SqFt"
    mail_url = f"mailto:admin@roofaid.com?subject={subject}&body={body}"
    
    st.markdown(f"""
        <a href="{mail_url}" target="_blank" style="text-decoration:none;">
            <div style="background-color:#28A745; color:white; padding:12px; text-align:center; border-radius:8px; font-weight:bold; box-shadow: 0 4px 10px rgba(40,167,69,0.2);">
                GET LEAD
            </div>
        </a>
    """, unsafe_allow_html=True)

# 1. Logo
st.markdown(f'<div class="logo-container"><img src="{LOGO_URL}" class="main-logo"></div>', unsafe_allow_html=True)

# --- BASE DE DATOS (Aquí es donde entrarán tus datos de Google Sheets) ---
# Si la lista está vacía [], no se mostrarán historias.
customers = [
    {"id": 1, "type": "appointment", "name": "John Doe", "address": "123 Sky Lane", "phone": "555-0101", "sqft": "2,400"},
    {"id": 2, "type": "appointment", "name": "Robert Ross", "address": "789 Pine Rd", "phone": "555-0303", "sqft": "3,100"},
    {"id": 3, "type": "follow_up", "name": "Jane Smith", "address": "456 Oak St", "phone": "555-0202", "sqft": "1,800"},
    {"id": 4, "type": "follow_up", "name": "Mike Myers", "address": "101 Lake Dr", "phone": "555-0404", "sqft": "2,000"},
    {"id": 5, "type": "follow_up", "name": "Sarah Connor", "address": "202 Term St", "phone": "555-0505", "sqft": "2,200"},
]

# Ordenar prioridad: Appointments (verdes) primero
sorted_customers = sorted(customers, key=lambda x: x['type'] != 'appointment')

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    if sorted_customers:
        st.write("### Potential Customers")
        
        # Carrusel horizontal con columnas dinámicas
        cols = st.columns(len(sorted_customers) if len(sorted_customers) > 0 else 1)
        
        for i, person in enumerate(sorted_customers):
            with cols[i]:
                # Color del texto según tipo
                label_color = "#28A745" if person['type'] == "appointment" else "#F57C00"
                
                # Círculo interactivo (Botón que dispara el Pop-up)
                if st.button("🏠", key=f"btn
