"""
Global styling for the Streamlit dashboard.
"""

import streamlit as st

from config.colors import *


def load_css():

    st.markdown(
        f"""
<style>

/* ==========================================================
BACKGROUND
========================================================== */

.stApp {{
    background-color: {BACKGROUND};
    color: {TEXT};
}}


/* ==========================================================
HIDE STREAMLIT DEFAULTS
========================================================== */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}


/* ==========================================================
MAIN CONTAINER
========================================================== */

.block-container {{

    padding-top: 1.5rem;

    padding-bottom: 2rem;

}}


/* ==========================================================
HEADINGS
========================================================== */

h1, h2, h3, h4 {{

    color: {TEXT};

    font-weight: 700;

}}


/* ==========================================================
KPI CARD
========================================================== */

.kpi-card {{

    background: {CARD};

    border-left: 6px solid {PRIMARY};

    border-radius: 14px;

    padding: 18px;

    margin-bottom: 12px;

    box-shadow: 0 8px 20px rgba(0,0,0,0.18);

    transition: 0.25s;

}}

.kpi-card:hover {{

    background: {CARD_HOVER};

    transform: translateY(-3px);

}}

.kpi-title {{

    color: {TEXT_LIGHT};

    font-size: 14px;

    font-weight: 600;

}}

.kpi-value {{

    color: {TEXT};

    font-size: 30px;

    font-weight: bold;

    margin-top: 10px;

}}

.kpi-sub {{

    color: {TEXT_MUTED};

    font-size: 13px;

}}


/* ==========================================================
SECTION CARD
========================================================== */

.section-card {{

    background: {CARD};

    border-radius: 14px;

    padding: 18px;

    margin-top: 10px;

    margin-bottom: 20px;

}}


/* ==========================================================
TABLE
========================================================== */

div[data-testid="stDataFrame"] {{

    border-radius: 12px;

    overflow: hidden;

}}


/* ==========================================================
SIDEBAR
========================================================== */

section[data-testid="stSidebar"] {{

    background: {CARD};

}}

section[data-testid="stSidebar"] * {{

    color: {TEXT};

}}


/* ==========================================================
BUTTONS
========================================================== */

.stButton>button {{

    background: {PRIMARY};

    color: white;

    border-radius: 10px;

    border: none;

    font-weight: 600;

}}

.stButton>button:hover {{

    background: {SECONDARY};

}}


/* ==========================================================
METRICS
========================================================== */

div[data-testid="metric-container"] {{

    background: {CARD};

    border-radius: 12px;

    padding: 12px;

}}


/* ==========================================================
EXPANDERS
========================================================== */

.streamlit-expanderHeader {{

    font-size: 16px;

    font-weight: 600;

}}


/* ==========================================================
SUCCESS
========================================================== */

.success-card {{

    border-left: 6px solid {SUCCESS};

}}


/* ==========================================================
WARNING
========================================================== */

.warning-card {{

    border-left: 6px solid {WARNING};

}}


/* ==========================================================
DANGER
========================================================== */

.danger-card {{

    border-left: 6px solid {DANGER};

}}

</style>
""",
        unsafe_allow_html=True,
    )
