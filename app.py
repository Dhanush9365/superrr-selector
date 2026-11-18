
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import html

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="SupeRR Selector | RR Scouting",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

# =====================================================
# THEME
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

.stApp {
    background: #080d19;
    color: #f5f5f7;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] {
    background: #111a2d;
    border-right: 1px solid #28334a;
}

.hero {
    background: linear-gradient(110deg,#111a2d,#29203b,#6d1744);
    padding: 34px;
    border-radius: 18px;
    border: 1px solid #57304f;
    margin-bottom: 24px;
}

.hero h1 {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 48px;
    font-weight: 800;
    margin: 0;
    color: white;
}

.hero p {
    color: #e5cbd9;
    font-size: 15px;
}

.section-title {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 30px;
    font-weight: 700;
    color: #ff4d91;
    margin: 20px 0 12px 0;
}

.metric-card {
    background: #141f33;
    border: 1px solid #2b3b56;
    border-radius: 13px;
    padding: 19px;
    min-height: 105px;
}

.metric-label {
    color: #aab7ca;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.metric-value {
    color: white;
    font-size: 27px;
    font-weight: 700;
    margin-top: 8px;
}

.info-card {
    background: #121d30;
    border-left: 4px solid #ff4d91;
    padding: 17px;
    border-radius: 8px;
    margin-bottom: 12px;
}

div.stButton > button {
    background: #ec287c;
    color: white;
    border: 0;
    border-radius: 9px;
    font-weight: 700;
}

h1, h2, h3 {
    font-family: 'Barlow Condensed', sans-serif;
}

[data-testid="stDataFrame"] {
    border: 1px solid #2b3b56;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# DATA LOADING
# =====================================================

FILE_NAMES = {
    "ball_by_ball": "ball_by_ball.csv",
    "matches": "matches.csv",
    "competition": "competition.csv",
    "teams": "teams.csv",
    "playing_eleven": "playing_eleven.csv",
    "player_mapping": "competition_team_player_mapping.csv"
}

@st.cache_data(show_spinner=False)
def load_csv(path):
    try:
        return pd.read_csv(path, low_memory=False)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1", low_memory=False)
    except Exception:
        return pd.DataFrame()

def load_all_data():
    data = {}
    for key, filename in FILE_NAMES.items():
        path = DATA_DIR / filename
        if path.exists():
            data[key] = load_csv(path)
        else:
            data[key] = pd.DataFrame()
    return data

data = load_all_data()

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def clean_columns(df):
    df = df.copy()
    df.columns = [
        str(c).strip().lower().replace(" ", "_")
        for c in df.columns
    ]
    return df

data = {
    key: clean_columns(df)
    for key, df in data.items()
}

def find_column(df, candidates):
    if df.empty:
        return None

    for candidate in candidates:
        if candidate in df.columns:
            return candidate

    for col in df.columns:
        for candidate in candidates:
            if candidate in col:
                return col

    return None

def safe_number(value):
    try:
        return f"{int(value):,}"
    except Exception:
        return "—"

def metric_card(label, value):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{html.escape(str(label))}</div>
        <div class="metric-value">{html.escape(str(value))}</div>
    </div>
    """, unsafe_allow_html=True)

def section(title):
    st.markdown(
        f'<div class="section-title">{html.escape(title)}</div>',
        unsafe_allow_html=True
    )

# =====================================================
# PLAYER DATA DISCOVERY
# =====================================================

PLAYER_CANDIDATES = [
    "player_name",
    "player",
    "batter",
    "batsman",
    "bowler",
    "name",
    "full_name",
    "cricketer"
]

def get_player_names():
    names = set()

    for key in [
        "player_mapping",
        "playing_eleven",
        "ball_by_ball"
    ]:
        df = data[key]
        col = find_column(df, PLAYER_CANDIDATES)

        if col:
            values = df[col].dropna().astype(str).str.strip()
            names.update(x for x in values if x and x.lower() != "nan")

    return sorted(names)

players = get_player_names()

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:
    st.markdown("## 🏏 SupeRR Selector")
    st.caption("RAJASTHAN ROYALS SCOUTING")

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Explore Players",
            "Batting Analysis",
            "Bowling Analysis",
            "Player Profiles",
            "Player Comparison",
            "RR Scouting Notes",
            "Data Health"
        ]
    )

    st.markdown("---")
    st.caption("ROUND 1 | PLAYER RELIABILITY UNDER PRESSURE")
    st.caption("Built for Rajasthan Royals scouting")

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero">
    <h1>SUPERR SELECTOR</h1>
    <p>RAJASTHAN ROYALS | PLAYER SCOUTING & PERFORMANCE ANALYSIS</p>
    <p>Discover player performances. Explore match data. Evaluate reliability under pressure.</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# OVERVIEW
# =====================================================

if page == "Overview":

    section("SCOUTING OVERVIEW")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Players identified", safe_number(len(players)))

    with c2:
        metric_card("Matches available", safe_number(len(data["matches"])))

    with c3:
        metric_card("Ball-by-ball records", safe_number(len(data["ball_by_ball"])))

    with c4:
        loaded = sum(not df.empty for df in data.values())
        metric_card("Datasets loaded", f"{loaded}/6")

    st.markdown("---")

    section("SCOUTING OBJECTIVES")

    a, b = st.columns(2)

    with a:
        st.markdown("""
        <div class="info-card">
        <h3>🏏 Batting Reliability</h3>
        Examine batting performances, scoring patterns,
        innings contribution and available match situations.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
        <h3>🎯 Bowling Reliability</h3>
        Explore bowling performances, wickets, runs conceded
        and available over-by-over information.
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="info-card">
        <h3>📊 Player Profiles</h3>
        Explore individual player records and available
        performance information.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
        <h3>🔍 Scouting Comparison</h3>
        Compare selected players using the actual fields
        available in the competition dataset.
        </div>
        """, unsafe_allow_html=True)

    section("DATASET SNAPSHOT")

    for key, df in data.items():
        with st.expander(f"{FILE_NAMES[key]} — {len(df):,} rows"):
            if df.empty:
                st.warning("Dataset not found or could not be loaded.")
            else:
                st.write("Columns:", ", ".join(df.columns))
                st.dataframe(df.head(5), use_container_width=True)

# =====================================================
# EXPLORE PLAYERS
# =====================================================

elif page == "Explore Players":

    section("EXPLORE THE PLAYER DATABASE")

    if not players:
        st.warning("No player-name column was detected. Check Data Health.")
    else:
        search = st.text_input("Search player by name")

        filtered = [
            p for p in players
            if search.lower() in p.lower()
        ]

        st.caption(f"{len(filtered)} players found")

        cols = st.columns(3)

        for i, player in enumerate(filtered):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">PLAYER PROFILE</div>
                    <div class="metric-value" style="font-size:20px">
                    {html.escape(player)}
                    </div>
                </div>
                """, unsafe_allow_html=True)

# =====================================================
# BATTING ANALYSIS
# =====================================================

elif page == "Batting Analysis":

    section("BATTING PERFORMANCE ANALYSIS")

    df = data["ball_by_ball"]

    if df.empty:
        st.warning("Ball-by-ball dataset is unavailable.")
    else:
        batter_col = find_column(
            df, ["batter", "batsman", "striker", "batter_name"]
        )
        runs_col = find_column(
            df, ["batter_runs", "batsman_runs", "runs_batter", "runs_off_bat"]
        )
        match_col = find_column(
            df, ["match_id", "game_id"]
        )

        st.write("Available batting dataset columns:")
        st.write(", ".join(df.columns))

        if batter_col:
            names = sorted(
                df[batter_col].dropna().astype(str).unique()
            )

            selected = st.selectbox("Select batter", names)

            player_df = df[
                df[batter_col].astype(str) == selected
            ].copy()

            c1, c2 = st.columns(2)

            with c1:
                metric_card("Recorded batting deliveries",
                            safe_number(len(player_df)))

            with c2:
                if runs_col:
                    runs = pd.to_numeric(
                        player_df[runs_col], errors="coerce"
                    ).sum()
                    metric_card("Batter runs", safe_number(runs))
                else:
                    metric_card("Batter runs", "Column unavailable")

            if runs_col:
                player_df[runs_col] = pd.to_numeric(
                    player_df[runs_col], errors="coerce"
                )
                st.subheader("Runs recorded per delivery")
                st.line_chart(player_df[runs_col].reset_index(drop=True))

            st.subheader("Player delivery records")
            st.dataframe(player_df, use_container_width=True)

            st.info(
                "Pressure-specific batting statistics are not calculated "
                "until match situation and innings fields are verified."
            )
        else:
            st.warning("Could not identify the batter column automatically.")

# =====================================================
# BOWLING ANALYSIS
# =====================================================

elif page == "Bowling Analysis":

    section("BOWLING PERFORMANCE ANALYSIS")

    df = data["ball_by_ball"]

    if df.empty:
        st.warning("Ball-by-ball dataset is unavailable.")
    else:
        bowler_col = find_column(
            df, ["bowler", "bowler_name"]
        )

        st.write("Available bowling dataset columns:")
        st.write(", ".join(df.columns))

        if bowler_col:
            names = sorted(
                df[bowler_col].dropna().astype(str).unique()
            )

            selected = st.selectbox("Select bowler", names)

            player_df = df[
                df[bowler_col].astype(str) == selected
            ].copy()

            c1, c2 = st.columns(2)

            with c1:
                metric_card("Recorded deliveries",
                            safe_number(len(player_df)))

            with c2:
                metric_card("Matches represented",
                            safe_number(
                                player_df[
                                    find_column(player_df, ["match_id", "game_id"])
                                ].nunique()
                            ) if find_column(player_df, ["match_id", "game_id"])
                            else "Unavailable")

            st.subheader("Bowling delivery records")
            st.dataframe(player_df, use_container_width=True)

            st.info(
                "Economy, legal-ball counts and wicket calculations "
                "require verification of extras and dismissal columns."
            )
        else:
            st.warning("Could not identify the bowler column automatically.")

# =====================================================
# PLAYER PROFILES
# =====================================================

elif page == "Player Profiles":

    section("INDIVIDUAL PLAYER PROFILE")

    if not players:
        st.warning("Player names could not be detected.")
    else:
        selected = st.selectbox("Choose a player", players)

        found = False

        for key in ["player_mapping", "playing_eleven", "ball_by_ball"]:
            df = data[key]
            col = find_column(df, PLAYER_CANDIDATES)

            if col:
                profile = df[
                    df[col].astype(str) == selected
                ]

                if not profile.empty:
                    found = True
                    st.subheader(FILE_NAMES[key])
                    st.dataframe(profile, use_container_width=True)

        if not found:
            st.info("No individual records found for this player.")

# =====================================================
# PLAYER COMPARISON
# =====================================================

elif page == "Player Comparison":

    section("PLAYER COMPARISON")

    if len(players) < 2:
        st.warning("At least two player names are required.")
    else:
        c1, c2 = st.columns(2)

        with c1:
            p1 = st.selectbox("Player One", players, key="p1")

        with c2:
            p2 = st.selectbox(
                "Player Two",
                [p for p in players if p != p1],
                key="p2"
            )

        for player in [p1, p2]:
            st.subheader(player)

            found = False

            for key in ["player_mapping", "playing_eleven", "ball_by_ball"]:
                df = data[key]
                col = find_column(df, PLAYER_CANDIDATES)

                if col:
                    result = df[df[col].astype(str) == player]

                    if not result.empty:
                        found = True
                        st.write(FILE_NAMES[key])
                        st.dataframe(result.head(20), use_container_width=True)

            if not found:
                st.info("No records found.")

# =====================================================
# SCOUTING NOTES
# =====================================================

elif page == "RR Scouting Notes":

    section("RAJASTHAN ROYALS SCOUTING NOTES")

    st.markdown("""
    Use this space to record evidence-based observations.

    **Batting evaluation**
    - Ability to handle difficult match situations
    - Scoring consistency
    - Contribution in different innings phases

    **Bowling evaluation**
    - Control during difficult overs
    - Ability to restrict scoring
    - Wicket-taking contributions

    **Team-fit evaluation**
    - Squad role requirements
    - Batting and bowling balance
    - Potential replacement or backup options
    """)

    note = st.text_area(
        "Write scouting observations",
        placeholder="Enter your evidence-based observations here...",
        height=180
    )

    if note:
        st.caption("Your notes are currently visible in this session only.")

# =====================================================
# DATA HEALTH
# =====================================================

elif page == "Data Health":

    section("DATA QUALITY & SOURCE CHECK")

    for key, filename in FILE_NAMES.items():

        df = data[key]

        with st.expander(filename, expanded=True):

            path = DATA_DIR / filename

            if not path.exists():
                st.error("File not found in the data folder.")
                continue

            if df.empty:
                st.error("File exists but could not be loaded or is empty.")
                continue

            st.success("Dataset loaded successfully.")

            c1, c2, c3 = st.columns(3)

            with c1:
                metric_card("Rows", safe_number(len(df)))

            with c2:
                metric_card("Columns", safe_number(len(df.columns)))

            with c3:
                missing = int(df.isna().sum().sum())
                metric_card("Missing cells", safe_number(missing))

            st.write("Column names:")
            st.write(", ".join(df.columns))

            st.write("Preview:")
            st.dataframe(df.head(5), use_container_width=True)

    st.markdown("---")
    st.caption(
        "Statistics are displayed only where the underlying data "
        "supports them. Missing or unverified fields are not fabricated."
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.markdown(
    "<center style='color:#aab7ca'>"
    "SUPERR SELECTOR | RAJASTHAN ROYALS SCOUTING"
    "<br>PLAYER RELIABILITY UNDER PRESSURE"
    "</center>",
    unsafe_allow_html=True
)
