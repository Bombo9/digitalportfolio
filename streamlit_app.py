import streamlit as st
import base64
from pathlib import Path
from PIL import Image
import io
import os

# Page configuration
st.set_page_config(
    page_title="Festus Matsitsa Bombo - Data Scientist Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_base64_of_file(path):
    """Convert a file to base64 encoding"""
    try:
        with open(path, "rb") as file:
            contents = file.read()
        return base64.b64encode(contents).decode()
    except FileNotFoundError:
        return None

def create_download_link(file_path, download_filename, link_text):
    """Create a download link for a file"""
    try:
        with open(file_path, "rb") as file:
            contents = file.read()
        
        b64 = base64.b64encode(contents).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{download_filename}">{link_text}</a>'
        return href
    except FileNotFoundError:
        return f"<span style='color: red;'>File not found: {file_path}</span>"

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
            if os.path.exists("assets/profile_picture.jpg"):
                profile_img = Image.open("assets/profile_picture.jpg")
                # Resize image to reasonable size while maintaining aspect ratio
                profile_img = profile_img.resize((300, 300), Image.Resampling.LANCZOS)
                st.image(profile_img, width=300, caption="Festus Matsitsa Bombo")
            else:
                # Fallback display for deployment without image
                st.markdown("""
                <div style='text-align: center; padding: 20px; border: 2px dashed #ccc; border-radius: 10px;'>
                    <h3>👤 Festus Matsitsa Bombo</h3>
                    <p>Data Scientist Portfolio</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            # Fallback display for any image loading issues
            st.markdown("""
            <div style='text-align: center; padding: 20px; border: 2px dashed #ccc; border-radius: 10px;'>
                <h3>👤 Festus Matsitsa Bombo</h3>
                <p>Data Scientist Portfolio</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Main title and subtitle
    st.markdown("<h1 style='text-align: center;'>FESTUS MATSITSA BOMBO</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #1f77b4;'>DATA SCIENTIST</h3>", unsafe_allow_html=True)
    
    # Resume download button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        try:
            if os.path.exists("assets/resume.pdf"):
                with open("assets/resume.pdf", "rb") as file:
                    pdf_bytes = file.read()
                    st.download_button(
                        label="📄 Download Resume (PDF)",
                        data=pdf_bytes,
                        file_name="Festus_Bombo_Resume.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
            else:
                st.info("📄 Resume download will be available when PDF is uploaded")
        except Exception as e:
            st.info("📄 Resume download temporarily unavailable")
    
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
        st.metric("Current Status", "Available", "Open to opportunities")
    
    # Quick links
    st.subheader("Quick Navigation")
    st.write("Use the sidebar navigation to explore different sections of my portfolio:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🛠️ Skills Section**")
        st.write("View my technical skills and expertise in data science tools and technologies.")
    
    with col2:
        st.markdown("**💼 Experience Section**")
        st.write("Explore my professional experience and freelance work history.")
    
    with col3:
        st.markdown("**📞 Contact Section**")
        st.write("Get in touch for job opportunities, internships, or project collaborations.")

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
            
        st.subheader("Current Status")
        st.success("""
        🎯 Actively seeking opportunities for:
        • Remote data science positions
        • Industrial attachment programs
        • Internship opportunities
        • Freelance data projects
        • Full-time employment
        """)
        
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
                "Computer Programming",
                "Data Mining Techniques",
                "Information Systems"
            ]
            
            for course in coursework:
                st.write(f"• {course}")
                
        with col2:
            st.metric("Current Year", "3rd", "Ongoing")
            st.metric("Expected Graduation", "2027", "On Track")

def show_projects():
    """Display projects section"""
    st.header("Portfolio Projects")
    
    st.write("""
    Here are some of the key projects I've worked on across different domains of data science.
    Each project demonstrates different aspects of my skills and expertise.
    """)
    
    # Project 1: Sales Analysis Dashboard
    with st.expander("📊 Sales Performance Analysis Dashboard", expanded=True):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write("**Project Type:** Business Intelligence & Data Visualization")
            st.write("**Tools Used:** Python, Pandas, Plotly, Power BI")
            st.write("**Duration:** 2 weeks")
            
            st.write("**Description:**")
            st.write("""
            Developed a comprehensive sales dashboard for a retail client to track performance metrics, 
            identify trends, and optimize business operations. The dashboard included real-time data 
            visualization, automated reporting, and predictive analytics for sales forecasting.
            """)
            
            st.write("**Key Features:**")
            st.write("• Interactive sales performance charts")
            st.write("• Regional and product-wise analysis")
            st.write("• Automated monthly reporting")
            st.write("• Sales forecasting models")
            
        with col2:
            st.metric("Client Rating", "5.0⭐")
            st.metric("Project Value", "$2,500")
            st.metric("Completion Time", "14 days")

def show_contact():
    """Display contact section"""
    st.header("Contact Information")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Get In Touch")
        st.write("""
        I'm always interested in discussing new opportunities, collaborations, or 
        answering questions about data science projects. Feel free to reach out!
        """)
        
        # Contact form
        st.subheader("Send a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.selectbox("Subject", [
                "Job Opportunity", 
                "Project Collaboration", 
                "Consultation Request",
                "General Inquiry"
            ])
            message = st.text_area("Message", height=100)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    st.success("Thank you for your message! I'll get back to you within 24 hours.")
                else:
                    st.error("Please fill in all required fields.")
    
    with col2:
        st.subheader("Contact Details")
        
        contact_info = {
            "📧 Email": "bombomatsitsa@gmail.com",
            "📱 Phone": "0702816978",
            "💼 LinkedIn": "https://linkedin.com/in/festusbombo",
            "💻 GitHub": "https://github.com/Bombo9",
            "🌐 Fiverr": "https://www.fiverr.com/festusbombo",
            "⚡ Upwork": "https://www.upwork.com/freelancers/festusbombo"
        }
        
        for label, info in contact_info.items():
            if info.startswith("http"):
                st.write(f"{label}: [{info}]({info})")
            else:
                st.write(f"{label}: {info}")
        
        st.subheader("Availability")
        st.write("""
        I'm particularly interested in:
        - Data Science opportunities
        - Machine Learning projects  
        - Business Intelligence consulting
        - Freelance collaborations
        - Industrial attachment programs
        - Full-time remote positions
        """)

if __name__ == "__main__":
    main()
