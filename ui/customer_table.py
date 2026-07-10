"""
Customer summary table.
"""

import streamlit as st

from core.utils import format_currency


# ==========================================================
# HEALTH INDICATOR
# ==========================================================

def health_badge(percent):

    if percent >= 95:
        return "🟢 Excellent"

    elif percent >= 75:
        return "🟡 Good"

    elif percent >= 50:
        return "🟠 Average"

    else:
        return "🔴 Needs Attention"


# ==========================================================
# RENDER CUSTOMER TABLE
# ==========================================================

def render_customer_table(summary_df):

    st.subheader("🏢 Customer Summary")

    if summary_df.empty:

        st.info("No customers found.")

        return None

    display = summary_df.copy()

    display["Health"] = (
        display["payment_percent"]
        .apply(health_badge)
    )

    display["Total Invoiced"] = (
        display["total_invoice"]
        .apply(format_currency)
    )

    display["Paid"] = (
        display["paid"]
        .apply(format_currency)
    )

    display["Outstanding"] = (
        display["due"]
        .apply(format_currency)
    )

    display = display.rename(
        columns={
            "Customer Name": "Customer",
            "invoices": "Invoices"
        }
    )

    display = display[
        [
            "Customer",
            "Total Invoiced",
            "Paid",
            "Outstanding",
            "Invoices",
            "Health"
        ]
    ]

    st.dataframe(
        display,
        use_container_width=True,
        hide_index=True,
        height=500
    )

    customer = st.selectbox(
        "Select Customer",
        summary_df["Customer Name"].tolist()
    )

    return customer
