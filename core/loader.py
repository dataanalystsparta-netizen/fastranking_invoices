
"""
Loads and validates the invoice Excel file.
"""

import pandas as pd

from config.settings import REQUIRED_COLUMNS


# ==========================================================
# LOAD EXCEL
# ==========================================================

def load_excel(uploaded_file):
    """
    Load invoice Excel file and return cleaned dataframe.
    """

    df = pd.read_excel(uploaded_file)

    return clean_dataframe(df)


# ==========================================================
# VALIDATE REQUIRED COLUMNS
# ==========================================================

def validate_columns(df):

    missing = []

    for column in REQUIRED_COLUMNS:

        if column not in df.columns:
            missing.append(column)

    return missing


# ==========================================================
# CLEAN DATAFRAME
# ==========================================================

def clean_dataframe(df):

    # -------------------------
    # Strip spaces from columns
    # -------------------------

    df.columns = df.columns.str.strip()

    # -------------------------
    # Validate columns
    # -------------------------

    missing = validate_columns(df)

    if missing:

        raise ValueError(
            "Missing required columns:\n\n"
            + "\n".join(missing)
        )

    # -------------------------
    # Convert numeric columns
    # -------------------------

    numeric_columns = [
        "Total",
        "Balance"
    ]

    for column in numeric_columns:

        df[column] = (
            pd.to_numeric(
                df[column],
                errors="coerce"
            )
            .fillna(0)
        )

    # -------------------------
    # Convert dates
    # -------------------------

    date_columns = [
        "Invoice Date",
        "Due Date"
    ]

    for column in date_columns:

        df[column] = pd.to_datetime(
            df[column],
            dayfirst=True,
            errors="coerce"
        )

    # -------------------------
    # Paid Amount
    # -------------------------

    df["Paid Amount"] = (
        df["Total"] -
        df["Balance"]
    )

    # -------------------------
    # Remove empty customer names
    # -------------------------

    df["Customer Name"] = (
        df["Customer Name"]
        .fillna("Unknown Customer")
        .astype(str)
        .str.strip()
    )

    # -------------------------
    # Standardise status
    # -------------------------

    df["Invoice Status"] = (
        df["Invoice Status"]
        .fillna("Unknown")
        .astype(str)
        .str.title()
        .str.strip()
    )

    # -------------------------
    # Sort newest first
    # -------------------------

    df = df.sort_values(
        by="Invoice Date",
        ascending=False
    )

    df.reset_index(
        drop=True,
        inplace=True
    )

    return df


# ==========================================================
# SUMMARY
# ==========================================================

def get_file_summary(df):

    return {

        "rows": len(df),

        "customers": df["Customer Name"].nunique(),

        "invoice_total": df["Total"].sum(),

        "paid_total": df["Paid Amount"].sum(),

        "balance_total": df["Balance"].sum()

    }
