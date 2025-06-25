
import streamlit as st
from PIL import Image
import pandas as pd
import io

# ---------- Styling ----------
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1531497865144-0464ef8fb9c6");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        .main-title {{
            font-size: 3em;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 2px 2px 10px #000000;
            padding: 0.3em 0;
        }}
        .section-box {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2em;
            border-radius: 15px;
            margin-bottom: 2em;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        }}
        .subheading {{
            color: #003366;
            font-size: 1.5em;
            font-weight: 600;
        }}
        </style>
        """,
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
    - 🔁 **Data Migration** (Foundation, Position, Employee, Payroll, Time)
    - 🧠 **Validation Engine** with built-in logic checks and field-level rule enforcement
    - 📊 **Variance Monitoring Tool** to flag mismatches and ensure audit accuracy
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Dashboard Page ----------
elif page == "Dashboard":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("📊 Executive Summary Dashboard")
    st.markdown("""
    Here's a simulated view of migration progress and quality stats.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Files Migrated", "5/5")
    col2.metric("Validation Pass Rate", "96%")
    col3.metric("Detected Variances", "12")

    st.progress(0.96)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- Data Migration Page ----------
elif page == "Data Migration":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("📂 Upload Data for Migration")

    for label, key in [
        ("Foundation Object", "foundation"),
        ("Position Object", "position"),
        ("Employee Object", "employee"),
        ("EC Payroll", "payroll"),
        ("EC Time & Attendance", "time")
    ]:
        with st.expander(f"📁 {label}"):
            st.file_uploader(f"Upload {label} file", type=["csv", "xlsx"], key=key)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Validation Page ----------
elif page == "Validation":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("✅ Run Validation")

    uploaded_data = st.file_uploader("Upload Data File (CSV/XLSX)", type=["csv", "xlsx"], key="val_data")
    uploaded_rules = st.file_uploader("Upload Validation Rules (CSV/JSON)", type=["csv", "json"], key="val_rules")

    if st.button("Run Validation"):
        st.success("Validation completed with 96% pass rate.")
        st.markdown(\""" 
• 4 critical issues  
• 8 warnings 
\""")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Variance Monitoring Page ----------
elif page == "Variance Monitoring":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("🔍 Variance Monitoring")

    st.markdown("Compare ECC and SF data to identify mismatches.")
    ecc_file = st.file_uploader("Upload SAP ECC Extract", type=["csv", "xlsx"], key="ecc")
    sf_file = st.file_uploader("Upload SAP SF Extract", type=["csv", "xlsx"], key="sf")

    if st.button("Run Comparison"):
        st.success("12 mismatches found across 3 employee records.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Export Summary ----------
elif page == "Export Summary":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("📤 Export Migration Summary")

    summary_data = pd.DataFrame({
        "Object": ["Foundation", "Position", "Employee", "Payroll", "Time"],
        "Records Migrated": [120, 85, 300, 115, 200],
        "Validation Pass %": [98, 95, 97, 96, 94]
    })

    st.dataframe(summary_data, use_container_width=True)

    # Create downloadable Excel file
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        summary_data.to_excel(writer, index=False, sheet_name="Summary")
    st.download_button("Download Summary Report", data=buffer.getvalue(), file_name="quantumela_migration_summary.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    st.markdown('</div>', unsafe_allow_html=True)
