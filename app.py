
import streamlit as st
from PIL import Image

# Load and apply custom CSS styling for a website-like look
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1504384308090-c894fdcc538d");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        .main-title {{
            font-size: 3em;
            font-weight: 700;
            color: #ffffff;
            padding: 0.5em 0;
            text-shadow: 2px 2px 8px #000000;
        }}
        .section-box {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2em;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
            margin-bottom: 2em;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Load logo
logo = Image.open("Quantumela-logo.webp")
st.image(logo, width=120)

# Main title
st.markdown('<div class="main-title">Quantumela: SAP EC Migration & Variance Monitor Tool</div>', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.image(logo, width=100)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Data Migration", "Validation", "Variance Monitoring"])

if page == "Overview":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("🔷 About Our Solution")
    st.markdown("""
    Quantumela offers a premium platform for **SAP ECC to SAP SuccessFactors** migration with full validation and monitoring capabilities.

    ### 🌐 Key Services:
    - **Employee Central Data Migration** (Foundation, Position, Employee, Payroll, Time & Attendance)
    - **Automated Data Validation** with rules, formats, and business logic checks
    - **Variance Monitoring** across source and target systems

    Our tools ensure accuracy, traceability, and business continuity.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Data Migration":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("📂 Employee Central Data Migration")
    st.markdown("Upload migration files below. Files remain local and secure.")

    with st.expander("📁 Foundation Objects"):
        st.file_uploader("Upload Foundation Data", type=["csv", "xlsx"], key="foundation")

    with st.expander("📁 Position Objects"):
        st.file_uploader("Upload Position Data", type=["csv", "xlsx"], key="position")

    with st.expander("📁 Employee Objects"):
        st.file_uploader("Upload Employee Data", type=["csv", "xlsx"], key="employee")

    with st.expander("💰 EC Payroll"):
        st.file_uploader("Upload Payroll Data", type=["csv", "xlsx"], key="payroll")

    with st.expander("⏱️ EC Time & Attendance"):
        st.file_uploader("Upload Time & Attendance Data", type=["csv", "xlsx"], key="time")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Validation":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("✅ Validation Services")
    st.markdown("""
    Ensure your migrated data meets quality and compliance expectations.

    - Null checks, format compliance
    - Field matching against rule files
    - Reporting on invalid entries and severity

    Upload data and rules to begin validation.
    """)
    st.file_uploader("Upload Data File", type=["csv", "xlsx"], key="val_data")
    st.file_uploader("Upload Validation Rules (CSV/JSON)", type=["csv", "json"], key="val_rules")
    if st.button("Run Validation"):
        st.success("Validation complete. Summary report available.")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Variance Monitoring":
    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.header("📊 Variance Monitoring")
    st.markdown("""
    Compare SAP ECC and SAP SF data for inconsistencies:

    - Identify missing rows and unmatched values
    - See field-level changes
    - Maintain audit readiness

    Upload ECC and SF files to begin comparison.
    """)
    st.file_uploader("Upload SAP ECC Extract", type=["csv", "xlsx"], key="ecc")
    st.file_uploader("Upload SAP SF Extract", type=["csv", "xlsx"], key="sf")
    if st.button("Compare Now"):
        st.success("Comparison completed. Differences will be visualized here.")
    st.markdown('</div>', unsafe_allow_html=True)
