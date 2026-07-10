import streamlit as st

from config.settings import (
    APP_NAME,
    APP_SUBTITLE,
    APP_SHORT_NAME,
)

from ui.styles import load_css
from ui.cards import render_kpis
from ui.charts import (
    paid_due_chart,
    monthly_chart,
    top_customers_chart,
    status_chart,
)
from ui.customer_table import render_customer_table
from ui.customer_details import render_customer_details
from ui.alerts import render_action_center

from core.loader import (
    load_excel,
    get_file_summary,
)

from core.filters import apply_filters
from core.calculations import dashboard_data


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title=APP_SHORT_NAME,
    page_icon="💷",
    layout="wide",
)

load_css()

# ==========================================================
# HEADER
# ==========================================================

st.title(APP_NAME)
st.caption(APP_SUBTITLE)

st.divider()

# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "Upload Invoice Excel",
    type=["xlsx", "xls"]
)

if uploaded_file is None:

    st.info("Please upload an invoice Excel file.")

    st.stop()

# ==========================================================
# LOAD DATA
# ==========================================================

try:

    df = load_excel(uploaded_file)

except Exception as e:

    st.error(e)

    st.stop()

summary = get_file_summary(df)

# ==========================================================
# FILTERS
# ==========================================================

st.subheader("Filters")

f1, f2, f3, f4 = st.columns(4)

with f1:

    start_date = st.date_input(
        "From",
        value=df["Invoice Date"].min().date()
    )

with f2:

    end_date = st.date_input(
        "To",
        value=df["Invoice Date"].max().date()
    )

with f3:

    status = st.selectbox(
        "Status",
        [
            "All",
            "Closed",
            "Open",
            "Overdue",
        ],
    )

with f4:

    customer_search = st.text_input(
        "Customer"
    )

filtered = apply_filters(
    df,
    start_date=start_date,
    end_date=end_date,
    status=status,
    customer_search=customer_search,
)

# ==========================================================
# CALCULATIONS
# ==========================================================

dashboard = dashboard_data(filtered)

# ==========================================================
# KPI CARDS
# ==========================================================

render_kpis(
    dashboard["kpis"]
)

st.write("")

# ==========================================================
# CHARTS + ACTION CENTER
# ==========================================================

left, right = st.columns([3, 1])

with left:

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Paid vs Outstanding")

        paid_due_chart(
            dashboard["paid_due"]
        )

    with c2:

        st.subheader("Invoice Status")

        status_chart(
            dashboard["status"]
        )

    st.subheader("Monthly Revenue")

    monthly_chart(
        dashboard["monthly"]
    )

    st.subheader("Top Outstanding Customers")

    top_customers_chart(
        dashboard["top_due"]
    )

with right:

    render_action_center(
        dashboard
    )

# ==========================================================
# CUSTOMER SUMMARY
# ==========================================================

customer = render_customer_table(
    dashboard["customers"]
)

# ==========================================================
# CUSTOMER DETAILS
# ==========================================================

render_customer_details(
    filtered,
    customer
)

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    f"{APP_NAME} • {len(filtered):,} invoices loaded"
)
