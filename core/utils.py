
"""
Common utility functions used throughout the application.
"""

from io import BytesIO
from datetime import datetime

import pandas as pd

from config.settings import (
    CURRENCY_SYMBOL,
    DATE_FORMAT
)

# ==========================================================
# CURRENCY
# ==========================================================

def format_currency(value):

    try:
        value = float(value)
    except:
        value = 0

    return f"{CURRENCY_SYMBOL}{value:,.2f}"


# ==========================================================
# DATE
# ==========================================================

def format_date(value):

    if pd.isna(value):
        return ""

    if isinstance(value, str):
        return value

    return value.strftime(DATE_FORMAT)


# ==========================================================
# SAFE DIVISION
# ==========================================================

def safe_divide(a, b):

    if b == 0:
        return 0

    return a / b


# ==========================================================
# PERCENTAGE
# ==========================================================

def percentage(part, total):

    return round(
        safe_divide(part, total) * 100,
        1
    )


# ==========================================================
# STATUS
# ==========================================================

# ==========================================================
# STATUS
# ==========================================================

def status_icon(status):

    if pd.isna(status):
        return ""

    status = str(status).strip()

    status_lower = status.lower()

    icons = {
        "closed": "🟢 Closed",
        "open": "🟠 Open",
        "overdue": "🔴 Overdue",
        "draft": "🟠 Draft",
        "void": "🟠 Void",
        "sent": "🟢 Sent",
        "paid": "🟢 Paid",
    }

    # Return matching icon if known
    if status_lower in icons:
        return icons[status_lower]

    # Otherwise return the original value instead of "Unknown"
    return status

# ==========================================================
# DAYS OVERDUE
# ==========================================================

def days_overdue(due_date):

    if pd.isna(due_date):
        return 0

    today = pd.Timestamp.today().normalize()

    delta = today - due_date.normalize()

    return max(delta.days, 0)


# ==========================================================
# EXPORT TO EXCEL
# ==========================================================

def dataframe_to_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False
        )

    output.seek(0)

    return output


# ==========================================================
# EXPORT TO CSV
# ==========================================================

def dataframe_to_csv(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")


# ==========================================================
# TODAY
# ==========================================================

def today():

    return datetime.now().strftime(DATE_FORMAT)


# ==========================================================
# FORMAT INVOICE TABLE
# ==========================================================

def format_invoice_table(df):

    table = df.copy()

    if "Invoice Date" in table.columns:
        table["Invoice Date"] = table["Invoice Date"].apply(format_date)

    if "Due Date" in table.columns:
        table["Due Date"] = table["Due Date"].apply(format_date)

    if "Total" in table.columns:
        table["Total"] = table["Total"].apply(format_currency)

    if "Balance" in table.columns:
        table["Balance"] = table["Balance"].apply(format_currency)

    if "Paid Amount" in table.columns:
        table["Paid Amount"] = table["Paid Amount"].apply(format_currency)

    if "Invoice Status" in table.columns:
        table["Invoice Status"] = table["Invoice Status"].apply(status_icon)

    return table
