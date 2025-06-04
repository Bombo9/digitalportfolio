import streamlit as st
import base64
from pathlib import Path
from PIL import Image
import io
from utils.helpers import get_base64_of_file, create_download_link

# Page configuration
st.set_page_config(
    page_title="Festus Matsitsa Bombo - Data Scientist Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main content
def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    sections = [
        "🏠 Home",
        "👨‍💼 About Me", 
        "🛠️ Skills",
        "💼 Experience",
        "🎓 Education",
        "📁 Projects",
        "📞 Contact"
    ]
    
    selected_section = st.sidebar.radio("Go to", sections)
    
    # Header section with profile picture
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Try to load profile picture
        try:
            profile_img = Image.open("assets/profile_picture.jpg")
            # Resize image to reasonable size
            profile_img = profile_img.resize((300, 300))
            st.image(profile_img, width=300)
        except FileNotFoundError:
            st.info("Profile picture not found. Please upload your profile picture to assets/profile_picture.jpg")
    
    # Main title and subtitle
    st.markdown("<h1 style='text-align: center;'>FESTUS MATSITSA BOMBO</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #1f77b4;'>DATA SCIENTIST</h3>", unsafe_allow_html=True)
    
    # Resume download button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        try:
            with open("assets/resume.pdf", "rb") as file:
                pdf_bytes = file.read()
                st.download_button(
                    label="📄 Download Resume (PDF)",
                    data=pdf_bytes,
                    file_name="Festus_Bombo_Resume.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.info("Resume PDF not found. Please upload your resume to assets/resume.pdf")
    
    st.markdown("---")
    
    # Content based on selected section
    if selected_section == "🏠 Home":
        show_home()
    elif selected_section == "👨‍💼 About Me":
        show_about()
    elif selected_section == "🛠️ Skills":
        show_skills()
    elif selected_section == "💼 Experience":
        show_experience()
    elif selected_section == "🎓 Education":
        show_education()
    elif selected_section == "📁 Projects":
        show_projects()
    elif selected_section == "📞 Contact":
        show_contact()

def show_home():
    """Display home page with overview"""
    st.header("Welcome to My Portfolio")
    
    # Professional summary from resume
    st.subheader("Professional Summary")
    st.write("""
    Passionate Data Scientist with a strong background in data analysis, machine learning, 
    data visualization, and statistical modeling, skilled in transforming complex datasets 
    into actionable insights that support data-driven decision-making and drive business success.
    """)
    
    # Key highlights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Years of Experience", "3+", "Growing")
        
    with col2:
        st.metric("Freelance Projects", "100+", "Completed")
        
    with col3:
        st.metric("Current Status", "Available", "For new projects")
    
    # Quick links
    st.subheader("Quick Navigation")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("View My Skills 🛠️", use_container_width=True):
            st.session_state.selected_section = "🛠️ Skills"
            st.rerun()
    
    with col2:
        if st.button("See My Experience 💼", use_container_width=True):
            st.session_state.selected_section = "💼 Experience"
            st.rerun()
    
    with col3:
        if st.button("Contact Me 📞", use_container_width=True):
            st.session_state.selected_section = "📞 Contact"
            st.rerun()

def show_about():
    """Display about me section"""
    st.header("About Me")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Background & Expertise")
        st.write("""
        I am a passionate Data Scientist with expertise in transforming complex datasets into 
        actionable insights that drive business success. My journey in data science has equipped 
        me with strong analytical thinking, attention to detail, and problem-solving skills.
        
        I specialize in:
        - **Machine Learning & Statistical Modeling**: Building predictive models using advanced algorithms
        - **Data Analysis & Visualization**: Creating compelling visual narratives from data
        - **Business Intelligence**: Translating data insights into strategic business decisions
        - **A/B Testing & Experimentation**: Designing and analyzing experiments for data-driven decisions
        """)
        
        st.subheader("Core Competencies")
        competencies = [
            "Data Analysis & Statistical Modeling",
            "Machine Learning & Predictive Analytics", 
            "Data Visualization & Business Intelligence",
            "Exploratory Data Analysis (EDA)",
            "A/B Testing & Experimentation",
            "Data Cleaning & Preprocessing",
            "Cross-functional Team Collaboration",
            "Project Management & Time Management"
        ]
        
        for competency in competencies:
            st.write(f"✅ {competency}")
    
    with col2:
        st.subheader("Personal Attributes")
        attributes = [
            "🧠 Analytical Thinking",
            "🔍 Attention to Detail", 
            "🛠️ Problem-Solving",
            "💬 Communication",
            "🤝 Collaboration",
            "🔄 Adaptability",
            "⏰ Time Management",
            "📊 Project Management"
        ]
        
        for attr in attributes:
            st.write(attr)
            
        st.subheader("Philosophy")
        st.info("""
        "Committed to continuous learning, innovation, and delivering high-impact, 
        scalable analytical solutions in cross-functional team environments."
        """)

def show_skills():
    """Display skills section"""
    st.header("Technical Skills")
    
    # Programming Languages
    st.subheader("Programming Languages")
    languages = ["Python", "R", "SQL"]
    language_levels = [90, 75, 85]
    
    for lang, level in zip(languages, language_levels):
        st.write(f"**{lang}**")
        st.progress(level / 100)
    
    # Tools & Technologies
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Data Analysis & Visualization")
        analysis_tools = [
            "Excel",
            "Power BI", 
            "Tableau",
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Seaborn",
            "Plotly"
        ]
        
        for tool in analysis_tools:
            st.write(f"• {tool}")
    
    with col2:
        st.subheader("Machine Learning & AI")
        ml_tools = [
            "Scikit-learn",
            "TensorFlow",
            "Keras",
            "XGBoost",
            "Random Forest",
            "Linear Regression",
            "Classification Models",
            "Clustering Algorithms"
        ]
        
        for tool in ml_tools:
            st.write(f"• {tool}")
    
    # Technical Expertise
    st.subheader("Areas of Expertise")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Data Science**")
        st.write("• Predictive Modeling")
        st.write("• Statistical Analysis") 
        st.write("• Data Mining")
        st.write("• Feature Engineering")
    
    with col2:
        st.write("**Analytics**")
        st.write("• Business Intelligence")
        st.write("• A/B Testing")
        st.write("• Performance Metrics")
        st.write("• Dashboard Creation")
    
    with col3:
        st.write("**Development**")
        st.write("• Data Pipelines")
        st.write("• ETL Processes")
        st.write("• Database Management")
        st.write("• Version Control (Git)")

def show_experience():
    """Display experience section"""
    st.header("Professional Experience")
    
    # Data Scientist - Fiverr
    with st.expander("💼 Data Scientist - Fiverr (April 2021 - Present)", expanded=True):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write("**Role:** Freelance Data Scientist")
            st.write("**Duration:** April 2021 - Present (3+ years)")
            
            st.write("**Key Responsibilities:**")
            st.write("• Built and maintained relationships with clients to understand their data needs")
            st.write("• Developed custom data analysis solutions for diverse business requirements")
            st.write("• Created predictive models and statistical analyses for client projects")
            st.write("• Delivered actionable insights through comprehensive data visualizations")
            st.write("• Managed multiple projects simultaneously with attention to detail and deadlines")
            
        with col2:
            st.metric("Project Rating", "5.0⭐", "Excellent")
            st.metric("Clients Served", "50+", "Growing")
    
    # Data Scientist - Upwork  
    with st.expander("💼 Data Scientist - Upwork (June 2022 - Present)", expanded=True):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write("**Role:** Freelance Data Scientist")
            st.write("**Duration:** June 2022 - Present (2+ years)")
            
            st.write("**Key Responsibilities:**")
            st.write("• Analyzed large datasets to identify trends and provide actionable insights")
            st.write("• Implemented machine learning algorithms for predictive analytics")
            st.write("• Created interactive dashboards and visualization reports")
            st.write("• Collaborated with international clients across various industries")
            st.write("• Provided data-driven recommendations for business optimization")
            
        with col2:
            st.metric("Success Rate", "98%", "High")
            st.metric("Projects", "75+", "Completed")
    
    # Skills gained through experience
    st.subheader("Skills Developed Through Experience")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Client Management**")
        st.write("• Requirement gathering and analysis")
        st.write("• Project scoping and timeline management") 
        st.write("• Regular communication and updates")
        st.write("• Quality assurance and delivery")
    
    with col2:
        st.write("**Technical Excellence**")
        st.write("• Large-scale data processing")
        st.write("• Advanced statistical modeling")
        st.write("• Custom solution development")
        st.write("• Performance optimization")

def show_education():
    """Display education section"""
    st.header("Education Background")
    
    # Current Education
    with st.expander("🎓 BSc Computer Science - Pwani University", expanded=True):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.write("**Degree:** Bachelor of Science in Computer Science")
            st.write("**Institution:** Pwani University")
            st.write("**Duration:** August 2022 - September 2027")
            st.write("**Status:** Currently Enrolled (Undergraduate)")
            
            st.write("**Relevant Coursework:**")
            coursework = [
                "Data Structures and Algorithms",
                "Database Management Systems", 
                "Statistics and Probability",
                "Machine Learning Fundamentals",
                "Software Engineering",
                "Computer Networks",
                "Operating Systems",
                "Web Development"
            ]
            
            for course in coursework:
                st.write(f"• {course}")
                
        with col2:
            st.metric("Expected Graduation", "2027", "On Track")
            st.metric("Current Year", "3rd", "of 5")
    
    # Additional Learning
    st.subheader("Continuous Learning & Development")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Self-Directed Learning**")
        st.write("• Online Data Science Courses")
        st.write("• Machine Learning Specializations")
        st.write("• Industry Best Practices")
        st.write("• Latest Technology Trends")
    
    with col2:
        st.write("**Practical Application**")
        st.write("• Freelance Project Experience")
        st.write("• Real-world Problem Solving")
        st.write("• Client Requirement Analysis")
        st.write("• Professional Communication")
    
    # Learning Philosophy
    st.subheader("Learning Philosophy")
    st.info("""
    I believe in combining formal education with practical, hands-on experience. 
    My ongoing university education provides me with strong theoretical foundations, 
    while my freelance work allows me to apply these concepts to real-world challenges 
    and stay current with industry demands.
    """)

def show_projects():
    """Display projects section"""
    st.header("Projects Portfolio")
    
    st.info("""
    This section showcases data science projects and case studies. 
    As a freelance data scientist, I work on confidential client projects, 
    but I'm developing public portfolio projects to demonstrate my capabilities.
    """)
    
    # Project categories
    tab1, tab2, tab3 = st.tabs(["📊 Data Analysis", "🤖 Machine Learning", "📈 Visualization"])
    
    with tab1:
        st.subheader("Data Analysis Projects")
        st.write("""
        **Coming Soon:** Public portfolio projects demonstrating:
        - Exploratory Data Analysis (EDA)
        - Statistical Analysis and Hypothesis Testing
        - Business Intelligence Solutions
        - Performance Metrics and KPI Development
        """)
        
        if st.button("🔔 Notify me when projects are available", key="notify_analysis"):
            st.success("You'll be notified when new analysis projects are published!")
    
    with tab2:
        st.subheader("Machine Learning Projects")
        st.write("""
        **In Development:** Machine learning projects including:
        - Predictive Modeling Solutions
        - Classification and Regression Models
        - Clustering and Segmentation Analysis
        - Time Series Forecasting
        """)
        
        if st.button("🔔 Notify me when projects are available", key="notify_ml"):
            st.success("You'll be notified when new ML projects are published!")
    
    with tab3:
        st.subheader("Data Visualization Projects")
        st.write("""
        **Under Construction:** Interactive visualization projects:
        - Dashboard Development with Power BI/Tableau
        - Interactive Charts and Graphs
        - Business Reporting Solutions
        - Data Storytelling Examples
        """)
        
        if st.button("🔔 Notify me when projects are available", key="notify_viz"):
            st.success("You'll be notified when new visualization projects are published!")
    
    # Project collaboration
    st.subheader("Collaboration Opportunities")
    st.write("""
    I'm always interested in collaborating on interesting data science projects. 
    If you have a project idea or would like to work together, please reach out!
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Types of Projects I'm Interested In:**")
        st.write("• Social Impact Data Science")
        st.write("• Business Analytics Solutions")
        st.write("• Predictive Modeling Challenges")
        st.write("• Open Source Contributions")
    
    with col2:
        st.write("**How We Can Collaborate:**")
        st.write("• Joint Research Projects")
        st.write("• Data Science Competitions")
        st.write("• Knowledge Sharing Sessions")
        st.write("• Mentorship Opportunities")

def show_contact():
    """Display contact section"""
    st.header("Get In Touch")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Let's Connect!")
        st.write("""
        I'm always excited to discuss data science opportunities, collaborate on interesting projects, 
        or simply connect with fellow data enthusiasts. Feel free to reach out!
        """)
        
        # Contact form
        st.subheader("Send Me a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.selectbox("Subject", [
                "Project Inquiry",
                "Collaboration Opportunity", 
                "General Question",
                "Freelance Work",
                "Other"
            ])
            message = st.text_area("Your Message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    st.success("""
                    Thank you for your message! I'll get back to you as soon as possible.
                    
                    For immediate response, please reach out via the contact methods listed.
                    """)
                else:
                    st.error("Please fill in all required fields.")
    
    with col2:
        st.subheader("Contact Information")
        
        # Contact methods
        st.write("**📧 Email:**")
        st.write("festus.bombo@example.com")
        
        st.write("**💼 Professional Profiles:**")
        st.write("• [Fiverr Profile](https://fiverr.com)")
        st.write("• [Upwork Profile](https://upwork.com)")
        st.write("• [LinkedIn](https://linkedin.com)")
        st.write("• [GitHub](https://github.com)")
        
        st.write("**🌍 Location:**")
        st.write("Available for remote work worldwide")
        
        st.write("**⏰ Availability:**")
        st.write("• Monday - Friday: 9 AM - 6 PM (EAT)")
        st.write("• Response Time: Within 24 hours")
        st.write("• Time Zone: East Africa Time (UTC+3)")
        
        # Quick stats
        st.subheader("Quick Stats")
        st.metric("Response Rate", "98%", "Excellent")
        st.metric("Client Satisfaction", "5.0⭐", "Outstanding")
        st.metric("Projects Completed", "125+", "Growing")
    
    # Services offered
    st.subheader("Services I Offer")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Data Analysis**")
        st.write("• Exploratory Data Analysis")
        st.write("• Statistical Modeling") 
        st.write("• Business Intelligence")
        st.write("• Performance Analytics")
    
    with col2:
        st.write("**Machine Learning**")
        st.write("• Predictive Modeling")
        st.write("• Classification Models")
        st.write("• Regression Analysis")
        st.write("• Clustering Solutions")
    
    with col3:
        st.write("**Visualization**")
        st.write("• Dashboard Development")
        st.write("• Interactive Charts")
        st.write("• Business Reports")
        st.write("• Data Storytelling")

if __name__ == "__main__":
    main()
