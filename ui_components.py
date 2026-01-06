import streamlit as st

# --- SYSTEM DESIGN PALETTE (GOTHAM BLUEPRINT) ---
COLOR_VOID  = "#090A0B"  # Deep background
COLOR_GRID  = "#1B1F23"  # Subtle grid lines
COLOR_WIRE  = "#30363D"  # Edge/Connection lines
COLOR_STEEL = "#444C56"  # Standard node color
COLOR_ALERT = "#F85149"  # High-value target color (Red)
COLOR_TEXT  = "#8B949E"  # Technical UI text color

def apply_tactical_theme():
    st.markdown(f"""
        <style>
        /* Main Background and Grid */
        .stApp {{
            background-color: {COLOR_VOID};
            background-image: 
                linear-gradient({COLOR_GRID} 1px, transparent 1px),
                linear-gradient(90deg, {COLOR_GRID} 1px, transparent 1px);
            background-size: 35px 35px;
        }}
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {{
            background-color: {COLOR_VOID} !important;
            border-right: 1px solid {COLOR_WIRE};
        }}

        /* Navigation Text Styling (No Ghosting) */
        [data-testid="stSidebarNav"] span {{
            color: {COLOR_TEXT} !important;
            font-family: 'Share Tech Mono', monospace !important;
            text-transform: uppercase !important;
            font-size: 14px !important;
            letter-spacing: 1px !important;
        }}

        /* Typography */
        h1, h2, h3 {{
            color: #FFFFFF !important;
            font-family: 'Share Tech Mono', monospace;
        }}
        
        .stCaption, p, li {{
            color: {COLOR_TEXT} !important;
        }}

        /* Clean up component borders */
        iframe {{ border: none !important; }}
        </style>
        """, unsafe_allow_html=True)