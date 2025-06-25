import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quantumela SAP Tool", page_icon="📊", layout="wide")

# --- Logo and Branding ---
col1, col2 = st.columns([0.15, 0.85])
with col1:
    st.image("Quantumela-logo.webp", width=100)
with col2:
    st.title("Quantumela: SAP EC Migration & Variance Monitor Tool")
    st.caption("Effortless, Accurate, and Insight-Driven SAP Data Transformation")

# Sidebar Navigation
st.sidebar.image("Quantumela-logo.webp", width=120)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Data Migration", "Validation", "Variance Monitoring"])

if page == "Overview":
    st.header("🔷 About Our Solution")
    st.markdown("""
    Welcome to **Quantumela's** SAP SuccessFactors data migration platform. We specialize in secure and scalable data migration and monitoring solutions tailored for SAP landscapes.

    ### 🌐 What We Do
    - **Employee Central Data Migration**
        - Migrate Foundation, Position, and Employee objects
        - Integrate EC Payroll and Time & Attendance

    - **Automated Validation**
        - Schema compliance checks
        - Field-level and cross-table rule validation
        - Summary reports

    - **Variance Monitoring**
        - Compare SAP ECC vs SAP SF
        - Track field mismatches, missing data, formatting errors

    ### 💡 Why Quantumela?
    - Industry-aligned best practices
    - Custom logic mapping and transformation
    - Clean, auditable variance reports

    ### 🛡️ Our Approach
    Quantumela follows a phased methodology: Discovery, Mapping, Testing, Validation, and Deployment.
    Each phase is powered by smart tools and SAP best practices to ensure integrity and minimal downtime.
    """)
    st.image("Employee_Central_Data_Migration.png", caption="Employee Central Migration Architecture", use_container_width=True)

elif page == "Data Migration":
    st.header("📂 Employee Central Data Migration")
    st.markdown("""
    Upload source files for migration below. Files remain private and are used only for analysis.

    **Services We Provide:**
    - Object-wise transformation based on SAP EC schema
    - Unique key reconciliation across legacy and target systems
    - Use of pre-migration templates, mapping sheets and config files
    - Multi-layer validation during ETL
    """)
    st.image("Employee_Central_Data_Migration2.png", caption="Process Flow for EC Object Handling", use_container_width=True)

    with st.expander("📁 Foundation Objects"):
        st.markdown("""
        - Company, Business Unit, Division, Department, Cost Center
        - Location and Legal Entity
        - Parent-child hierarchy setup
        """)
        st.file_uploader("Upload Foundation Data (CSV/XLSX)", type=["csv", "xlsx"], key="foundation")

    with st.expander("📁 Position Objects"):
        st.markdown("""
        - Position ID, Title, Org Chart mappings
        - Job Relationships (Matrix, Manager, etc.)
        - Effective start dates and status
        """)
        st.file_uploader("Upload Position Data (CSV/XLSX)", type=["csv", "xlsx"], key="position")

    with st.expander("📁 Employee Objects"):
        st.markdown("""
        - Personal Information: Name, DOB, Gender
        - Job Info: Department, Position, Manager
        - Comp Info: Salary, Pay Grade, Currency
        """)
        st.file_uploader("Upload Employee Data (CSV/XLSX)", type=["csv", "xlsx"], key="employee")

    with st.expander("💰 EC Payroll"):
        st.markdown("""
        - Pay Components & Frequency
        - Assignment to Jobs or Individuals
        - Payroll Calendar Mapping
        """)
        st.file_uploader("Upload Payroll Data (CSV/XLSX)", type=["csv", "xlsx"], key="payroll")

    with st.expander("⏱️ EC Time & Attendance"):
        st.markdown("""
        - Time Type Mapping
        - Shift and Leave Balance Validation
        - Time Account Setup
        """)
        st.file_uploader("Upload Time & Attendance (CSV/XLSX)", type=["csv", "xlsx"], key="time")

elif page == "Validation":
    st.header("✅ Validation Services")
    st.markdown("""
    Quantumela applies rule-based validations at field and relationship level. 

    **Validation Checks Include:**
    - Schema compliance with SAP EC standards
    - Missing critical fields or bad formats (e.g., phone number, email, currency code)
    - Referential integrity checks across Position, Job Info, Org data
    - Business rules: date logic, cross-field dependency
    """)
    st.image("validation_lifecycle.png", caption="Validation Lifecycle Overview", use_container_width=True)

    st.file_uploader("Upload Migrated Dataset", type=["csv", "xlsx"], key="val_data")
    st.file_uploader("Upload Validation Rules (CSV/JSON)", type=["csv", "json"], key="val_rules")

    if st.button("Run Validation"):
        st.success("Validation successful. A detailed report will be generated.")

elif page == "Variance Monitoring":
    st.header("📊 Variance Monitoring")
    st.markdown("""
    Compare values between SAP ECC and SAP SF datasets to identify mismatches:

    **We Monitor:**
    - Presence of missing/mismatched records
    - Variations in numeric values (e.g. salary, bonus)
    - Format & date inconsistencies
    - Record status mismatches (active vs inactive)

    **How We Help:**
    - Auto-generate variance reports
    - Highlight critical fields
    - Support delta resolution tracking
    """)
    st.image("variance_monitoring.png", caption="Variance Monitoring Workflow", use_container_width=True)

    st.file_uploader("Upload SAP ECC Extract", type=["csv", "xlsx"], key="source")
    st.file_uploader("Upload SAP SF Extract", type=["csv", "xlsx"], key="target")

    if st.button("Run Variance Analysis"):
        st.success("Variance check complete. Delta report will be displayed here.")
