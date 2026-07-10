"""
All business calculations for the dashboard.
"""

import pandas as pd


# ==========================================================
# KPI SUMMARY
# ==========================================================

def calculate_kpis(df):

    total_invoice = df["Total"].sum()

    total_paid = df["Paid Amount"].sum()

    # Only Open + Overdue contribute to Outstanding
    outstanding_df = df[
        df["Invoice Status"].str.lower().isin(["open", "overdue"])
    ]

    total_due = outstanding_df["Balance"].sum()

    total_customers = df["Customer Name"].nunique()

    total_invoices = len(df)

    overdue = (
        df["Invoice Status"]
        .str.lower()
        .eq("overdue")
        .sum()
    )

    draft = (
        df["Invoice Status"]
        .str.lower()
        .eq("draft")
        .sum()
    )

    void = (
        df["Invoice Status"]
        .str.lower()
        .eq("void")
        .sum()
    )

    return {
        "total_invoice": total_invoice,
        "total_paid": total_paid,
        "total_due": total_due,
        "customers": total_customers,
        "invoices": total_invoices,
        "overdue": overdue,
        "draft": draft,
        "void": void,
    }

# ==========================================================
# CUSTOMER SUMMARY
# ==========================================================

def customer_summary(df):

    summary = (

        df.groupby("Customer Name")

        .agg(

            invoices=("Invoice Number", "count"),

            total_invoice=("Total", "sum"),

            paid=("Paid Amount", "sum"),

            due=("Balance", "sum")

        )

        .reset_index()

    )

    summary["payment_percent"] = (

        summary["paid"]

        /

        summary["total_invoice"]

        * 100

    ).fillna(0)

    summary = summary.sort_values(

        by="due",

        ascending=False

    )

    return summary


# ==========================================================
# TOP OUTSTANDING
# ==========================================================

def top_outstanding(df, top=10):

    summary = customer_summary(df)

    return summary.head(top)


# ==========================================================
# OVERDUE INVOICES
# ==========================================================

def overdue_invoices(df):

    overdue = df[

        df["Invoice Status"]

        .str.lower()

        == "overdue"

    ]

    overdue = overdue.sort_values(

        by="Due Date"

    )

    return overdue


# ==========================================================
# PAID VS DUE
# ==========================================================

def paid_vs_due(df):

    return pd.DataFrame(

        {

            "Category": [

                "Paid",

                "Outstanding"

            ],

            "Amount": [

                df["Paid Amount"].sum(),

                df["Balance"].sum()

            ]

        }

    )


# ==========================================================
# MONTHLY REVENUE
# ==========================================================

def monthly_revenue(df):

    temp = df.copy()

    temp["Month"] = (

        temp["Invoice Date"]

        .dt.to_period("M")

        .astype(str)

    )

    monthly = (

        temp.groupby("Month")

        ["Total"]

        .sum()

        .reset_index()

    )

    return monthly


# ==========================================================
# STATUS BREAKDOWN
# ==========================================================

def status_breakdown(df):

    summary = (

        df.groupby("Invoice Status")

        .size()

        .reset_index(name="Invoices")

    )

    return summary


# ==========================================================
# CUSTOMER DETAILS
# ==========================================================

def customer_details(df, customer_name):

    customer = df[

        df["Customer Name"]

        == customer_name

    ].copy()

    customer = customer.sort_values(

        by="Invoice Date",

        ascending=False

    )

    return customer


# ==========================================================
# DASHBOARD SUMMARY
# ==========================================================

def dashboard_data(df):

    return {

        "kpis": calculate_kpis(df),

        "customers": customer_summary(df),

        "monthly": monthly_revenue(df),

        "top_due": top_outstanding(df),

        "paid_due": paid_vs_due(df),

        "overdue": overdue_invoices(df),

        "status": status_breakdown(df)

    }

