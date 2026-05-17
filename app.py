# Fully Updated Advanced Streamlit Portfolio Code

```python
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
# SESSION STATE
# ---------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

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

/* CLICKABLE METRIC CARDS */

.metric-link {
    text-decoration: none !important;
}

.metric-card {

    background: rgba(255,255,255,0.05);

    border-radius: 24px;

    padding: 28px;

    border: 1px solid rgba(255,255,255,0.08);

    backdrop-filter: blur(14px);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.35);

    transition: all 0.35s ease;

    cursor: pointer;

    text-align: center;
}

.metric-card:hover {

    transform: translateY(-8px) scale(1.02);

    border: 1px solid rgba(56,189,248,0.5);

    box-shadow:
        0 0 25px rgba(56,189,248,0.35),
        0 12px 35px rgba(56,189,248,0.18);
}

.metric-card h1 {
    color: white;
    margin-bottom: 5px;
}

.metric-card p {
    color: #CBD5E1;
    font-size: 18px;
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
        0 0 30px rgba(124,58,237,0.28),
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

/* LINK BUTTONS */

div[data-testid="stLinkButton"] a {
    width: 100%;
    display: inline-flex;
    justify-content: center;
    align-items: center;

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

    color: white !important;

    text-decoration: none !important;

    transition: 0.3s;
}

div[data-testid="stLinkButton"] a:hover {
    transform: scale(1.03);

    box-shadow:
        0 8px 25px rgba(59,130,246,0.4);
}

/* FILTER BOX */

.stSelectbox > div > div {
    background-color: rgba(255,255,255,0.05);
    color: white;
}

/* WELCOME BOX */

.welcome-box {

    padding: 22px;

    border-radius: 24px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    margin-bottom: 25px;

    backdrop-filter: blur(12px);
}

/* SCROLLBAR */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {
    background: #374151;
    border-radius: 10px;
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

    with col1:

        st.image(
            "assets/Kartik_Profile.jpg",
            width=300
        )

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

        col_btn1, col_btn2, col_btn3 = st.columns(3)

        with col_btn1:

            with open("assets/Resume_Kartik.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()

            st.download_button(
                label="📄 Resume",
                data=PDFbyte,
                file_name="Resume_Kartik.pdf",
                mime="application/octet-stream",
                use_container_width=True
            )

        with col_btn2:

            st.link_button(
                "🔗 LinkedIn",
                "https://www.linkedin.com/",
                use_container_width=True
            )

        with col_btn3:

            st.link_button(
                "💻 GitHub",
                "https://github.com/",
                use_container_width=True
            )

    st.write("---")

    # CLICKABLE METRIC CARDS

    st.subheader("📊 Dashboard Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("15+\nProjects", key="projects_card", use_container_width=True):
            st.session_state.page = "Projects"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h1>300+</h1>
            <p>DSA Problems</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if st.button("5+\nCertifications", key="skills_card", use_container_width=True):
            st.session_state.page = "Skills"
            st.rerun()

    with col4:
        if st.button("2\nInternships", key="contact_card", use_container_width=True):
            st.session_state.page = "Contact"
            st.rerun()

    st.write("---")

    # ABOUT

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

    # ANALYTICS OVERVIEW

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

    # FILTER

    project_filter = st.selectbox(
        "Filter Projects",
        [
            "All",
            "Machine Learning",
            "Analytics",
            "AI Applications"
        ]
    )

    projects = [
        {
            "title": "📈 ESG Greenwashing Analyzer",
            "category": "AI Applications",
            "description": "AI-powered system for analyzing ESG reports and detecting potential greenwashing patterns using NLP and sentiment analysis.",
            "tech": "Python, NLP, Streamlit, FinBERT"
        },

        {
            "title": "🏦 Bank Customer Retention Agent",
            "category": "Machine Learning",
            "description": "Intelligent ML system that predicts customer churn and recommends personalized retention strategies.",
            "tech": "Python, Scikit-learn, Pandas, Power BI"
        },

        {
            "title": "📊 Stock Trend Prediction Dashboard",
            "category": "Analytics",
            "description": "Interactive dashboard for stock market trend analysis and prediction.",
            "tech": "Streamlit, Prophet, Plotly"
        }
    ]

    for project in projects:

        if project_filter == "All" or project["category"] == project_filter:

            st.markdown(f"""
            <div class="project-card">

                <h3>{project['title']}</h3>

                <p>{project['description']}</p>

                <p>
                <b>Tech Stack:</b> {project['tech']}
                </p>

            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                st.link_button(
                    "🔗 GitHub Repo",
                    "https://github.com/",
                    use_container_width=True
                )

            with col2:
                st.link_button(
                    "🌐 Live Demo",
                    "https://streamlit.io/",
                    use_container_width=True
                )

            st.write("")

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
        "https://www.linkedin.com/",
        use_container_width=True
    )

    st.link_button(
        "💻 GitHub",
        "https://github.com/",
        use_container_width=True
    )

    st.write("📧 Email: kartiksanjay.k24@iiits.in")
    st.write("📧 Email: kartikkumthe7115@gmail.com")
    st.write("📧 Email: kartik7115edu@gmail.com")
