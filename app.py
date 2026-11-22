
import streamlit as st
from pathlib import Path
from datetime import datetime
from html import escape
import re

# =====================================================
# 1. APPLICATION CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Gbenge Terfa Nathaniel | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"
IMAGE_DIR.mkdir(exist_ok=True)

CV_PATH = BASE_DIR / "cv.pdf"

# =====================================================
# 2. PERSONAL AND EDUCATIONAL INFORMATION
# =====================================================

FULL_NAME = "Gbenge Terfa Nathaniel"
EMAIL = "terfagbenge@gmail.com"
LOCATION = "Naka, Benue State, Nigeria"

HND_QUALIFICATION = (
    "Higher National Diploma (HND) "
    "in Software and Web Development"
)

HND_SCHOOL = "Federal Polytechnic Bauchi"
HND_YEAR = "2026"

SECONDARY_SCHOOL = "Christ the King College, Naka"
SECONDARY_YEAR = "2020"

# =====================================================
# 3. IMAGE MANAGEMENT
# =====================================================

def find_image(filename, fallback=False):
    path = IMAGE_DIR / filename

    if path.is_file():
        return path

    if fallback:
        for file in sorted(IMAGE_DIR.iterdir()):
            if file.suffix.lower() in (
                ".jpg", ".jpeg", ".png", ".webp"
            ):
                return file

    return None


PROFILE_IMAGE = find_image("profile.jpg", True)
SOLAR_IMAGE = find_image("solar_dashboard.png")
SCHOOL_IMAGE = find_image("school_portal.png")

# =====================================================
# 4. WEBSITE DESIGN
# =====================================================

st.html("""
<style>
.stApp {
    background: #080f1f;
    color: #e2e8f0;
}

[data-testid="stAppViewContainer"] {
    background: #080f1f;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: #f8fafc !important;
}

.hero {
    background: linear-gradient(
        120deg, #10294d, #111827
    );
    border: 1px solid #285079;
    border-radius: 24px;
    padding: 45px 35px;
    margin: 15px 0 25px;
}

.hero-label {
    color: #38bdf8;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero-name {
    color: white;
    font-size: clamp(34px, 5vw, 60px);
    font-weight: 800;
    line-height: 1.15;
    margin: 18px 0;
}

.hero-role {
    color: #7dd3fc;
    font-size: 22px;
    font-weight: 600;
}

.hero-text {
    color: #cbd5e1;
    font-size: 16px;
    line-height: 1.8;
    margin-top: 18px;
}

.section-title {
    color: white;
    font-size: 28px;
    font-weight: 750;
    margin: 30px 0 18px;
}

.project-card {
    background: #111d30;
    border: 1px solid #263951;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 18px;
}

.project-title {
    color: #7dd3fc;
    font-size: 21px;
    font-weight: 700;
}

.project-description {
    color: #cbd5e1;
    line-height: 1.8;
    margin-top: 14px;
}

.project-tech {
    color: #38bdf8;
    font-size: 14px;
    margin-top: 15px;
}

.skill-pill {
    display: inline-block;
    padding: 10px 16px;
    margin: 5px;
    background: #172b45;
    border: 1px solid #285079;
    border-radius: 20px;
    color: #bae6fd;
}

.info-card {
    background: #111d30;
    border: 1px solid #263951;
    border-radius: 16px;
    padding: 25px;
    margin: 15px 0;
}

.info-card h3 {
    color: #7dd3fc !important;
}

.info-card p {
    color: #cbd5e1;
}

.footer {
    text-align: center;
    color: #94a3b8;
    padding: 30px 0;
}

div.stButton > button,
div.stDownloadButton > button,
div.stFormSubmitButton > button {
    background: #0284c7;
    color: white;
    border: none;
    border-radius: 10px;
}

div.stButton > button:hover,
div.stDownloadButton > button:hover,
div.stFormSubmitButton > button:hover {
    background: #0369a1;
    color: white;
}

[data-testid="stMetricLabel"] {
    color: #cbd5e1;
}

[data-testid="stMetricValue"] {
    color: white;
}
</style>
""")

# =====================================================
# 5. NAVIGATION
# =====================================================

st.markdown("### 💻 GBENGE TERFA | PORTFOLIO")

pages = [
    "Home",
    "About Me",
    "Skills",
    "Projects",
    "Work Experience",
    "Resume",
    "Contact"
]

