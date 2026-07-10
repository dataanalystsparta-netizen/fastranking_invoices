
"""
Premium KPI cards.
"""

import streamlit as st

from core.utils import format_currency


# ==========================================================
# SINGLE KPI CARD
# ==========================================================

def kpi_card(title, value, subtitle="", icon="📊", accent="#2563EB"):

    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            border-left:6px solid {accent};
            border-radius:14px;
            padding:18px;
            box-shadow:0 8px 20px rgba(0,0,0,.18);
            min-height:140px;
        ">

            <div style="
                font-size:15px;
                color:#CBD5E1;
                font-weight:600;
            ">
                {icon} {title}
            </div>

            <div style="
                font-size:32px;
                font-weight:700;
                color:white;
                margin-top:12px;
            ">
                {value}
            </div>

            <div style="
                color:#94A3B8;
                margin-top:10px;
                font-size:13px;
            ">
                {subtitle}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# KPI ROW
# ==========================================================

def render_kpis(kpis):

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    with c1:

        kpi_card(
            "Total Invoiced",
            format_currency(kpis["total_invoice"]),
            f"{kpis['invoices']:,} invoices",
            "💷",
            "#2563EB",
        )

    with c2:

        kpi_card(
            "Paid",
            format_currency(kpis["total_paid"]),
            "Collected",
            "✅",
            "#22C55E",
        )

    with c3:

        kpi_card(
            "Outstanding",
            format_currency(kpis["total_due"]),
            "Awaiting payment",
            "⏳",
            "#F59E0B",
        )

    with c4:

        kpi_card(
            "Customers",
            f"{kpis['customers']:,}",
            "Active customers",
            "🏢",
            "#8B5CF6",
        )

    with c5:

        kpi_card(
            "Invoices",
            f"{kpis['invoices']:,}",
            "Total invoices",
            "📄",
            "#0EA5E9",
        )

    with c6:

        kpi_card(
            "Overdue",
            f"{kpis['overdue']:,}",
            "Require attention",
            "🚨",
            "#EF4444",
        )
