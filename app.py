import streamlit as st
from PIL import Image
import pandas as pd
import io
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.animated_number import animated_number

# ---------- Styling ----------
def set_background():
    st.markdown(
        '''
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1531497865144-0464ef8fb9c6");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 2px 2px 10px #000000;
            padding: 0.3em 0;
        }
        .section-box {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2em;
            border-radius: 15px;
            margin-bottom: 2em;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }
        </style>
        ''',
        unsafe_allow_html=True
    )

set_background()

# ---------- Load logo ----------
logo = Image.open("Quantumela-logo.webp")

# ---------- Header ----------
col1, col2 = st.columns([0.15, 0.85])
with col1:
    st.image(logo, width=100)
with col2:
    st.markdown('<div class="main-title">Quantumela: SAP EC Migration & Variance Monitor</div>', unsafe_allow_html=True)
    st.caption("Secure • Accurate • Scalable")

# ---------- Sidebar Navigation ----------
st.sidebar.image(logo, width=100)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a module", ["Overview", "Dashboard", "Data Migration", "Validation", "Variance Monitoring", "Export Summary"])

# ---------- Overview Page ----------
if page == "Overview":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("🔷 Welcome to Quantumela’s Migration Suite")
    st.markdown("""
        At Quantumela, we help enterprises move from **SAP ECC** to **SAP SuccessFactors** with confidence.

        Our services cover:
        - 🔁 Data Migration (Foundation, Position, Employee, Payroll, Time)
        - 🧠 Validation Engine with built-in logic checks and field-level rule enforcement
        - 📊 Variance Monitoring Tool to flag mismatches and ensure audit accuracy
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Dashboard Page ----------
elif page == "Dashboard":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("📊 Executive Summary Dashboard")
    st.markdown("Here's a simulated view of migration progress and quality stats.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Files Migrated", value="5 / 5")
    with col2:
        st.metric("Validation Pass Rate", value="96%")
    with col3:
        st.metric("Detected Variances", value="12")

    style_metric_cards()

    st.markdown("---")
    st.subheader("📈 Live Metric Simulation")
    animated_number("Validated Records", 1800, format="{:,.0f}")
    animated_number("Clean Records %", 96, format="{:.1f}%")
    animated_number("Variance Reduction", 82, format="{:.0f}%")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Other sections remain unchanged... (add previous working logic here) --
