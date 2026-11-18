import streamlit as st

st.set_page_config(
    page_title="SupeRR Selector",
    page_icon="🏏",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #10182D;
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
div[data-testid="stMetric"] {
    background: #202D49;
    padding: 18px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("🏏 SupeRR SELECTOR")
st.subheader("PLAYER RELIABILITY UNDER PRESSURE")
st.markdown("---")

st.sidebar.title("ROYAL SELECTOR")
page = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Batting Analytics",
        "Bowling Analytics",
        "Player Profiles",
        "Player Comparison",
        "RR Recommendations"
    ]
)

if page == "Overview":
    st.header("Royal Performance Centre")
    st.write("Welcome to the Rajasthan Royals scouting dashboard.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Batters", "Awaiting analysis")
    c2.metric("Bowlers", "Awaiting analysis")
    c3.metric("Dataset", "Not analysed")
    st.info("Verified competition statistics will appear here after dataset processing.")

elif page == "Batting Analytics":
    st.header("🏏 Batting Under Pressure")
    st.info("Player rankings will be populated from the competition dataset.")

elif page == "Bowling Analytics":
    st.header("🎯 Bowling Under Pressure")
    st.info("Bowler rankings will be populated from the competition dataset.")

elif page == "Player Profiles":
    st.header("⭐ Cinematic Player Profiles")
    st.info("Player portraits and verified statistics will appear here.")

elif page == "Player Comparison":
    st.header("⚔️ Player Comparison")
    st.info("Compare verified player performances here.")

elif page == "RR Recommendations":
    st.header("👑 Rajasthan Royals Scouting")
    st.info("Player recommendations and replacement analysis will appear here.")

st.markdown("---")
st.caption("SupeRR Selector | Rajasthan Royals Inspired Analytics")
