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
# Aquí es donde vive TODA la información del cliente ahora
@st.dialog("Property Details")
def show_owner_details(person):
    st.markdown(f"""
        <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1); color: white;">
            <p style="font-size: 18px; margin-bottom: 10px;"><b>Owner:</b> {person['name']}</p>
            <p style="margin: 5px 0;"><b>Address:</b> {person['address']}</p>
            <p style="margin: 5px 0;"><b>Phone:</b> {person['phone']}</p>
            <p style="margin: 5px 0;"><b>Roof Size:</b> {person['sqft']} SqFt</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    
    # Lógica del botón GET
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

# --- BASE DE DATOS TEMPORAL ---
customers = [
    {"id": 1, "type": "appointment", "name": "John Doe", "address": "123 Sky Lane", "phone": "555-0101", "sqft": "2,400"},
    {"id": 2, "type": "appointment", "name": "Robert Ross", "address": "789 Pine Rd", "phone": "555-0303", "sqft": "3,100"},
    {"id": 3, "type": "follow_up", "name": "Jane Smith", "address": "456 Oak St", "phone": "555-0202", "sqft": "1,800"},
    {"id": 4, "type": "follow_up", "name": "Mike Myers", "address": "101 Lake Dr", "phone": "555-0404", "sqft": "2,000"},
    {"id": 5, "type": "follow_up", "name": "Sarah Connor", "address": "202 Term St", "phone": "555-0505", "sqft": "2,200"},
]

# Ordenar prioridad: Appointments primero
sorted_customers = sorted(customers, key=lambda x: x['type'] != 'appointment')

# --- NAVEGACIÓN ---
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    if sorted_customers:
        st.write("### Potential Customers")
        
        # Carrusel de historias
        cols = st.columns(len(sorted_customers))
        
        for i, person in enumerate(sorted_customers):
            with cols[i]:
                label_color = "#28A745" if person['type'] == "appointment" else "#F57C00"
                
                # Al hacer clic aquí, se abre el Pop-up y nada más
                if st.button("🏠", key=f"btn_{person['id']}"):
                    show_owner_details(person)
                
                st.markdown(f'<div class="owner-label" style="color:{label_color}">Owner</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # El Feed ahora aparece justo después de las historias
    st.write("### Feed")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    st.write("**Storm Intel:** Hail activity detected in NWA. Check potential claims.")

with tab_messages:
    st.chat_message("assistant").write("Hi, this is Riley from ROOF-AID. Ready to claim some leads?")
