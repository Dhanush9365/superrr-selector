
import streamlit as st
import pandas as pd
from pathlib import Path
import html

# ==========================================================
# RAJASTHAN ROYALS - PLAYER SCOUTING INTELLIGENCE
# ==========================================================

st.set_page_config(
    page_title="Rajasthan Royals | Scouting Intelligence",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# RAJASTHAN ROYALS THEME
# ==========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

:root {
    --rr-pink: #ea1d76;
    --rr-light: #ff65a5;
    --rr-navy: #10152e;
    --rr-dark: #080d20;
    --rr-gold: #d8b66a;
}

.stApp {
    background: linear-gradient(140deg,#080d20,#111a38 60%,#26132e);
    color: white;
    font-family: 'Inter',sans-serif;
}

[data-testid="stHeader"] {
    background: rgba(8,13,32,0.96);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#10152e,#19142d);
    border-right: 1px solid #45304e;
}

[data-testid="stSidebar"] * {
    color: white;
}

.hero {
    background: linear-gradient(110deg,#e91e73 0%,#8c1d70 48%,#151d42 100%);
    padding: 38px;
    border-radius: 20px;
    border: 1px solid #9c426f;
    margin-bottom: 26px;
    box-shadow: 0 12px 35px rgba(0,0,0,.25);
}

.hero h1 {
    font-family: 'Barlow Condensed',sans-serif;
    font-size: 58px;
    font-weight: 800;
    letter-spacing: 2px;
    color: white;
    margin: 0;
}

.hero h3 {
    font-family: 'Barlow Condensed',sans-serif;
    color: #ffe0ed;
    font-size: 26px;
    margin-top: 8px;
}

.hero p {
    color: #ffe5ef;
    letter-spacing: 2px;
    font-size: 12px;
}

.section-title {
    font-family: 'Barlow Condensed',sans-serif;
    color: #ff65a5;
    font-size: 32px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 15px;
}

.metric-card,.player-card {
    background: linear-gradient(145deg,#202b50,#111a35);
    border: 1px solid #495477;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 14px;
}

.metric-card {
    min-height: 115px;
}

.metric-label {
    color: #c4cbe0;
    font-size: 11px;
    letter-spacing: 1.5px;
}

.metric-value {
    color: white;
    font-family: 'Barlow Condensed',sans-serif;
    font-size: 33px;
    font-weight: 800;
    margin-top: 7px;
}

.player-name {
    color: #ff65a5;
    font-family: 'Barlow Condensed',sans-serif;
    font-size: 27px;
    font-weight: 800;
}

.note {
    background: #1a2545;
    border-left: 4px solid #ea1d76;
    border-radius: 8px;
    padding: 16px;
    color: #f3eaf0;
}

div.stButton > button,
div.stLinkButton > a {
    background: linear-gradient(90deg,#ea1d76,#a32379);
    color: white !important;
    border: 1px solid #ff65a5;
    border-radius: 9px;
    font-weight: 700;
}

div.stButton > button:hover,
div.stLinkButton > a:hover {
    background: #ff4d98;
    color: white !important;
    border-color: white;
}

.stSelectbox label,
.stTextInput label {
    color: #ff80b2 !important;
    font-weight: 600;
}

[data-testid="stDataFrame"] {
    border: 1px solid #495477;
    border-radius: 10px;
}

[data-testid="stMetricValue"] {
    color: #ff65a5;
}

.stTabs [aria-selected="true"] {
    color: #ff65a5 !important;
    border-bottom-color: #ff65a5 !important;
}

hr {
    border-color: #495477;
}

a {
    color: #ff80b2 !important;
}
</style>
""", unsafe_allow_html=True)


# ==========================================================
# PLAYER SHORTLIST
# ==========================================================

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


# ==========================================================
# CRICBUZZ PLAYER PROFILES
# All links point to individual player profile pages.
# ==========================================================

research = {

    "Shai Hope": {
        "URL": "https://www.cricbuzz.com/profiles/10384/shai-hope",
        "Batting Style": "Right-handed",
        "Bowling Style": "Not listed",
        "Profile": "Wicketkeeper-batter",
        "Focus": "Top-order stability and innings construction"
    },

    "Shimron Hetmyer": {
        "URL": "https://www.cricbuzz.com/profiles/9789/hetmyer",
        "Batting Style": "Left-handed",
        "Bowling Style": "Not listed",
        "Profile": "Middle-order batter",
        "Focus": "Middle-order batting and boundary scoring"
    },

    "Amir Jangoo": {
        "URL": "https://www.cricbuzz.com/profiles/12674/amir-jangoo",
        "Batting Style": "Left-handed",
        "Bowling Style": "Not listed",
        "Profile": "Wicketkeeper-batter",
        "Focus": "Wicketkeeping and top-order batting"
    },

    "Tushar Raheja": {
        "URL": "https://www.cricbuzz.com/profiles/13860/tushar-raheja",
        "Batting Style": "Left-handed",
        "Bowling Style": "Not listed",
        "Profile": "Wicketkeeper-batter",
        "Focus": "Wicketkeeping and batting contribution"
    },

    "Karan Lal": {
        "URL": "https://www.cricbuzz.com/profiles/14708/karan-lal",
        "Batting Style": "Right-handed",
        "Bowling Style": "Right-arm offbreak",
        "Profile": "Batter",
        "Focus": "Batting and off-spin contribution"
    },

    "Shivalik Sharma": {
        "URL": "https://www.cricbuzz.com/profiles/14408/shivalik-sharma",
        "Batting Style": "Left-handed",
        "Bowling Style": "Right-arm legbreak",
        "Profile": "Batting all-rounder",
        "Focus": "Batting and leg-spin contribution"
    },

    "Anmolpreet Singh": {
        "URL": "https://www.cricbuzz.com/profiles/10947/anmolpreet-singh",
        "Batting Style": "Right-handed",
        "Bowling Style": "Right-arm offbreak",
        "Profile": "Batter",
        "Focus": "Top-order batting and innings construction"
    },

    "Nehal Wadhera": {
        "URL": "https://www.cricbuzz.com/profiles/13915/nehal-wadhera-c",
        "Batting Style": "Left-handed",
        "Bowling Style": "Right-arm legbreak",
        "Profile": "Middle-order batter",
        "Focus": "Middle-order batting and spin-hitting"
    },

    "Mitchell Owen": {
        "URL": "https://www.cricbuzz.com/profiles/18568/mitchell-owen",
        "Batting Style": "Right-handed",
        "Bowling Style": "Right-arm medium",
        "Profile": "Batting all-rounder",
        "Focus": "Power hitting and medium-pace bowling"
    },

    "Tanmay Agarwal": {
        "URL": "https://www.cricbuzz.com/profiles/10258/tanmay-agarwal",
        "Batting Style": "Left-handed",
        "Bowling Style": "Right-arm legbreak",
        "Profile": "Batter",
        "Focus": "Top-order batting and innings building"
    },

    "Ben Stokes": {
        "URL": "https://www.cricbuzz.com/profiles/6557/ben-stokes",
        "Batting Style": "Left-handed",
        "Bowling Style": "Right-arm fast-medium",
        "Profile": "Batting all-rounder",
        "Focus": "Pressure batting and seam-bowling contribution"
    },

    "Sikandar Raza": {
        "URL": "https://www.cricbuzz.com/profiles/9354/s-raza",
        "Batting Style": "Right-handed",
        "Bowling Style": "Right-arm offbreak",
        "Profile": "Batting all-rounder",
        "Focus": "Batting and off-spin contribution"
    },

    "Michael Bracewell": {
        "URL": "https://www.cricbuzz.com/profiles/9551/m-bracewell",
        "Batting Style": "Left-handed",
        "Bowling Style": "Right-arm offbreak",
        "Profile": "Batting all-rounder",
        "Focus": "Batting and off-spin contribution"
    },

    "Shamar Springer": {
        "URL": "https://www.cricbuzz.com/profiles/11223/shamar-springer",
        "Batting Style": "Right-handed",
        "Bowling Style": "Right-arm fast-medium",
        "Profile": "Bowling all-rounder",
        "Focus": "Seam bowling and lower-order batting"
    },

    "Deepak Chahar": {
        "URL": "https://www.cricbuzz.com/profiles/7836/deepak-chahar",
        "Batting Style": "Right-handed",
        "Bowling Style": "Right-arm fast-medium",
        "Profile": "Fast bowler",
        "Focus": "New-ball movement and powerplay wickets"
    },

    "Trent Boult": {
        "URL": "https://www.cricbuzz.com/profiles/8117/trent-boult",
        "Batting Style": "Right-handed",
        "Bowling Style": "Left-arm fast-medium",
        "Profile": "Fast bowler",
        "Focus": "Left-arm pace and new-ball movement"
    },

    "Naman Tiwari": {
        "URL": "https://www.cricbuzz.com/profiles/51756/naman-tiwari",
        "Batting Style": "Left-handed",
        "Bowling Style": "Left-arm fast-medium",
        "Profile": "Fast bowler",
        "Focus": "Left-arm pace and wicket-taking ability"
    },

    "Raj Limbani": {
        "URL": "https://www.cricbuzz.com/profiles/52488/raj-limbani",
        "Batting Style": "Left-handed",
        "Bowling Style": "Right-arm fast-medium",
        "Profile": "Bowling all-rounder",
        "Focus": "Seam bowling and lower-order batting"
    },

    "Umran Malik": {
        "URL": "https://www.cricbuzz.com/profiles/19027/umran-malik",
        "Batting Style": "Right-handed",
        "Bowling Style": "Right-arm fast",
        "Profile": "Fast bowler",
        "Focus": "Express pace and wicket-taking potential"
    },

    "Ishant Bhardwaj": {
        "URL": "https://www.cricbuzz.com/profiles/1466256/ishant-bhardwaj",
        "Batting Style": "Right-handed",
        "Bowling Style": "Left-arm fast-medium",
        "Profile": "Bowling all-rounder",
        "Focus": "Left-arm pace and lower-order batting"
    }
}


# ==========================================================
# RESEARCH LINKS
# ==========================================================

def research_url(name):
    return research.get(name, {}).get("URL", "")


# ==========================================================
# DATASET DETECTION
# ==========================================================

def find_dataset_files():

    base = Path(__file__).resolve().parent

    ignored = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules"
    }

    csv_files = []

    for file in base.rglob("*.csv"):

        if any(part in ignored for part in file.parts):
            continue

        csv_files.append(file)

    return csv_files


dataset_files = find_dataset_files()

dataset_categories = {
    "Ball-by-ball data": ["ball", "delivery"],
    "Match data": ["match"],
    "Competition data": ["competition", "tournament"],
    "Team data": ["team"],
    "Playing XI data": ["playing", "xi", "squad"]
}

detected_categories = {}

for category, keywords in dataset_categories.items():

    detected_categories[category] = [
        file.name
        for file in dataset_files
        if any(keyword in file.stem.lower() for keyword in keywords)
    ]


# ==========================================================
# EVALUATION FRAMEWORK
# ==========================================================

batting_parameters = pd.DataFrame({
    "Evaluation Parameter": [
        "Batting Average",
        "Strike Rate",
        "Boundary Percentage",
        "Pressure Runs",
        "Pressure Strike Rate",
        "Dismissal Frequency",
        "Chase Performance",
        "Consistency",
        "Sample Size"
    ],
    "What It Measures": [
        "Average runs scored per dismissal.",
        "Runs scored per 100 balls faced.",
        "Share of runs scored through boundaries.",
        "Runs contributed in pressure situations.",
        "Scoring speed in high-pressure situations.",
        "How frequently the batter gets dismissed.",
        "Contribution while chasing a target.",
        "Performance across different innings.",
        "Number of innings and balls analysed."
    ],
    "Scouting Importance": [
        "Measures run-scoring contribution.",
        "Evaluates scoring tempo.",
        "Identifies boundary-scoring ability.",
        "Examines contribution in difficult situations.",
        "Evaluates scoring under pressure.",
        "Helps assess batting reliability.",
        "Examines chase-related performance.",
        "Distinguishes consistent performance.",
        "Avoids misleading conclusions."
    ]
})

bowling_parameters = pd.DataFrame({
    "Evaluation Parameter": [
        "Bowling Average",
        "Economy Rate",
        "Bowling Strike Rate",
        "Dot-Ball Percentage",
        "Death-Over Economy",
        "Powerplay Economy",
        "Pressure Wickets",
        "Boundary Control",
        "Sample Size"
    ],
    "What It Measures": [
        "Runs conceded per wicket taken.",
        "Runs conceded per over.",
        "Balls bowled per wicket.",
        "Percentage of dot balls.",
        "Run control in final overs.",
        "Run control in opening overs.",
        "Wickets taken in pressure situations.",
        "Ability to limit boundaries.",
        "Number of overs and deliveries."
    ],
    "Scouting Importance": [
        "Evaluates wicket-taking efficiency.",
        "Measures scoring control.",
        "Shows wicket frequency.",
        "Evaluates ability to build pressure.",
        "Examines death-over effectiveness.",
        "Examines powerplay effectiveness.",
        "Evaluates impact in difficult moments.",
        "Measures boundary prevention.",
        "Provides statistical context."
    ]
})

general_parameters = pd.DataFrame({
    "Parameter": [
        "Role Suitability",
        "Fielding Contribution",
        "Fitness and Availability",
        "Experience",
        "Opposition Quality",
        "Match Conditions",
        "Team Balance"
    ],
    "Evaluation Purpose": [
        "Fit with the required squad position.",
        "Catches, run-outs and fielding reliability.",
        "Availability throughout the season.",
        "Experience in competitive T20 cricket.",
        "Performance against different opposition.",
        "Suitability to different pitches.",
        "Contribution to the overall combination."
    ]
})


# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================

st.sidebar.markdown("""
<div style="text-align:center;padding:12px 0;">
    <div style="font-size:34px;">🏏</div>
    <div style="color:#ff65a5;font-weight:800;
                letter-spacing:3px;font-size:13px;">
        RAJASTHAN ROYALS
    </div>
    <div style="color:#d8b66a;font-size:10px;
                letter-spacing:2px;">
        SCOUTING INTELLIGENCE
    </div>
</div>
<hr style="border-color:#495477;">
""", unsafe_allow_html=True)

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
st.sidebar.caption("ROUND 1 | PLAYER RELIABILITY")
st.sidebar.caption("Scouting Dashboard | 2026")


# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown("""
<div class="hero">
    <p>RAJASTHAN ROYALS • SCOUTING INTELLIGENCE</p>
    <h1>ROYAL SCOUTING</h1>
    <h3>PLAYER RELIABILITY UNDER PRESSURE</h3>
    <p>DATA-DRIVEN TALENT IDENTIFICATION • ROUND 1</p>
</div>
""", unsafe_allow_html=True)


# ==========================================================
# OVERVIEW
# ==========================================================

if page == "Overview":

    st.markdown(
        '<div class="section-title">SCOUTING OVERVIEW</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("SHORTLISTED PLAYERS", len(player_df)),
        ("BATTER PROFILES", len(player_df[player_df["Category"] == "Batting"])),
        ("ALL-ROUNDERS", len(player_df[player_df["Category"] == "All-rounder"])),
        ("BOWLER PROFILES", len(player_df[player_df["Category"] == "Bowling"]))
    ]

    for col, (label, value) in zip(
        [c1, c2, c3, c4], metrics
    ):

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

    st.markdown("### 🏏 SCOUTING FRAMEWORK")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="player-card">
            <div class="player-name">BATTER EVALUATION</div>
            <p>• Runs scored under pressure</p>
            <p>• Strike rate under pressure</p>
            <p>• Dismissal frequency</p>
            <p>• Chase performance</p>
            <p>• Comparison with normal performance</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="player-card">
            <div class="player-name">BOWLER EVALUATION</div>
            <p>• Economy under pressure</p>
            <p>• Wickets taken</p>
            <p>• Dot-ball percentage</p>
            <p>• Death-over performance</p>
            <p>• Comparison with normal performance</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📋 ADDITIONAL EVALUATION")

    st.dataframe(
        general_parameters,
        use_container_width=True,
        hide_index=True
    )

    # Dynamic dataset availability

    st.markdown("### 📁 DATASET AVAILABILITY")

    if dataset_files:

        st.success(
            f"{len(dataset_files)} CSV file(s) detected in the application."
        )

    else:

        st.warning(
            "No CSV files detected. Please check your uploaded dataset."
        )

    st.caption(
        "File detection confirms file availability only. "
        "It does not confirm that statistical calculations have been completed."
    )

    with st.expander("VIEW DATASET FILES"):

        if dataset_files:

            base = Path(__file__).resolve().parent

            for file in dataset_files:

                st.write(
                    "📄",
                    str(file.relative_to(base))
                )

        else:

            st.write("No CSV files detected.")

    st.markdown("### DATASET CATEGORY CHECK")

    for category, files in detected_categories.items():

        if files:

            st.success(
                f"{category}: Found — {', '.join(files)}"
            )

        else:

            st.info(
                f"{category}: Not detected by filename"
            )

    st.markdown("### PLAYER SHORTLIST")

    st.dataframe(
        player_df,
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# BATTING ANALYTICS
# ==========================================================

elif page == "Batting Analytics":

    st.markdown(
        '<div class="section-title">BATTING INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    batters = player_df[
        player_df["Category"] == "Batting"
    ]

    st.write(
        "Explore the shortlisted batting candidates and the parameters "
        "used to assess their T20 batting contribution."
    )

    st.dataframe(
        batters,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### BATTER EVALUATION PARAMETERS")

    st.dataframe(
        batting_parameters,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### HOW TO INTERPRET THE PARAMETERS")

    st.markdown("""
    <div class="note">
    <b>Batting Average:</b> Helps assess the batter's run contribution
    before dismissal.<br><br>

    <b>Strike Rate:</b> Helps understand how quickly the batter scores.<br><br>

    <b>Pressure Strike Rate:</b> Examines scoring tempo in difficult
    match situations.<br><br>

    <b>Sample Size:</b> Prevents conclusions based on a very small
    number of innings or deliveries.
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "These are evaluation definitions. Actual player statistics "
        "are not calculated by this version of the dashboard."
    )


# ==========================================================
# BOWLING ANALYTICS
# ==========================================================

elif page == "Bowling Analytics":

    st.markdown(
        '<div class="section-title">BOWLING INTELLIGENCE</div>',
        unsafe_allow_html=True
    )

    bowlers = player_df[
        player_df["Category"] == "Bowling"
    ]

    st.write(
        "Explore the shortlisted bowling candidates and the parameters "
        "used to evaluate their T20 bowling contribution."
    )

    st.dataframe(
        bowlers,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### BOWLER EVALUATION PARAMETERS")

    st.dataframe(
        bowling_parameters,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### HOW TO INTERPRET THE PARAMETERS")

    st.markdown("""
    <div class="note">
    <b>Economy Rate:</b> Measures the bowler's ability to restrict runs.<br><br>

    <b>Bowling Strike Rate:</b> Measures how frequently the bowler takes wickets.<br><br>

    <b>Dot-Ball Percentage:</b> Examines the ability to build pressure.<br><br>

    <b>Death-Over Economy:</b> Helps assess effectiveness during the final overs.<br><br>

    <b>Sample Size:</b> Provides context to the bowling statistics.
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "These are evaluation definitions. Actual bowling statistics "
        "are not calculated by this version of the dashboard."
    )


# ==========================================================
# PLAYER PROFILES - CRICBUZZ INTEGRATION
# ==========================================================

elif page == "Player Profiles":

    st.markdown(
        '<div class="section-title">PLAYER SCOUTING PROFILES</div>',
        unsafe_allow_html=True
    )

    selected_player = st.selectbox(
        "SELECT A PLAYER",
        player_df["Player"].tolist()
    )

    player = player_df[
        player_df["Player"] == selected_player
    ].iloc[0]

    details = research.get(selected_player, {})

    st.markdown(f"""
    <div class="player-card">
        <div class="player-name">
            {html.escape(selected_player)}
        </div>

        <h4>{html.escape(player['Country'])}</h4>

        <p><b>Squad Role:</b>
        {html.escape(player['Role'])}</p>

        <p><b>Category:</b>
        {html.escape(player['Category'])}</p>

        <hr>

        <h4>PLAYER INFORMATION</h4>

        <p><b>Batting Style:</b>
        {html.escape(details.get('Batting Style', 'Check published profile'))}</p>

        <p><b>Bowling Style:</b>
        {html.escape(details.get('Bowling Style', 'Check published profile'))}</p>

        <p><b>Playing Profile:</b>
        {html.escape(details.get('Profile', player['Role']))}</p>

        <p><b>Scouting Focus:</b>
        {html.escape(details.get('Focus', 'Further research required'))}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### OFFICIAL PLAYER RESEARCH")

    profile_url = research_url(selected_player)

    if profile_url:

        st.link_button(
            "📖 OPEN CRICBUZZ PLAYER PROFILE",
            profile_url,
            use_container_width=True
        )

        st.caption(
            "The link opens the player's individual Cricbuzz profile, "
            "where available career and statistics sections can be explored."
        )

    else:

        st.warning("Published player profile link is unavailable.")

    st.markdown("### SCOUTING EVALUATION")

    st.write(
        "The player's suitability should be assessed using the relevant "
        "batting, bowling, fielding and role-specific evaluation parameters."
    )

    st.info(
        "Career statistics and pressure metrics should be verified "
        "against the competition dataset before drawing conclusions."
    )


# ==========================================================
# PLAYER COMPARISON
# ==========================================================

elif page == "Player Comparison":

    st.markdown(
        '<div class="section-title">PLAYER INTELLIGENCE & COMPARISON</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        player1 = st.selectbox(
            "SELECT FIRST PLAYER",
            player_df["Player"].tolist(),
            key="p1"
        )

    with col2:

        player2 = st.selectbox(
            "SELECT SECOND PLAYER",
            player_df["Player"].tolist(),
            index=1,
            key="p2"
        )

    if player1 == player2:

        st.warning("Please select two different players.")

    else:

        p1 = player_df[
            player_df["Player"] == player1
        ].iloc[0]

        p2 = player_df[
            player_df["Player"] == player2
        ].iloc[0]

        r1 = research.get(player1, {})
        r2 = research.get(player2, {})

        st.markdown("### HEAD-TO-HEAD PLAYER PROFILE")

        comparison = pd.DataFrame({

            "Attribute": [
                "Country",
                "Squad Role",
                "Category",
                "Batting Style",
                "Bowling Style",
                "Playing Profile",
                "Scouting Focus"
            ],

            player1: [
                p1["Country"],
                p1["Role"],
                p1["Category"],
                r1.get("Batting Style", "Verification required"),
                r1.get("Bowling Style", "Verification required"),
                r1.get("Profile", p1["Role"]),
                r1.get("Focus", "Further research required")
            ],

            player2: [
                p2["Country"],
                p2["Role"],
                p2["Category"],
                r2.get("Batting Style", "Verification required"),
                r2.get("Bowling Style", "Verification required"),
                r2.get("Profile", p2["Role"]),
                r2.get("Focus", "Further research required")
            ]

        })

        st.dataframe(
            comparison,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### PLAYER RESEARCH")

        c1, c2 = st.columns(2)

        with c1:

            st.markdown(f"""
            <div class="player-card">
                <div class="player-name">{html.escape(player1)}</div>
                <p><b>Country:</b> {html.escape(p1['Country'])}</p>
                <p><b>Role:</b> {html.escape(p1['Role'])}</p>
                <p><b>Playing Profile:</b>
                {html.escape(r1.get('Profile', p1['Role']))}</p>
                <p><b>Scouting Focus:</b>
                {html.escape(r1.get('Focus', 'Further research required'))}</p>
            </div>
            """, unsafe_allow_html=True)

            if r1.get("URL"):

                st.link_button(
                    f"OPEN {player1.upper()} CRICBUZZ PROFILE",
                    r1["URL"],
                    use_container_width=True
                )

        with c2:

            st.markdown(f"""
            <div class="player-card">
                <div class="player-name">{html.escape(player2)}</div>
                <p><b>Country:</b> {html.escape(p2['Country'])}</p>
                <p><b>Role:</b> {html.escape(p2['Role'])}</p>
                <p><b>Playing Profile:</b>
                {html.escape(r2.get('Profile', p2['Role']))}</p>
                <p><b>Scouting Focus:</b>
                {html.escape(r2.get('Focus', 'Further research required'))}</p>
            </div>
            """, unsafe_allow_html=True)

            if r2.get("URL"):

                st.link_button(
                    f"OPEN {player2.upper()} CRICBUZZ PROFILE",
                    r2["URL"],
                    use_container_width=True
                )

        st.markdown("### COMPARISON EVALUATION PARAMETERS")

        comparison_tabs = st.tabs([
            "Batting",
            "Bowling",
            "Overall Fit"
        ])

        with comparison_tabs[0]:

            st.dataframe(
                batting_parameters,
                use_container_width=True,
                hide_index=True
            )

        with comparison_tabs[1]:

            st.dataframe(
                bowling_parameters,
                use_container_width=True,
                hide_index=True
            )

        with comparison_tabs[2]:

            st.dataframe(
                general_parameters,
                use_container_width=True,
                hide_index=True
            )

        st.info(
            "This comparison supports scouting discussions. "
            "It does not rank players or declare a winner. "
            "Verified career statistics and match-situation data "
            "are required for statistical conclusions."
        )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown("""
<div style="text-align:center;padding:15px;color:#c4cbe0;">

    <div style="color:#ff65a5;font-weight:800;
                letter-spacing:2px;">
        RAJASTHAN ROYALS SCOUTING
    </div>

    PLAYER RELIABILITY UNDER PRESSURE

    <br>

    <span style="color:#d8b66a;">
        ROUND 1 | 2026
    </span>

</div>
""", unsafe_allow_html=True)
