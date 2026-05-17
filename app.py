import streamlit as st
from streamlit_option_menu import option_menu

import plotly.express as px
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Kartik | Data Science Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* MAIN APP */

.stApp {
    background: linear-gradient(
        135deg,
        #0B0F19,
        #111827,
        #0F172A
    );

    color: white;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background: rgba(17, 24, 39, 0.92);

    backdrop-filter: blur(15px);

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* HEADINGS */

h1, h2, h3, h4, h5 {
    color: white;
}

/* HERO TITLE */

.hero-title {

    font-size: 78px;

    font-weight: 800;

    background: linear-gradient(
        90deg,
        #38BDF8,
        #7C3AED,
        #2563EB
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 0px;
}

/* HERO SUBTITLE */

.hero-subtitle {

    font-size: 24px;

    color: #CBD5E1;

    margin-top: 0px;
}

/* GLASS CARDS */

.metric-card {

    background: rgba(255,255,255,0.05);

    border-radius: 24px;

    padding: 28px;

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(14px);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.35);

    transition: all 0.35s ease;
}

/* CARD HOVER */

.metric-card:hover {

    transform: translateY(-6px);

    border: 1px solid rgba(56,189,248,0.35);

    box-shadow:
        0 12px 35px rgba(56,189,248,0.18);
}

/* PROJECT CARDS */

.project-card {

    background: rgba(255,255,255,0.05);

    padding: 30px;

    border-radius: 24px;

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(12px);

    transition: all 0.35s ease;

    margin-bottom: 25px;
}

.project-card:hover {

    transform: scale(1.015);

    border: 1px solid rgba(124,58,237,0.4);

    box-shadow:
        0 10px 35px rgba(124,58,237,0.18);
}

/* BUTTONS */

div.stButton > button,
div.stDownloadButton > button {

    width: 100%;

    border-radius: 14px;

    height: 3.2em;

    font-size: 16px;

    font-weight: 600;

    border: none;

    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    );

    color: white;

    transition: 0.3s;
}

div.stButton > button:hover,
div.stDownloadButton > button:hover {

    transform: scale(1.03);

    box-shadow:
        0 8px 25px rgba(59,130,246,0.4);
}

/* LINKS */

a {
    text-decoration: none !important;
}

/* SCROLLBAR */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: #374151;
    border-radius: 10px;
}

/* WELCOME CONTAINER */

