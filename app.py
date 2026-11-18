
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# SUPERR SELECTOR | RAJASTHAN ROYALS SCOUTING DASHBOARD
# ==========================================================

st.set_page_config(
    page_title="SupeRR Selector | Rajasthan Royals",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# PLAYER SHORTLIST
# ==========================================================

players = [
    {"Player": "Shai Hope", "Country": "West Indies", "Role": "Top-order Batter", "Category": "Batting"},
    {"Player": "Shimron Hetmyer", "Country": "West Indies", "Role": "Middle-order Batter", "Category": "Batting"},
    {"Player": "Amir Jangoo", "Country": "West Indies", "Role": "Wicketkeeper Batter", "Category": "Batting"},
    {"Player": "Shahrukh Khan", "Country": "India", "Role": "Middle-order Batter / Finisher", "Category": "Batting"},
    {"Player": "Nitish Rana", "Country": "India", "Role": "Top / Middle-order Batter", "Category": "Batting"},
    {"Player": "Shivalik Sharma", "Country": "India", "Role": "Middle-order Batter", "Category": "Batting"},
    {"Player": "Anmolpreet Singh", "Country": "India", "Role": "Top-order Batter", "Category": "Batting"},
    {"Player": "Nehal Wadhera", "Country": "India", "Role": "Middle-order Batter", "Category": "Batting"},
    {"Player": "Mitchell Owen", "Country": "Australia", "Role": "All-rounder", "Category": "All-rounder"},
    {"Player": "Karun Nair", "Country": "India", "Role": "Top-order Batter", "Category": "Batting"},
    {"Player": "Ben Stokes", "Country": "England", "Role": "All-rounder", "Category": "All-rounder"},
    {"Player": "Sikandar Raza", "Country": "Zimbabwe", "Role": "All-rounder", "Category": "All-rounder"},
    {"Player": "Michael Bracewell", "Country": "New Zealand", "Role": "All-rounder", "Category": "All-rounder"},
    {"Player": "Shamar Springer", "Country": "West Indies", "Role": "All-rounder", "Category": "All-rounder"},
    {"Player": "Deepak Chahar", "Country": "India", "Role": "Fast Bowler", "Category": "Bowling"},
    {"Player": "Trent Boult", "Country": "New Zealand", "Role": "Left-arm Fast Bowler", "Category": "Bowling"},
    {"Player": "Naman Tiwari", "Country": "India", "Role": "Left-arm Fast Bowler", "Category": "Bowling"},
    {"Player": "Matheesha Pathirana", "Country": "Sri Lanka", "Role": "Fast Bowler", "Category": "Bowling"},
    {"Player": "Umran Malik", "Country": "India", "Role": "Fast Bowler", "Category": "Bowling"},
    {"Player": "Avesh Khan", "Country": "India", "Role": "Fast Bowler", "Category": "Bowling"},
]

df = pd.DataFrame(players)

# ==========================================================
# THEME AND CSS
# ==========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #080d1b 0%, #10172b 55%, #171126 100%);
    color: #f4f5fa;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] {
    background: #0a1020;
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: #f4f5fa;
}

h1, h2, h3 {
    font-family: 'Barlow Condensed', sans-serif !important;
    letter-spacing: 1px;
}

