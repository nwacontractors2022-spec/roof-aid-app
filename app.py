import streamlit as st

# Configuración de página para móviles
st.set_page_config(page_title="Roof-Aid Beta", layout="centered")

# --- CSS Personalizado para el Look de Instagram ---
st.markdown("""
    <style>
    /* Estilo de los círculos de historias */
    .story-circle {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: 65px;
        height: 65px;
        padding: 3px;
    }
    .red-border { border: 3px solid #ff4b4b; }
    .green-border { border: 3px solid #28a745; }
    
    /* Ajuste de la navegación inferior */
    .stTabs [data-baseweb="tab-list"] {
        position: fixed;
        bottom: 0;
        background-color: white;
        z-index: 100;
        width: 100%;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN INFERIOR ---
# Usamos Tabs para simular los módulos de IG
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

# --- MÓDULO 1: HOME (STORIES & FEED) ---
with tab_home:
    # SECCIÓN STORIES (Follow-ups y Appointments)
    st.write("### New Opportunities")
    s_col1, s_col2, s_col3, s_col4 = st.columns(4)
    
    with s_col1:
        st.markdown('<div class="story-circle red-border"><img src="https://cdn-icons-png.flaticon.com/512/1239/1239525.png" width="55"></div>', unsafe_allow_index=True)
        st.caption("Portland")
        st.button("Follow", key="f1")

    with s_col2:
        st.markdown('<div class="story-circle green-border"><img src="https://cdn-icons-png.flaticon.com/512/3209/3209265.png" width="55"></div>', unsafe_allow_index=True)
        st.caption("Corpus")
        st.button("Get Appt", key="a1")

    with s_col3:
        st.markdown('<div class="story-circle red-border"><img src="https://cdn-icons-png.flaticon.com/512/1239/1239525.png" width="55"></div>', unsafe_allow_index=True)
        st.caption("Mobile")
        st.button("Follow", key="f2")

    with s_col4:
        st.markdown('<div class="story-circle green-border"><img src="https://cdn-icons-png.flaticon.com/512/3209/3209265.png" width="55"></div>', unsafe_allow_index=True)
        st.caption("Arkansas")
        st.button("Get Appt", key="a2")

    st.divider()

    # SECCIÓN FEED (Contenido IA Marketing)
    st.write("### 🌩️ Hail Activity Updates")
    # Simulación de Video de Avatar IA
    st.video("https://www.w3schools.com/html/mov_bbb.mp4") 
    st.write("**Storm Intel:** Granizo detectado en Alabama. 120 techos afectados.")
    
    # Simulación de Info-Foto IA
    st.image("https://via.placeholder.com/600x400/1a1a1a/ffffff?text=Insurance+Claim+Data+IA", use_container_width=True)
    st.write("Nuevos contratos disponibles para Roofers con licencia activa.")

# --- MÓDULO 2: MESSAGES (BUZÓN CENTRAL) ---
with tab_messages:
    st.write("### 💬 Communications Center")
    st.info("⚠️ Alerta Especial: Tormenta de granizo categoría 2 en Corpus Christi.")
    st.chat_message("assistant").write("Roof-Aid Support: Hola, ¿necesitas ayuda técnica?")
    st.text_input("Escribe un mensaje...")

# --- MÓDULO 3: PROFILE (LICENCIA Y SUSCRIPCIÓN) ---
with tab_profile:
    st.write("### 👤 Contractor Profile")
    p_col1, p_col2 = st.columns([1, 2])
    with p_col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90)
    with p_col2:
        st.write("#### Roofer Pro ✅")
        st.write("**License:** #TX-99812-RC")
    
    st.divider()
    st.write(f"**State:** Texas")
    st.write(f"**Email:** adrian@roofaid.com")
    st.write(f"**Tier:** Premium ($600/mo)")
    st.button("Verify New License")
