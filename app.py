import streamlit as st

# Configuración de página para móviles
st.set_page_config(page_title="Roof-Aid Beta", layout="centered")

# --- CSS Personalizado para el Look de Instagram ---
st.markdown("""
    <style>
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
tab_home, tab_messages, tab_profile = st.tabs(["🏠 Feed", "📩 Messages", "👤 Profile"])

with tab_home:
    st.write("### New Opportunities")
    s_col1, s_col2, s_col3, s_col4 = st.columns(4)
    
    with s_col1:
        st.markdown('<div class="story-circle red-border"><img src="https://cdn-icons-png.flaticon.com/512/1239/1239525.png" width="55"></div>', unsafe_allow_html=True)
        st.caption("Portland")
        st.button("Follow", key="f1")

    with s_col2:
        st.markdown('<div class="story-circle green-border"><img src="https://cdn-icons-png.flaticon.com/512/3209/3209265.png" width="55"></div>', unsafe_allow_html=True)
        st.caption("Corpus")
        st.button("Get Appt", key="a1")

    with s_col3:
        st.markdown('<div class="story-circle red-border"><img src="https://cdn-icons-png.flaticon.com/512/1239/1239525.png" width="55"></div>', unsafe_allow_html=True)
        st.caption("Mobile")
        st.button("Follow", key="f2")

    with s_col4:
        st.markdown('<div class="story-circle green-border"><img src="https://cdn-icons-png.flaticon.com/512/3209/3209265.png" width="55"></div>', unsafe_allow_html=True)
        st.caption("Arkansas")
        st.button("Get Appt", key="a2")

    st.divider()
    st.write("### 🌩️ Hail Activity Updates")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4") 
    st.image("https://via.placeholder.com/600x400/1a1a1a/ffffff?text=Insurance+Claim+Data+IA", use_container_width=True)

with tab_messages:
    st.write("### 💬 Communications Center")
    st.info("⚠️ Alerta: Tormenta de granizo en Corpus Christi.")
    st.chat_message("assistant").write("Hola! Soy Riley de ROOF-AID. ¿En qué puedo ayudarte hoy?")

with tab_profile:
    st.write("### 👤 Contractor Profile")
    p_col1, p_col2 = st.columns([1, 2])
    with p_col1:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=90)
    with p_col2:
        st.write("#### Roofer Pro ✅")
        st.write("**License:** #TX-99812-RC")
    st.divider()
    st.write(f"**Plan:** Premium ($600/mo)")