.welcome-box {

    padding: 22px;

    border-radius: 24px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    margin-bottom: 25px;

    backdrop-filter: blur(12px);
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.title("📊 Portfolio")

    selected = option_menu(
        menu_title="Navigation",
        options=[
            "Home",
            "Projects",
            "Skills",
            "Contact"
        ],
        icons=[
            "house",
            "bar-chart",
            "code-slash",
            "envelope"
        ],
        menu_icon="cast",
        default_index=0,
    )

# ---------------------------------------------------
# HOME
# ---------------------------------------------------

if selected == "Home":

    # WELCOME BOX

    st.markdown("""
    <div class="welcome-box">

    <h2 style="color:#38BDF8;">
    📊 Welcome to My Analytics Portfolio
    </h2>

    <p style="font-size:18px; color:#CBD5E1;">
    Building data-driven solutions using analytics,
    machine learning, visualization, and AI-powered applications.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # HERO SECTION

    col1, col2 = st.columns([1, 2])

    # LEFT SIDE

    with col1:

        st.image(
            "assets/Kartik_Profile.jpg",
            width=300
        )

    # RIGHT SIDE

    with col2:

        st.markdown("""
        <h1 class="hero-title">
        Kartik
        </h1>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h3 class="hero-subtitle">
        Data Analyst • Data Science Enthusiast • Problem Solver
        </h3>
        """, unsafe_allow_html=True)

        st.write("""
        Passionate about solving real-world business problems using:
        - Data Analytics
        - Machine Learning
        - Data Visualization
        - AI Applications
        - Business Insights
        """)

        # BUTTONS

        # BUTTONS

col_btn1, col_btn2, col_btn3 = st.columns(3)

# RESUME BUTTON

with col_btn1:

    with open("assets/Resume_Kartik.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📄 Resume",
        data=PDFbyte,
        file_name="Resume_Kartik.pdf",
        mime="application/octet-stream"
    )

# LINKEDIN BUTTON

with col_btn2:

    st.markdown("""
    <a href="https://www.linkedin.com/"
    target="_blank">

    <button style="
        width:100%;
        height:3.2em;
        border:none;
        border-radius:14px;

        background: linear-gradient(
            90deg,
            #2563EB,
            #7C3AED
        );

        color:white;
        font-size:16px;
        font-weight:600;
        cursor:pointer;
    ">
    🔗 LinkedIn
    </button>

    </a>
    """, unsafe_allow_html=True)

# GITHUB BUTTON

with col_btn3:

    st.markdown("""
    <a href="https://github.com/"
    target="_blank">

    <button style="
        width:100%;
        height:3.2em;
        border:none;
        border-radius:14px;

        background: linear-gradient(
            90deg,
            #2563EB,
            #7C3AED
        );

        color:white;
        font-size:16px;
        font-weight:600;
        cursor:pointer;
    ">
    💻 GitHub
    </button>

    </a>
    """, unsafe_allow_html=True)

    st.write("---")

    # METRICS

    st.subheader("📊 Dashboard Metrics")

    col1, col2, col3, col4 = st.columns(4)

    metrics = [
        ("15+", "Projects"),
        ("300+", "DSA Problems"),
        ("5+", "Certifications"),
        ("2", "Internships")
    ]

    for col, (value, label) in zip(
        [col1, col2, col3, col4],
        metrics
    ):

        with col:

            st.markdown(f"""
            <div class="metric-card">
                <h1>{value}</h1>
                <p>{label}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("---")

    # ABOUT SECTION

    st.subheader("🚀 About Me")

    st.write("""
    I am a 3rd year engineering student passionate about leveraging
    data science and analytics to solve real-world business problems.

    My interests include:
    - Machine Learning
    - Financial Analytics
    - AI-Powered Applications
    - Business Intelligence
    - Consulting Analytics

    Currently building:
    - ESG Greenwashing Analyzer
    - AI Banking Retention Agent
    - Stock Trend Prediction Dashboard
    - Consulting Case Studies
    """)

    st.write("---")

    # ANALYTICS CHART

    st.subheader("📈 Analytics Overview")

    analytics_df = pd.DataFrame({
        "Domain": [
            "Machine Learning",
            "Data Analytics",
            "Visualization",
            "System Design",
            "Consulting"
        ],

        "Experience": [
            85,
            90,
            80,
            65,
            75
        ]
    })

    analytics_fig = px.bar(
        analytics_df,
        x="Domain",
        y="Experience",
        text="Experience",
        height=500
    )

    analytics_fig.update_layout(
        paper_bgcolor="#0B0F19",
        plot_bgcolor="#0B0F19",
        font_color="white"
    )

    st.plotly_chart(
        analytics_fig,
        use_container_width=True
    )

# ---------------------------------------------------
# PROJECTS
# ---------------------------------------------------

elif selected == "Projects":

    st.title("🚀 Featured Projects")

    # PROJECT 1

    st.markdown("""
    <div class="project-card">

        <h3>📈 ESG Greenwashing Analyzer</h3>

        <p>
        AI-powered system for analyzing ESG reports and detecting
        potential greenwashing patterns using NLP and sentiment analysis.
        </p>

        <p>
        <b>Tech Stack:</b>
        Python, NLP, Streamlit, FinBERT
        </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "🔗 GitHub Repo",
            "https://github.com/"
        )

    with col2:

        st.link_button(
            "🌐 Live Demo",
            "https://streamlit.io/"
        )

    st.write("")

    # PROJECT 2

    st.markdown("""
    <div class="project-card">

        <h3>🏦 Bank Customer Retention Agent</h3>

        <p>
        Intelligent ML system that predicts customer churn
        and recommends personalized retention strategies.
        </p>

        <p>
        <b>Tech Stack:</b>
        Python, Scikit-learn, Pandas, Power BI
        </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "🔗 GitHub Repo",
            "https://github.com/"
        )

    with col2:

        st.link_button(
            "🌐 Live Demo",
            "https://streamlit.io/"
        )

    st.write("---")

    # PROJECT DISTRIBUTION

    st.subheader("📊 Project Distribution")

    project_df = pd.DataFrame({

        "Category": [
            "Machine Learning",
            "Analytics",
            "Visualization",
            "Consulting",
            "AI Applications"
        ],

        "Projects": [
            4,
            3,
            2,
            2,
            3
        ]
    })

    pie_fig = px.pie(
        project_df,
        names="Category",
        values="Projects",
        hole=0.5
    )

    pie_fig.update_layout(
        paper_bgcolor="#0B0F19",
        font_color="white"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

# ---------------------------------------------------
# SKILLS
# ---------------------------------------------------

elif selected == "Skills":

    st.title("⚡ Technical Skills Dashboard")

    skills_df = pd.DataFrame({

        "Skill": [
            "Python",
            "SQL",
            "Machine Learning",
            "Data Visualization",
            "Power BI",
            "Streamlit",
            "Data Analysis",
            "Problem Solving"
        ],

        "Level": [
            90,
            75,
            85,
            80,
            70,
            85,
            88,
            92
        ]
    })

    # BAR CHART

    skill_fig = px.bar(
        skills_df,
        x="Skill",
        y="Level",
        text="Level",
        height=500
    )

    skill_fig.update_layout(
        paper_bgcolor="#0B0F19",
        plot_bgcolor="#0B0F19",
        font_color="white"
    )

    st.plotly_chart(
        skill_fig,
        use_container_width=True
    )

    st.write("---")

    # RADAR CHART

    radar_fig = px.line_polar(
        skills_df,
        r="Level",
        theta="Skill",
        line_close=True
    )

    radar_fig.update_layout(
        paper_bgcolor="#0B0F19",
        font_color="white"
    )

    st.plotly_chart(
        radar_fig,
        use_container_width=True
    )

# ---------------------------------------------------
# CONTACT
# ---------------------------------------------------

elif selected == "Contact":

    st.title("📬 Contact Me")

    st.write(
        "Feel free to connect with me through the platforms below."
    )

    st.link_button(
        "🔗 LinkedIn",
        "https://www.linkedin.com/"
    )

    st.link_button(
        "💻 GitHub",
        "https://github.com/"
    )

    st.write("📧 Email: kartiksanjay.k24@iiits.in")
    st.write("📧 Email: kartikkumthe7115@gmail.com")
    st.write("📧 Email: kartik7115edu@gmail.com")
