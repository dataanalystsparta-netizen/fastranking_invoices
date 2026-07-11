import streamlit as st
from core.utils import format_currency


def kpi_card(title, value, subtitle="", icon="📊", accent="#2563EB"):

    html = f"""
    <div style="
        background:#1E293B;
        border-left:6px solid {accent};
        border-radius:12px;
        padding:20px;
        height:160px;
        box-shadow:0 4px 10px rgba(0,0,0,0.25);
        font-family:sans-serif;
    ">

        <div style="
            font-size:15px;
            color:#CBD5E1;
            font-weight:600;
        ">
            {icon} {title}
        </div>


        <div style="
            font-size:34px;
            font-weight:700;
            color:#FFFFFF;
            margin-top:15px;
        ">
            {value}
        </div>


        <div style="
            font-size:13px;
            color:#94A3B8;
            margin-top:18px;
        ">
            {subtitle}
        </div>

    </div>
    """

    st.markdown(html, unsafe_allow_html=True)


def render_kpis(kpis):

    c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)


    with c1:
        kpi_card(
            "Total Invoiced",
            format_currency(kpis["total_invoice"]),
            f'{kpis["invoices"]:,} invoices',
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
            f'{kpis["customers"]:,}',
            "Active Customers",
            "🏢",
            "#8B5CF6",
        )


    with c5:
        kpi_card(
            "Invoices",
            f'{kpis["invoices"]:,}',
            "Total Invoices",
            "📄",
            "#0EA5E9",
        )


    with c6:
        kpi_card(
            "Overdue",
            f'{kpis["overdue"]:,}',
            "Require Attention",
            "🚨",
            "#EF4444",
        )
    with c7:
    kpi_card(
        "Draft",
        f'{kpis["draft"]:,}',
        "Draft invoices",
        "📝",
        "#64748B",
    )

    with c8:
        kpi_card(
            "Void",
            f'{kpis["void"]:,}',
            "Void invoices",
            "❌",
            "#6B7280",
        )
