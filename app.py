import streamlit as st
import pandas as pd
from io import BytesIO

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Invoice Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main{
    background-color:#0e1117;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3{
    color:white;
}

.metric-card{
    background:#1f2937;
    border-radius:14px;
    padding:20px;
    border:1px solid #30363d;
    box-shadow:0 0 10px rgba(0,0,0,.25);
    transition:0.25s;
}

.metric-card:hover{
    transform:translateY(-2px);
    box-shadow:0 0 18px rgba(0,0,0,.35);
}

.metric-title{
    color:#9ca3af;
    font-size:15px;
}

.metric-value{
    color:white;
    font-size:34px;
    font-weight:bold;
    margin-top:8px;
}

.paid{
    color:#22c55e;
    font-weight:bold;
}

.open{
    color:#f59e0b;
    font-weight:bold;
}

.overdue{
    color:#ef4444;
    font-weight:bold;
}

.summary-box{
    background:#1b2028;
    padding:15px;
    border-radius:12px;
    border:1px solid #2f3640;
    margin-bottom:12px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# FUNCTIONS
# ==========================================================

@st.cache_data(show_spinner=False)
def load_excel(file):

    df = pd.read_excel(file)

    df.columns = df.columns.str.strip()

    df["Total"] = pd.to_numeric(df["Total"], errors="coerce").fillna(0)

    df["Balance"] = pd.to_numeric(df["Balance"], errors="coerce").fillna(0)

    df["Paid Amount"] = df["Total"] - df["Balance"]

    df["Invoice Date"] = pd.to_datetime(
        df["Invoice Date"],
        dayfirst=True,
        errors="coerce"
    )

    df["Due Date"] = pd.to_datetime(
        df["Due Date"],
        dayfirst=True,
        errors="coerce"
    )

    return df


def pounds(value):
    return f"£{value:,.2f}"


def status_html(status):

    if pd.isna(status):
        return ""

    status = str(status).lower()

    if status == "closed":
        return "<span class='paid'>🟢 Closed</span>"

    if status == "open":
        return "<span class='open'>🟠 Open</span>"

    if status == "overdue":
        return "<span class='overdue'>🔴 Overdue</span>"

    return status.title()


# ==========================================================
# HEADER
# ==========================================================

st.title("📊 Invoice Dashboard")

st.caption("Upload your invoice Excel export to begin.")

uploaded_file = st.file_uploader(
    "Upload Invoice Excel",
    type=["xlsx"]
)

if uploaded_file is None:

    st.info("Please upload an invoice export to continue.")

    st.stop()

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_excel(uploaded_file)

# ==========================================================
# KPI CALCULATIONS
# ==========================================================

total_invoice = df["Total"].sum()

total_due = df["Balance"].sum()

total_paid = df["Paid Amount"].sum()

invoice_count = len(df)

customer_count = df["Customer Name"].nunique()

# ==========================================================
# KPI CARDS
# ==========================================================

c1, c2, c3, c4, c5 = st.columns(5)

with c1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💷 Total Invoiced</div>
        <div class="metric-value">{pounds(total_invoice)}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">✅ Total Paid</div>
        <div class="metric-value">{pounds(total_paid)}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">⏳ Total Due</div>
        <div class="metric-value">{pounds(total_due)}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📄 Invoices</div>
        <div class="metric-value">{invoice_count:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c5:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🏢 Customers</div>
        <div class="metric-value">{customer_count:,}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================================================
# SEARCH
# ==========================================================

search = st.text_input(
    "🔍 Search Business",
    placeholder="Start typing customer name..."
)

if search:

    df = df[
        df["Customer Name"]
        .str.contains(search, case=False, na=False)
    ]
