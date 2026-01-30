import streamlit as st
import networkx as nx
# Import the logic functions
from src.data_manager import load_repository_data, parse_mtx
from ui_components import apply_tactical_theme

def df_to_graph(edge_df, n_nodes=None):
    """
    Builds an undirected NetworkX graph from an edge list DataFrame.
    """
    # pick endpoint columns
    if "source" in edge_df.columns and "target" in edge_df.columns:
        s_col, t_col = "source", "target"
    else:
        s_col, t_col = edge_df.columns[0], edge_df.columns[1]

    weighted = "weight" in edge_df.columns

    G = nx.Graph()

    # optionally pre-add nodes (helps if isolated nodes exist)
    if n_nodes is not None:
        G.add_nodes_from(range(n_nodes))

    if weighted:
        for s, t, w in edge_df[[s_col, t_col, "weight"]].itertuples(index=False):
            if int(s) != int(t):
                G.add_edge(int(s), int(t), weight=float(w))
    else:
        for s, t in edge_df[[s_col, t_col]].itertuples(index=False):
            if int(s) != int(t):
                G.add_edge(int(s), int(t), weight=1.0)

    return G

# --- Page Config ---
st.set_page_config(page_title="Data Importing Tool", layout="wide")
apply_tactical_theme()

# --- 1. RUN LOGIC ---
# This one line handles scanning the folder and updating the registry
load_repository_data("data")

# --- Header Section ---
col_title, col_status = st.columns([3, 1])

with col_title:
    st.title("DATA IMPORTING TOOL")
    st.caption("Upload, validate, and activate network datasets for system-wide analysis.")

with col_status:
    count = len(st.session_state.get('data_registry', {}))
    st.markdown(f"""
<div style="
    border: 1px solid #30363d; 
    padding: 15px; 
    border-radius: 6px; 
    background-color: #0d1117;
    text-align: right;">
    <div style="font-size: 12px; color: #8b949e; margin-bottom: 4px;">SYSTEM STATUS</div>
    <div style="font-size: 16px; font-weight: 600; color: #58a6ff;">{count} DATASETS LOADED</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# --- Main Interface ---
col_upload, col_select = st.columns([1, 1])

# ==========================================
# LEFT: UPLOADER
# ==========================================
with col_upload:
    with st.container(border=True):
        st.subheader("Data Upload")
        st.caption("System accepts verified Matrix Market (.mtx) formats only.")
        
        uploaded_files = st.file_uploader(
            "Select Intel Files", 
            type=['mtx'], 
            accept_multiple_files=True,
            label_visibility="collapsed"
        )

        if uploaded_files:
            new_count = 0
            if 'data_registry' not in st.session_state:
                st.session_state['data_registry'] = {}

            for file in uploaded_files:
                if file.name not in st.session_state['data_registry']:
                    data_pack = parse_mtx(file, file.name, "UPLOAD")
                    
                    if data_pack:
                        st.session_state['data_registry'][file.name] = data_pack
                        new_count += 1
                    else:
                        st.error(f"Failed to parse {file.name}")
            
            if new_count > 0:
                st.rerun()

# ==========================================
# RIGHT: SELECTOR
# ==========================================
with col_select:
    with st.container(border=True):
        st.subheader("Active Operation Data")
        
        if not st.session_state.get('data_registry'):
            st.warning("NO DATA AVAILABLE")
        else:
            options = list(st.session_state['data_registry'].keys())
            
            # Smart Indexing
            index = 0
            if 'data_source' in st.session_state and st.session_state['data_source'] in options:
                index = options.index(st.session_state['data_source'])

            selected_name = st.selectbox("Select Dataset", options, index=index)

            if selected_name:
                # Activate the selection
                data_pack = st.session_state['data_registry'][selected_name]
                st.session_state['network_data'] = data_pack['df']
                st.session_state['network_shape'] = data_pack['shape']
                st.session_state['data_source'] = data_pack['name']
                n_nodes = data_pack["shape"][0]
                # Build graph object for accurate metrics
                G_obj = df_to_graph(data_pack["df"], n_nodes=n_nodes)
                st.session_state["network_graph"] = G_obj

                st.divider()
                
                # Source Badge
                src_type = data_pack.get('type', 'UNKNOWN')
                st.markdown(f"<p style='font-family: \"Share Tech Mono\", monospace; color:#8b949e; font-size:12px;'>DATA ORIGIN: <span style='color:#58a6ff;'>[{src_type}]</span></p>", unsafe_allow_html=True)
                st.success(f"DATA ACTIVE: {selected_name}")
                
                m1, m2 = st.columns(2)
                m1.metric("Nodes", data_pack['shape'][0])
                m2.metric("Connections", G_obj.number_of_edges())
                
                if st.button("Purge Registry", type="primary", use_container_width=True):
                    st.session_state['data_registry'] = {}
                    if 'network_data' in st.session_state:
                        del st.session_state['network_data']
                    st.rerun()
    
    # Help Expander
    with st.expander("DATA STRUCTURE SPECIFICATION"):
        st.markdown("**REQUIRED FORMAT: Matrix Market (.mtx)**")
        template_data = """%%MatrixMarket matrix coordinate pattern symmetric
        6 6 7
        1 2
        2 3
        3 4
        4 5
        5 6
        6 1
        2 5
        """
        st.download_button(
            label="DOWNLOAD TEMPLATE", 
            data=template_data, 
            file_name="template.mtx",
            mime="text/plain"
        )