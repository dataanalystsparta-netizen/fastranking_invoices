"""
Executive Action Center
"""

import streamlit as st

from core.utils import (
    format_currency,
    percentage
)


# ==========================================================
# ACTION CENTER
# ==========================================================

def render_action_center(data):

    kpis = data["kpis"]
    customers = data["customers"]
    overdue = data["overdue"]

    st.subheader("🚨 Action Center")

    # ------------------------------------------------------

    st.metric(
        "Outstanding",
        format_currency(kpis["total_due"])
    )

    st.divider()

    # ------------------------------------------------------

    if not customers.empty:

        debtor = customers.iloc[0]

        st.metric(
            "Largest Debtor",
            debtor["Customer Name"]
        )

        st.caption(
            format_currency(debtor["due"])
        )

    st.divider()

    # ------------------------------------------------------

    st.metric(
        "Overdue Invoices",
        len(overdue)
    )

    st.divider()

    # ------------------------------------------------------

    collection_rate = percentage(
        kpis["total_paid"],
        kpis["total_invoice"]
    )

    st.metric(
        "Collection Rate",
        f"{collection_rate:.1f}%"
    )

    progress_color = (
        "normal"
        if collection_rate >= 80
        else "inverse"
    )

    st.progress(
        collection_rate / 100
    )

    st.divider()

    # ------------------------------------------------------

    if len(overdue):

        oldest = overdue.iloc[0]

        st.write("### ⚠ Oldest Overdue")

        st.write(
            oldest["Customer Name"]
        )

        st.caption(
            oldest["Invoice Number"]
        )

        st.caption(
            format_currency(
                oldest["Balance"]
            )
        )

    else:

        st.success(
            "No overdue invoices 🎉"
        )
