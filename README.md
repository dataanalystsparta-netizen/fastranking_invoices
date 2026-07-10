# FastRanking Accounts Receivable

A modern Streamlit dashboard for analysing invoices, payments and outstanding balances.

---

## Features

- 📊 Executive KPI Dashboard
- 💷 Total Invoice / Paid / Outstanding
- 📅 Date Range Filtering
- 🏢 Customer Summary
- 📄 Customer Invoice Details
- 📈 Monthly Revenue Trends
- 🍩 Paid vs Outstanding Analysis
- 🚨 Action Centre
- 📤 Excel Upload
- 📥 Excel Export

---

## Technologies

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL

---

## Project Structure

```
InvoiceDashboard/

app.py

config/
colors.py
settings.py

core/
loader.py
calculations.py
filters.py
utils.py

ui/
styles.py
cards.py
charts.py
customer_table.py
customer_details.py
alerts.py
```

---

## Installation

```bash
pip install -r requirements.txt
```

Run locally:

```bash
streamlit run app.py
```

---

## Deployment

Deploy directly from GitHub using Streamlit Community Cloud.

---

## Version

Current Version: **2.0.0**
