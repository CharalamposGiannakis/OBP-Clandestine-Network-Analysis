import streamlit as st
import pandas as pd
import numpy as np

from ui_components import apply_tactical_theme, COLOR_VOID, COLOR_WIRE, COLOR_STEEL, COLOR_ALERT

st.set_page_config(layout="wide")
apply_tactical_theme()

st.title("ROLES // CLASSIFICATION")
st.caption("SOCIAL ROLE ANALYSIS ENGINE")