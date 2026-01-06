import streamlit as st
from ui_components import apply_tactical_theme

st.set_page_config(page_title="DSS | Welcome", layout="wide")
apply_tactical_theme()

col_title, col_status = st.columns([3, 1])

with col_title:
    st.title("DECISION SUPPORT SYSTEM")
    st.caption("CLANDESTINE NETWORK ANALYSIS & OPTIMIZATION")

with col_status:
    st.markdown(f"""
        <div style="border: 1px solid #30363D; padding: 15px; background-color: rgba(17, 20, 24, 0.8);">
            <p style="margin:0; font-family: 'Share Tech Mono', monospace; font-size:12px; color:#58a6ff;">SYSTEM_STATUS: ACTIVE</p>
            <p style="margin:0; font-family: 'Share Tech Mono', monospace; font-size:12px; color:#8b949e;">OPERATOR: ADMIN</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("""### WELCOME, ANALYST
This system provides tactical insights into the identified clandestine network (N=62). 
Utilizing high-fidelity **Network Science** and **Mathematical Optimization**, 
this platform identifies critical nodes and organizational vulnerabilities.

#### // CURRENT_OBJECTIVES:
1. **IDENTIFY KEY PLAYERS**: Use Centrality measures (Degree, Eigenvector, Katz) to locate leadership hubs.
2. **COMMUNITY DETECTION**: Map distinct operational cells or "factions" within the topology.
3. **RESILIENCE ANALYSIS**: Measure network stability using the **Kemeny Constant**.
4. **DISRUPTION STRATEGY**: Optimize arrest protocols to maximize network degradation.
""")