page = st.radio(
    "Navigation",
    pages,
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# =====================================================
# 6. HOME PAGE
# =====================================================

if page == "Home":

    left, right = st.columns([2.5, 1])

    with left:
        st.html("""
        <div class="hero">
            <div class="hero-label">
                WELCOME TO MY PORTFOLIO
            </div>

            <div class="hero-name">
                GBENGE TERFA<br>NATHANIEL
            </div>

            <div class="hero-role">
                Python Software Developer &amp;
                Machine Learning Enthusiast
            </div>

            <p class="hero-text">
                I design and develop Python
                web applications, intelligent
                monitoring systems, and
                machine learning solutions
                that solve real-world problems.
            </p>
        </div>
        """)

    with right:
        if PROFILE_IMAGE:
            st.image(
                str(PROFILE_IMAGE),
                width="stretch",
                caption=FULL_NAME
            )
        else:
            st.info("Profile photograph coming soon.")

    c1, c2, c3 = st.columns(3)

    c1.metric("Featured Projects", "2")
    c2.metric("Primary Language", "Python")
    c3.metric("Specialization", "ML & Web")

    st.html("""
    <div class="section-title">
        Featured Software Projects
    </div>
    """)

    col1, col2 = st.columns(2)

    with col1:
        if SOLAR_IMAGE:
            st.image(
                str(SOLAR_IMAGE),
                width="stretch"
            )

        st.html("""
        <div class="project-card">
            <div class="project-title">
                ☀️ Solar and Battery Fault Detection
            </div>

            <p class="project-description">
                A Python-based machine learning
                system for detecting solar PV
                faults and evaluating detection
                delay and false alarm rate.
            </p>

            <div class="project-tech">
                Python | Streamlit |
                Scikit-learn | Pandas
            </div>
        </div>
        """)

    with col2:
        if SCHOOL_IMAGE:
            st.image(
                str(SCHOOL_IMAGE),
                width="stretch"
            )

        st.html("""
        <div class="project-card">
            <div class="project-title">
                🏫 School Management Portal
            </div>

            <p class="project-description">
                A Python-based school
                administration application
                for managing student and
                staff information.
            </p>

            <div class="project-tech">
                Python | Database |
                Software Development
            </div>
        </div>
        """)

    st.subheader("What I Can Build")

    st.write("""
    - Python web applications
    - Machine learning prediction systems
    - School management software
    - Business management applications
    - Data analysis dashboards
    """)

    st.subheader("Educational Background")

    st.write(
        f"**{HND_QUALIFICATION}** — "
        f"{HND_SCHOOL}, {HND_YEAR}"
    )

# =====================================================
# 7. ABOUT ME PAGE
# =====================================================

elif page == "About Me":

    st.title("About Me")

    col1, col2 = st.columns([1, 2])

    with col1:
        if PROFILE_IMAGE:
            st.image(
                str(PROFILE_IMAGE),
                width="stretch"
            )

    with col2:
        st.write(f"""
        I am **{FULL_NAME}**,
        a Python software developer with
        an interest in intelligent and
        reliable software applications.

        My work focuses on Python programming,
        machine learning, web development,
        database management, and data analysis.
        """)

    st.subheader("Educational Background")

    st.html(f"""
    <div class="info-card">
        <h3>{escape(HND_SCHOOL)}</h3>
        <p>{escape(HND_QUALIFICATION)}</p>
        <p>Department of Computing Technology</p>
        <p>Year: {escape(HND_YEAR)}</p>
    </div>
    """)

    st.html(f"""
    <div class="info-card">
        <h3>{escape(SECONDARY_SCHOOL)}</h3>
        <p>Secondary School Education</p>
        <p>Benue State, Nigeria</p>
        <p>Year: {escape(SECONDARY_YEAR)}</p>
    </div>
    """)

    st.subheader("Development Interests")

    st.write("""
    - Software engineering
    - Python web development
    - Machine learning integration
    - Intelligent monitoring systems
    - Database applications
    """)

# =====================================================
# 8. SKILLS PAGE
# =====================================================

elif page == "Skills":

    st.title("My Technical Skills")

    skill_categories = {
        "Programming": [
            "Python",
            "SQL"
        ],
        "Web Development": [
            "Streamlit",
            "Web Application Design"
        ],
        "Machine Learning": [
            "Scikit-learn",
            "Random Forest",
            "Model Evaluation"
        ],
        "Data Analysis": [
            "Pandas",
            "Matplotlib",
            "Data Visualization"
        ],
        "Development Tools": [
            "SQLite",
            "VS Code",
            "Git",
            "Software Testing"
        ]
    }

    for category, skills in skill_categories.items():

        st.subheader(category)

        html = "".join(
            f'<span class="skill-pill">'
            f'{escape(skill)}'
            f'</span>'
            for skill in skills
        )

        st.html(html)

# =====================================================
# 9. PROJECTS PAGE
# =====================================================

elif page == "Projects":

    st.title("My Software Projects")

    projects = [
        {
            "title":
                "Solar and Battery Fault Detection System",
            "description":
                "A machine learning-based solar "
                "monitoring system that detects "
                "faults and evaluates performance.",
            "features": [
                "Solar fault classification",
                "Monitoring dashboard",
                "Sensor data visualization",
                "Detection delay evaluation",
                "False alarm rate evaluation",
                "User authentication"
            ],
            "tech":
                "Python, Streamlit, Scikit-learn",
            "image": SOLAR_IMAGE
        },
        {
            "title":
                "School Management Portal",
            "description":
                "A Python-based school administration "
                "application for managing records.",
            "features": [
                "Student management",
                "Staff records",
                "Administrative functions",
                "Database management"
            ],
            "tech": "Python, Database",
            "image": SCHOOL_IMAGE
        }
    ]

    for project in projects:

        with st.container(border=True):

            st.subheader(project["title"])

            if project["image"]:
                st.image(
                    str(project["image"]),
                    width="stretch"
                )

            st.write(project["description"])

            st.markdown("**Main Features**")

            for feature in project["features"]:
                st.write("✓ " + feature)

            st.caption(
                "Technologies: " + project["tech"]
            )

# =====================================================
# 10. WORK EXPERIENCE PAGE
# =====================================================

elif page == "Work Experience":

    st.title("Professional Work Experience")

    st.write(
        "My professional experience includes "
        "computer operations and industrial training "
        "in different organizations in Nigeria."
    )

    with st.container(border=True):

        st.subheader("Industrial Training Student")

        st.write("**Organization:** Appeal Court, Jos")
        st.write("**Location:** Plateau State, Nigeria")
        st.write("**Year:** 2025")

        st.write(
            "Industrial training placement "
            "providing exposure to a "
            "professional workplace."
        )

    with st.container(border=True):

        st.subheader("Computer Operator")

        st.write("**Organization:** Flour Mills Company")
        st.write("**Location:** Kano, Nigeria")
        st.write("**Period:** 2023–2024")

        st.write(
            "Professional experience in computer "
            "operations within an organizational setting."
        )

    with st.container(border=True):

        st.subheader("Computer Operator")

        st.write("**Organization:** Doo Doo Enterprise")
        st.write("**Location:** Jos, Plateau State")
        st.write("**Period:** 2019–2021")

        st.write(
            "Professional experience working "
            "as a computer operator."
        )

    st.subheader("Educational Qualifications")

    st.write(
        f"**{HND_QUALIFICATION}** — "
        f"{HND_SCHOOL}, {HND_YEAR}"
    )

    st.write(
        "**Secondary School Education** — "
        f"{SECONDARY_SCHOOL}, {SECONDARY_YEAR}"
    )

# =====================================================
# 11. RESUME PAGE
# =====================================================

elif page == "Resume":

    st.title("My Professional Resume")

    st.subheader("Professional Summary")

    st.write("""
    Python software developer with experience
    in computer operations and an interest
    in web development, machine learning,
    data analysis, and software system design.
    """)

    st.subheader("Education")

    st.write(
        f"**{HND_QUALIFICATION}** — "
        f"{HND_SCHOOL}, {HND_YEAR}"
    )

    st.write(
        "**Secondary School Education** — "
        f"{SECONDARY_SCHOOL}, {SECONDARY_YEAR}"
    )

    st.subheader("Work Experience")

    st.write("""
    - Appeal Court, Jos — Industrial Training (2025)
    - Flour Mills Company, Kano — Computer Operator (2023–2024)
    - Doo Doo Enterprise, Jos — Computer Operator (2019–2021)
    """)

    st.subheader("Technical Skills")

    st.write(
        "Python, Streamlit, Scikit-learn, "
        "Pandas, SQLite, Machine Learning"
    )

    st.subheader("Download My CV")

    if CV_PATH.is_file():

        st.download_button(
            "📄 Download My Professional CV",
            data=CV_PATH.read_bytes(),
            file_name="Gbenge_Terfa_Nathaniel_CV.pdf",
            mime="application/pdf"
        )

    else:

        st.info(
            "Save your updated professional CV "
            "as cv.pdf inside the "
            "my-python-portfolio folder."
        )

# =====================================================
# 12. CONTACT PAGE
# =====================================================

elif page == "Contact":

    st.title("Contact Me")

    st.write(
        "For software development enquiries "
        "or professional opportunities, "
        "use the contact details below."
    )

    st.subheader("Contact Information")

    st.write(f"**Email:** {EMAIL}")

    st.write(f"**Location:** {LOCATION}")

    st.write(
        "Phone numbers are available "
        "upon direct request."
    )

    st.divider()

    st.subheader("Prepare a Message")

    with st.form("contact_form"):

        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        subject = st.text_input("Subject")
        message = st.text_area(
            "Your Message",
            height=150
        )

        submitted = st.form_submit_button(
            "Prepare Message"
        )

    if submitted:

        if not all([
            name.strip(),
            email.strip(),
            subject.strip(),
            message.strip()
        ]):

            st.warning("Please complete all fields.")

        elif not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+",
            email.strip()
        ):

            st.warning("Enter a valid email address.")

        else:

            prepared_message = (
                f"From: {name}\n"
                f"Email: {email}\n"
                f"Subject: {subject}\n\n"
                f"{message}"
            )

            st.success("Your message is ready to copy.")

            st.code(
                prepared_message,
                language="text"
            )

            st.info(
                "Copy this message and send it "
                "using your email application. "
                "Automatic delivery is not configured."
            )

# =====================================================
# 13. FOOTER
# =====================================================

st.divider()

year = datetime.now().year

st.html(f"""
<div class="footer">
    © {year} GBENGE TERFA NATHANIEL

    <p>
        Python Software Developer |
        Machine Learning Enthusiast
    </p>

    <p>
        Built with Python and Streamlit
    </p>
</div>
""")
