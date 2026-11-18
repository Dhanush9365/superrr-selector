
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# SUPERR SELECTOR - RAJASTHAN ROYALS
# ==========================================

st.set_page_config(
    page_title="SupeRR Selector | RR Scouting",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ROYAL THEME
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(145deg, #090d24 0%, #111936 55%, #1c1734 100%);
    color: white;
}

section[data-testid="stSidebar"] {
    background: #0b1029;
    border-right: 1px solid #343b5d;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.hero {
    padding: 32px;
    border-radius: 20px;
    background: linear-gradient(110deg, #c2185b, #651b72, #172653);
    border: 1px solid rgba(255,255,255,.18);
    margin-bottom: 25px;
}

.hero h1 {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 58px;
    font-weight: 800;
    margin: 0;
    color: white;
    letter-spacing: 2px;
}

.hero p {
    color: #f7dce9;
    font-size: 15px;
    letter-spacing: 3px;
}

.section-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 30px;
    font-weight: 700;
    color: #ff5b9c;
    margin-top: 15px;
}

.metric-card {
    background: linear-gradient(145deg, #1b2447, #111832);
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #41496b;
    min-height: 115px;
}

.metric-label {
    color: #b7bfdc;
    font-size: 12px;
    letter-spacing: 1px;
}

.metric-value {
    font-family: 'Barlow Condensed', sans-serif;
    color: white;
    font-size: 32px;
    font-weight: 700;
}

.player-card {
    background: linear-gradient(145deg, #222b50, #121a37);
    border: 1px solid #4a5277;
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 12px;
}

.player-name {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 25px;
    color: #ff6ba6;
    font-weight: 700;
}

.player-role {
    color: #c5cce4;
    font-size: 13px;
}

.note {
    background: #172343;
    border-left: 4px solid #ff4f91;
    padding: 14px;
    border-radius: 8px;
    color: #e4e8fa;
}

div.stButton > button {
    background: linear-gradient(90deg, #e91e63, #9c27b0);
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 700;
}

h1, h2, h3 {
    color: white;
}

[data-testid="stDataFrame"] {
    border: 1px solid #41496b;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# PLAYER SHORTLIST
# ==========================================

players = [
    ("Shai Hope", "West Indies", "Top-order Batter", "Batting"),
    ("Shimron Hetmyer", "West Indies", "Middle-order Batter", "Batting"),
    ("Amir Jangoo", "West Indies", "Wicketkeeper Batter", "Batting"),
    ("Tushar Raheja", "India", "Wicketkeeper Batter", "Batting"),
    ("Karan Lal", "India", "All-rounder", "All-rounder"),
    ("Shivalik Sharma", "India", "Middle-order Batter", "Batting"),
    ("Anmolpreet Singh", "India", "Top-order Batter", "Batting"),
    ("Nehal Wadhera", "India", "Middle-order Batter", "Batting"),
    ("Mitchell Owen", "Australia", "All-rounder", "All-rounder"),
    ("Tanmay Agarwal", "India", "Top-order Batter", "Batting"),
    ("Ben Stokes", "England", "All-rounder", "All-rounder"),
    ("Sikandar Raza", "Zimbabwe", "All-rounder", "All-rounder"),
    ("Michael Bracewell", "New Zealand", "All-rounder", "All-rounder"),
    ("Shamar Springer", "West Indies", "All-rounder", "All-rounder"),
    ("Deepak Chahar", "India", "Fast Bowler", "Bowling"),
    ("Trent Boult", "New Zealand", "Left-arm Fast Bowler", "Bowling"),
    ("Naman Tiwari", "India", "Left-arm Fast Bowler", "Bowling"),
    ("Raj Limbani", "India", "Fast Bowler", "Bowling"),
    ("Umran Malik", "India", "Fast Bowler", "Bowling"),
    ("Ishant Bhardwaj", "India", "Bowler", "Bowling")
]

player_df = pd.DataFrame(
    players,
    columns=["Player", "Country", "Role", "Category"]
)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("## 🏏 SUPERR SELECTOR")
st.sidebar.markdown("### RAJASTHAN ROYALS")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Batting Analytics",
        "Bowling Analytics",
        "Player Profiles",
        "Player Comparison",
        "RR Recommendations"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("ROUND 1 | PLAYER RELIABILITY")
st.sidebar.caption("Scouting Dashboard | 2026")

# ==========================================
# HERO
# ==========================================

st.markdown("""
<div class="hero">
    <p>RAJASTHAN ROYALS • SCOUTING INTELLIGENCE</p>
    <h1>SUPERR SELECTOR</h1>
    <h3>PLAYER RELIABILITY UNDER PRESSURE</h3>
    <p>DATA-DRIVEN TALENT IDENTIFICATION • ROUND 1</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# OVERVIEW
# ==========================================

if page == "Overview":

    st.markdown('<div class="section-title">SCOUTING OVERVIEW</div>',
                unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("SHORTLISTED PLAYERS", "20"),
        ("BATTER PROFILES", "10"),
        ("BOWLER PROFILES", "6"),
        ("DATA STATUS", "Pending")
    ]

    for col, (label, value) in zip([c1, c2, c3, c4], metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### 🎯 PROJECT OBJECTIVE")
    st.write(
        "Identify players who can perform reliably under high-pressure "
        "match situations. The scouting framework focuses on batting "
        "consistency, death-over bowling, pressure handling and role suitability."
    )

    st.markdown("### 📊 SCOUTING FRAMEWORK")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="player-card">
            <div class="player-name">BATTER EVALUATION</div>
            - Runs scored under pressure<br>
            - Strike rate under pressure<br>
            - Dismissal frequency<br>
            - Comparison with normal performance
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="player-card">
            <div class="player-name">BOWLER EVALUATION</div>
            - Economy under pressure<br>
            - Wickets taken<br>
            - Dot-ball percentage<br>
            - Comparison with normal performance
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📌 CURRENT DATA STATUS")
    st.warning(
        "The player shortlist is loaded. Verified ball-by-ball calculations "
        "and final reliability rankings have not yet been integrated. "
        "No placeholder statistics are presented as real results."
    )

    st.markdown("### PLAYER SHORTLIST")
    st.dataframe(player_df, use_container_width=True, hide_index=True)

# ==========================================
# BATTING ANALYTICS
# ==========================================

elif page == "Batting Analytics":

    st.markdown('<div class="section-title">BATTING INTELLIGENCE</div>',
                unsafe_allow_html=True)

    batters = player_df[player_df["Category"] == "Batting"]

    st.write("Explore the shortlisted batting candidates.")

    st.dataframe(batters, use_container_width=True, hide_index=True)

    st.info(
        "Pressure strike rates, runs, dismissals and baseline comparisons "
        "will appear here after the official match data is processed."
    )

    st.markdown("### EVALUATION PARAMETERS")
    st.write("- Pressure runs")
    st.write("- Pressure strike rate")
    st.write("- Balls faced")
    st.write("- Dismissals")
    st.write("- Performance compared with normal situations")

# ==========================================
# BOWLING ANALYTICS
# ==========================================

elif page == "Bowling Analytics":

    st.markdown('<div class="section-title">BOWLING INTELLIGENCE</div>',
                unsafe_allow_html=True)

    bowlers = player_df[player_df["Category"] == "Bowling"]

    st.dataframe(bowlers, use_container_width=True, hide_index=True)

    st.info(
        "Verified pressure economy, wickets, dot-ball percentage and "
        "baseline comparisons will be displayed after data processing."
    )

    st.markdown("### EVALUATION PARAMETERS")
    st.write("- Pressure overs")
    st.write("- Economy rate")
    st.write("- Wickets")
    st.write("- Dot-ball percentage")
    st.write("- Runs conceded compared with normal situations")

# ==========================================
# PLAYER PROFILES
# ==========================================

elif page == "Player Profiles":

    st.markdown('<div class="section-title">PLAYER SCOUTING PROFILES</div>',
                unsafe_allow_html=True)

    selected_player = st.selectbox(
        "Select a player",
        player_df["Player"].tolist()
    )

    player = player_df[player_df["Player"] == selected_player].iloc[0]

    st.markdown(f"""
    <div class="player-card">
        <div class="player-name">{player['Player']}</div>
        <h4>{player['Country']}</h4>
        <div class="player-role">{player['Role']}</div>
        <hr>
        <h4>SCOUTING PROFILE</h4>
        <p>Category: {player['Category']}</p>
        <p>Pressure reliability score: Pending verification</p>
        <p>Pressure performance: Awaiting data analysis</p>
        <p>Role suitability: Requires evaluation</p>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Player photographs and verified individual performance metrics "
        "can be added once the relevant source data is available."
    )

# ==========================================
# PLAYER COMPARISON
# ==========================================

elif page == "Player Comparison":

    st.markdown('<div class="section-title">HEAD-TO-HEAD COMPARISON</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        player1 = st.selectbox(
            "PLAYER 1",
            player_df["Player"].tolist(),
            key="p1"
        )

    with col2:
        player2 = st.selectbox(
            "PLAYER 2",
            player_df["Player"].tolist(),
            index=1,
            key="p2"
        )

    p1 = player_df[player_df["Player"] == player1].iloc[0]
    p2 = player_df[player_df["Player"] == player2].iloc[0]

    comparison = pd.DataFrame({
        "Attribute": ["Country", "Role", "Category"],
        player1: [p1["Country"], p1["Role"], p1["Category"]],
        player2: [p2["Country"], p2["Role"], p2["Category"]]
    })

    st.dataframe(comparison, use_container_width=True, hide_index=True)

    st.warning(
        "Performance comparison will be enabled when verified player statistics "
        "are integrated."
    )

# ==========================================
# RR RECOMMENDATIONS
# ==========================================

elif page == "RR Recommendations":

    st.markdown('<div class="section-title">RAJASTHAN ROYALS SCOUTING BOARD</div>',
                unsafe_allow_html=True)

    recommendations = [
        ("Shai Hope", "Top-order batting option",
         "Evaluate as a possible top-order or opening backup."),
        ("Shimron Hetmyer", "Middle-order power",
         "Consider as a middle-order retention or buy-back target."),
        ("Amir Jangoo", "Wicketkeeper batting option",
         "Assess his T20 middle-order suitability and finishing ability."),
        ("Michael Bracewell", "All-rounder option",
         "Evaluate his batting and off-spin contribution."),
        ("Trent Boult", "Left-arm fast bowling",
         "Assess as a new-ball and left-arm pace option."),
        ("Deepak Chahar", "Powerplay bowling",
         "Evaluate swing bowling and powerplay impact.")
    ]

    for name, role, reason in recommendations:
        st.markdown(f"""
        <div class="player-card">
            <div class="player-name">{name}</div>
            <b>{role}</b>
            <p>{reason}</p>
        </div>
        """, unsafe_allow_html=True)

    st.warning(
        "These are preliminary role-based scouting ideas, not final "
        "auction recommendations. Availability, price and performance "
        "must be verified."
    )

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")
st.markdown(
    "<center style='color:#aeb7d7;'>"
    "SUPERR SELECTOR | RAJASTHAN ROYALS SCOUTING PROJECT<br>"
    "PLAYER RELIABILITY UNDER PRESSURE | ROUND 1"
    "</center>",
    unsafe_allow_html=True
)
