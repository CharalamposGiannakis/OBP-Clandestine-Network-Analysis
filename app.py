import streamlit as st

pg = st.navigation([
    st.Page("pages/0_welcome.py", title="Welcome"),
    st.Page("pages/1_members.py", title="Members"),
    st.Page("pages/2_roles.py", title="Roles")
])
pg.run()