.hero {
    background: linear-gradient(115deg, #171c35, #3a1235 65%, #8c174e);
    padding: 32px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 24px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin: 0;
    color: white;
}

.hero p {
    color: #f5c6dc;
    font-size: 15px;
    margin-bottom: 0;
}

.metric-card {
    background: linear-gradient(145deg, #171f35, #22213b);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 14px;
    padding: 20px;
    min-height: 112px;
}

.metric-label {
    color: #b8bfd0;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
}

.metric-value {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 36px;
    font-weight: 800;
    color: #ff4f9a;
    margin-top: 4px;
}

.section-title {
    color: #ff5b9e;
    font-size: 27px;
    font-weight: 800;
    margin-top: 18px;
    margin-bottom: 12px;
}

.info-card {
    background: #151d31;
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 13px;
    padding: 18px;
    margin-bottom: 12px;
}

.small-muted {
    color: #aeb8ca;
    font-size: 13px;
}

div[data-testid="stMetric"] {
    background: #171f35;
    border: 1px solid rgba(255,255,255,0.10);
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stMetric"] label {
    color: #c5cbd8 !important;
}

div[data-testid="stMetricValue"] {
    color: #ff5b9e !important;
}

.stButton button {
    background: linear-gradient(90deg, #ed287c, #ff5b9e);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 700;
}

.stButton button:hover {
    border: 1px solid white;
    color: white;
}

[data-testid="stDataFrame"] {
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 10px;
}

hr {
    border-color: rgba(255,255,255,0.12);
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================

st.sidebar.markdown("## 🏏 SUPERR SELECTOR")
st.sidebar.caption("RAJASTHAN ROYALS | SCOUTING INTELLIGENCE")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Batting Analytics",
        "Bowling Analytics",
        "Player Profiles",
        "Player Comparison"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### SCOUTING SHORTLIST")
st.sidebar.metric("Players shortlisted", len(df))
st.sidebar.caption("Scouting analysis dashboard")

# ==========================================================
# REUSABLE COMPONENTS
# ==========================================================

def hero(title, subtitle):
    st.markdown(f"""
    <div class="hero">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def metric_card(label, value):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)


# ==========================================================
# OVERVIEW
# ==========================================================

if page == "Overview":

    hero(
        "SUPERR SELECTOR",
        "A data-informed player scouting dashboard for Rajasthan Royals"
    )

    st.markdown('<div class="section-title">SCOUTING OVERVIEW</div>',
                unsafe_allow_html=True)

    batting_count = len(df[df["Category"] == "Batting"])
    bowling_count = len(df[df["Category"] == "Bowling"])
    allrounder_count = len(df[df["Category"] == "All-rounder"])

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("TOTAL SHORTLIST", len(df))
    with c2:
        metric_card("BATTERS", batting_count)
    with c3:
        metric_card("ALL-ROUNDERS", allrounder_count)
    with c4:
        metric_card("BOWLERS", bowling_count)

    st.markdown("---")

    left, right = st.columns([1.1, 0.9])

    with left:
        st.markdown('<div class="section-title">PLAYER DISTRIBUTION</div>',
                    unsafe_allow_html=True)

        category_data = (
            df["Category"].value_counts()
            .rename_axis("Category")
            .reset_index(name="Players")
        )

        fig = px.pie(
            category_data,
            names="Category",
            values="Players",
            hole=0.58,
            title="Shortlist by player category"
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white",
            legend_title_text=""
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown('<div class="section-title">SCOUTING FOCUS</div>',
                    unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
            <h3>🏏 Batting depth</h3>
            <p class="small-muted">
            Assess top-order stability, middle-order flexibility,
            finishing ability and wicketkeeping options.
            </p>
        </div>
        <div class="info-card">
            <h3>⚡ All-round capabilities</h3>
            <p class="small-muted">
            Evaluate players who can contribute with both bat
            and ball and provide team balance.
            </p>
        </div>
        <div class="info-card">
            <h3>🎯 Bowling resources</h3>
            <p class="small-muted">
            Examine pace options, left-arm variation,
            death-over execution and powerplay skills.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">CURRENT SHORTLIST</div>',
                unsafe_allow_html=True)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

# ==========================================================
# BATTING ANALYTICS
# ==========================================================

elif page == "Batting Analytics":

    hero(
        "BATTING ANALYTICS",
        "Evaluating batting roles, consistency and match impact"
    )

    batters = df[df["Category"] == "Batting"].copy()

    st.markdown('<div class="section-title">BATTING SHORTLIST</div>',
                unsafe_allow_html=True)

    st.metric("Players in batting category", len(batters))

    st.dataframe(
        batters[["Player", "Country", "Role"]],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")
    st.markdown('<div class="section-title">BATTING EVALUATION FRAMEWORK</div>',
                unsafe_allow_html=True)

    batting_parameters = pd.DataFrame({
        "Parameter": [
            "Batting Average",
            "Strike Rate",
            "Boundary Percentage",
            "Dot Ball Percentage",
            "Powerplay Performance",
            "Middle-over Performance",
            "Death-over Performance",
            "Performance Under Pressure"
        ],
        "Scouting Purpose": [
            "Measures scoring consistency",
            "Measures scoring speed",
            "Evaluates boundary-scoring ability",
            "Identifies scoring pressure",
            "Evaluates powerplay contribution",
            "Measures middle-over stability",
            "Assesses finishing contribution",
            "Evaluates performance in difficult situations"
        ]
    })

    st.dataframe(
        batting_parameters,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "These are the evaluation parameters used in the scouting framework. "
        "Actual player-level batting statistics are not calculated in this version."
    )

# ==========================================================
# BOWLING ANALYTICS
# ==========================================================

elif page == "Bowling Analytics":

    hero(
        "BOWLING ANALYTICS",
        "Evaluating pace resources, wicket-taking ability and control"
    )

    bowlers = df[df["Category"] == "Bowling"].copy()

    st.markdown('<div class="section-title">BOWLING SHORTLIST</div>',
                unsafe_allow_html=True)

    st.metric("Players in bowling category", len(bowlers))

    st.dataframe(
        bowlers[["Player", "Country", "Role"]],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")
    st.markdown('<div class="section-title">BOWLING EVALUATION FRAMEWORK</div>',
                unsafe_allow_html=True)

    bowling_parameters = pd.DataFrame({
        "Parameter": [
            "Bowling Average",
            "Economy Rate",
            "Strike Rate",
            "Dot Ball Percentage",
            "Powerplay Economy",
            "Middle-over Control",
            "Death-over Economy",
            "Wicket-taking Ability",
            "Variation and Execution"
        ],
        "Scouting Purpose": [
            "Measures runs conceded per wicket",
            "Evaluates run-control ability",
            "Measures frequency of wickets",
            "Identifies pressure-building ability",
            "Evaluates early-over effectiveness",
            "Assesses control during middle overs",
            "Measures performance at the death",
            "Evaluates wicket-taking threat",
            "Assesses tactical bowling options"
        ]
    })

    st.dataframe(
        bowling_parameters,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "These are the evaluation parameters used in the scouting framework. "
        "Actual player-level bowling statistics are not calculated in this version."
    )

# ==========================================================
# PLAYER PROFILES
# ==========================================================

elif page == "Player Profiles":

    hero(
        "PLAYER PROFILES",
        "Explore the shortlisted players and their cricketing roles"
    )

    selected_player = st.selectbox(
        "Select a player",
        df["Player"].tolist()
    )

    player = df[df["Player"] == selected_player].iloc[0]

    st.markdown("---")
    st.markdown('<div class="section-title">PLAYER INFORMATION</div>',
                unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])

    with c1:
        st.markdown("""
        <div class="info-card" style="text-align:center;">
            <div style="font-size:70px;">🏏</div>
            <h2 style="color:#ff5b9e;">PLAYER PROFILE</h2>
            <p class="small-muted">Rajasthan Royals Scouting</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"## {player['Player']}")
        st.write(f"**Country:** {player['Country']}")
        st.write(f"**Playing Role:** {player['Role']}")
        st.write(f"**Scouting Category:** {player['Category']}")

        st.markdown("---")
        st.markdown("### Scouting considerations")

        if player["Category"] == "Batting":
            st.write(
                "- Batting consistency and scoring options\n"
                "- Ability to adapt to different match situations\n"
                "- Strike rotation and boundary potential\n"
                "- Role flexibility within the batting order"
            )

        elif player["Category"] == "Bowling":
            st.write(
                "- Wicket-taking ability\n"
                "- Economy and control\n"
                "- Powerplay and death-over suitability\n"
                "- Bowling variations and execution"
            )

        else:
            st.write(
                "- Contribution with both bat and ball\n"
                "- Team balance and role flexibility\n"
                "- Match-up suitability\n"
                "- Ability to influence different phases"
            )

    st.markdown("---")
    st.caption(
        "Profile information is based on the current scouting shortlist. "
        "Detailed verified player statistics and career records are not included here."
    )

# ==========================================================
# PLAYER COMPARISON
# ==========================================================

elif page == "Player Comparison":

    hero(
        "PLAYER COMPARISON",
        "Compare shortlisted players by role, country and scouting category"
    )

    col1, col2 = st.columns(2)

    with col1:
        player_one = st.selectbox(
            "Select first player",
            df["Player"].tolist(),
            key="player_one"
        )

    with col2:
        player_two = st.selectbox(
            "Select second player",
            df["Player"].tolist(),
            index=1,
            key="player_two"
        )

    first = df[df["Player"] == player_one].iloc[0]
    second = df[df["Player"] == player_two].iloc[0]

    st.markdown("---")
    st.markdown('<div class="section-title">HEAD-TO-HEAD COMPARISON</div>',
                unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(f"### 🏏 {first['Player']}")
        st.markdown(f"""
        <div class="info-card">
            <p><b>Country:</b> {first['Country']}</p>
            <p><b>Role:</b> {first['Role']}</p>
            <p><b>Category:</b> {first['Category']}</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"### 🏏 {second['Player']}")
        st.markdown(f"""
        <div class="info-card">
            <p><b>Country:</b> {second['Country']}</p>
            <p><b>Role:</b> {second['Role']}</p>
            <p><b>Category:</b> {second['Category']}</p>
        </div>
        """, unsafe_allow_html=True)

    comparison = pd.DataFrame({
        "Comparison": ["Country", "Playing Role", "Category"],
        player_one: [
            first["Country"],
            first["Role"],
            first["Category"]
        ],
        player_two: [
            second["Country"],
            second["Role"],
            second["Category"]
        ]
    })

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    if player_one == player_two:
        st.warning("You have selected the same player twice.")
    elif first["Category"] == second["Category"]:
        st.success(
            "Both players belong to the same scouting category. "
            "Compare their specific roles and suitability for the team."
        )
    else:
        st.info(
            "These players belong to different scouting categories "
            "and may serve different team requirements."
        )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; padding:12px; color:#9ba6bb;">
        <b style="color:#ff5b9e;">SUPERR SELECTOR</b><br>
        Rajasthan Royals | Player Scouting Intelligence<br>
        <span style="font-size:11px;">
        Independent scouting dashboard
        </span>
    </div>
    """,
    unsafe_allow_html=True
)
