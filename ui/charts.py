"""
Interactive dashboard charts.
"""

import streamlit as st
import plotly.express as px

from config.colors import (
    CHART_BLUE,
    CHART_GREEN,
    CHART_ORANGE,
    CHART_RED,
    CARD,
    TEXT
)


# ==========================================================
# COMMON LAYOUT
# ==========================================================

def apply_layout(fig):

    fig.update_layout(

        paper_bgcolor=CARD,

        plot_bgcolor=CARD,

        font=dict(
            color=TEXT,
            size=13
        ),

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),

        height=380,

        legend_title=None
    )

    return fig


# ==========================================================
# PAID VS OUTSTANDING
# ==========================================================

def paid_due_chart(df):

    fig = px.pie(

        df,

        names="Category",

        values="Amount",

        hole=.65,

        color="Category",

        color_discrete_map={

            "Paid": CHART_GREEN,

            "Outstanding": CHART_ORANGE

        }

    )

    fig.update_traces(

        textposition="inside",

        textinfo="percent+label"

    )

    fig = apply_layout(fig)

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# MONTHLY REVENUE
# ==========================================================

def monthly_chart(df):

    fig = px.line(

        df,

        x="Month",

        y="Total",

        markers=True

    )

    fig.update_traces(

        line=dict(

            width=4,

            color=CHART_BLUE

        )

    )

    fig = apply_layout(fig)

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# TOP OUTSTANDING
# ==========================================================

def top_customers_chart(df):

    if df.empty:

        st.info("No outstanding invoices.")

        return

    fig = px.bar(

        df,

        x="due",

        y="Customer Name",

        orientation="h",

        text="due"

    )

    fig.update_traces(

        marker_color=CHART_RED

    )

    fig.update_layout(

        yaxis=dict(

            categoryorder="total ascending"

        )

    )

    fig = apply_layout(fig)

    st.plotly_chart(

        fig,

        use_container_width=True

    )


# ==========================================================
# STATUS
# ==========================================================

def status_chart(df):

    fig = px.bar(

        df,

        x="Invoice Status",

        y="Invoices",

        color="Invoice Status",

        color_discrete_map={

            "Closed": CHART_GREEN,

            "Open": CHART_ORANGE,

            "Overdue": CHART_RED

        }

    )

    fig = apply_layout(fig)

    st.plotly_chart(

        fig,

        use_container_width=True

    )
