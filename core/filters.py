"""
Filtering functions for the dashboard.
"""

import pandas as pd


# ==========================================================
# DATE FILTER
# ==========================================================

def filter_by_date(
    df,
    start_date=None,
    end_date=None
):

    if start_date is not None:

        df = df[
            df["Invoice Date"].dt.date >= start_date
        ]

    if end_date is not None:

        df = df[
            df["Invoice Date"].dt.date <= end_date
        ]

    return df


# ==========================================================
# STATUS FILTER
# ==========================================================

def filter_by_status(
    df,
    status
):

    if (
        status is None
        or status == "All"
    ):

        return df

    return df[
        df["Invoice Status"]
        == status
    ]


# ==========================================================
# CUSTOMER SEARCH
# ==========================================================

def filter_by_customer(
    df,
    search_text
):

    if (
        search_text is None
        or search_text.strip() == ""
    ):

        return df

    return df[

        df["Customer Name"]

        .str.contains(

            search_text,

            case=False,

            na=False

        )

    ]


# ==========================================================
# INVOICE SEARCH
# ==========================================================

def filter_by_invoice(
    df,
    invoice_number
):

    if (
        invoice_number is None
        or invoice_number.strip() == ""
    ):

        return df

    return df[

        df["Invoice Number"]

        .astype(str)

        .str.contains(

            invoice_number,

            case=False,

            na=False

        )

    ]


# ==========================================================
# OUTSTANDING ONLY
# ==========================================================

def outstanding_only(df):

    return df[

        df["Balance"] > 0

    ]


# ==========================================================
# OVERDUE ONLY
# ==========================================================

def overdue_only(df):

    return df[

        df["Invoice Status"]

        .str.lower()

        == "overdue"

    ]


# ==========================================================
# PAID ONLY
# ==========================================================

def paid_only(df):

    return df[

        df["Invoice Status"]

        .str.lower()

        == "closed"

    ]


# ==========================================================
# APPLY ALL FILTERS
# ==========================================================

def apply_filters(

    df,

    start_date=None,

    end_date=None,

    status="All",

    customer_search="",

    invoice_search="",

    outstanding=False,

    overdue=False,

    paid=False

):

    filtered = df.copy()

    filtered = filter_by_date(

        filtered,

        start_date,

        end_date

    )

    filtered = filter_by_status(

        filtered,

        status

    )

    filtered = filter_by_customer(

        filtered,

        customer_search

    )

    filtered = filter_by_invoice(

        filtered,

        invoice_search

    )

    if outstanding:

        filtered = outstanding_only(

            filtered

        )

    if overdue:

        filtered = overdue_only(

            filtered

        )

    if paid:

        filtered = paid_only(

            filtered

        )

    return filtered
