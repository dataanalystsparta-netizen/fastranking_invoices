"""
Application-wide settings.

Change values here instead of hardcoding them
throughout the application.
"""

# ==========================================================
# APPLICATION
# ==========================================================

APP_NAME = "FastRanking Accounts Receivable"

APP_SHORT_NAME = "FastRanking AR"

APP_SUBTITLE = "Invoice & Payment Analytics Dashboard"

VERSION = "2.0.0"

# ==========================================================
# COMPANY
# ==========================================================

COMPANY_NAME = "FastRanking"

# ==========================================================
# CURRENCY
# ==========================================================

CURRENCY_SYMBOL = "£"

CURRENCY_CODE = "GBP"

# ==========================================================
# DATE FORMAT
# ==========================================================

DATE_FORMAT = "%d/%m/%Y"

# ==========================================================
# TABLE SETTINGS
# ==========================================================

DEFAULT_PAGE_SIZE = 25

TOP_CUSTOMERS = 10

# ==========================================================
# DASHBOARD
# ==========================================================

SHOW_OVERDUE_ALERTS = True

SHOW_MONTHLY_CHART = True

SHOW_TOP_CUSTOMERS = True

SHOW_PAID_DUE_CHART = True

# ==========================================================
# EXCEL SETTINGS
# ==========================================================

REQUIRED_COLUMNS = [
    "Invoice Date",
    "Invoice Number",
    "Invoice Status",
    "Customer Name",
    "Due Date",
    "Total",
    "Balance"
]
