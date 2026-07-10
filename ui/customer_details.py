
"""
Customer details section.
"""

import streamlit as st

from core.utils import (
    format_currency,
    format_invoice_table,
    percentage
)


# ==========================================================
# CUSTOMER DETAILS
# ==========================================================

def render_customer_details(df, customer_name):

    if customer_name is None:
        return

    customer_df = df[
        df["Customer Name"] == customer_name
    ].copy()

    if customer_df.empty:
        st.info("No invoices found.")
        return

    total_invoice = customer_df["Total"].sum()
    total_paid = customer_df["Paid Amount"].sum()
    total_due = customer_df["Balance"].sum()

    payment_rate = percentage(
        total_paid,
        total_invoice
    )

    st.divider()

    st.subheader(f"🏢 {customer_name}")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.metric(
            "Total Invoiced",
            format_currency(total_invoice)
        )

    with c2:
        st.metric(
            "Paid",
            format_currency(total_paid)
        )

    with c3:
        st.metric(
            "Outstanding",
            format_currency(total_due)
        )

    with c4:
        st.metric(
            "Invoices",
            len(customer_df)
        )

    with c5:
        st.metric(
            "Payment Rate",
            f"{payment_rate:.1f}%"
        )

    st.progress(payment_rate / 100)

    st.caption(
        f"Payment Completion: {payment_rate:.1f}%"
    )

    st.write("")

    st.subheader("📄 Invoices")

    display = format_invoice_table(customer_df)

    columns = [
        "Invoice Number",
        "Invoice Date",
        "Due Date",
        "Total",
        "Paid Amount",
        "Balance",
        "Invoice Status"
    ]

    columns = [
        c for c in columns
        if c in display.columns
    ]

    st.dataframe(
        display[columns],
        use_container_width=True,
        hide_index=True,
        height=450
    )
