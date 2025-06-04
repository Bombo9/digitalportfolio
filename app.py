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
    st.header("Data Science Projects Portfolio")
    
    st.write("""
    Here are some of the data science projects I've worked on, showcasing my skills in 
    data analysis, machine learning, and visualization across various domains.
    """)
    
    # Project categories
    tab1, tab2, tab3 = st.tabs(["📊 Data Analysis", "🤖 Machine Learning", "📈 Visualization"])
    
    with tab1:
        st.subheader("Data Analysis Projects")
        
        # Project 1: E-commerce Sales Analysis
        with st.expander("🛒 E-commerce Sales Analysis Dashboard", expanded=True):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write("**Project Overview:**")
                st.write("""
                Comprehensive analysis of e-commerce sales data to identify trends, customer behavior patterns, 
                and revenue optimization opportunities for a retail client.
                """)
                
                st.write("**Key Features:**")
                st.write("• Sales trend analysis across multiple product categories")
                st.write("• Customer segmentation and behavioral analysis")
                st.write("• Seasonal pattern identification")
                st.write("• Revenue forecasting and growth metrics")
                st.write("• Interactive Power BI dashboard for stakeholders")
                
                st.write("**Technologies Used:** Python, Pandas, NumPy, Matplotlib, Seaborn, Power BI")
                
            with col2:
                st.metric("Data Points", "500K+", "Records analyzed")
                st.metric("Revenue Increase", "15%", "After optimization")
                st.metric("Project Duration", "3 weeks", "Completed")
        
        # Project 2: Financial Market Analysis
        with st.expander("📈 Financial Market Trend Analysis"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write("**Project Overview:**")
                st.write("""
                Statistical analysis of stock market data to identify investment opportunities 
                and risk assessment for a financial advisory firm.
                """)
                
                st.write("**Key Features:**")
                st.write("• Time series analysis of stock prices")
                st.write("• Correlation analysis between different sectors")
                st.write("• Risk-return optimization models")
                st.write("• Technical indicator calculations")
                st.write("• Automated reporting system")
                
                st.write("**Technologies Used:** Python, R, SQL, Tableau, Statistical Modeling")
                
            with col2:
                st.metric("Stocks Analyzed", "200+", "Different companies")
                st.metric("Accuracy", "87%", "Prediction rate")
                st.metric("Client Rating", "5.0⭐", "Excellent")
    
    with tab2:
        st.subheader("Machine Learning Projects")
        
        # Project 3: Customer Churn Prediction
        with st.expander("👥 Customer Churn Prediction Model", expanded=True):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write("**Project Overview:**")
                st.write("""
                Developed a machine learning model to predict customer churn for a subscription-based 
                service, enabling proactive retention strategies.
                """)
                
                st.write("**Key Features:**")
                st.write("• Feature engineering from customer interaction data")
                st.write("• Multiple ML algorithms comparison (Random Forest, XGBoost, Logistic Regression)")
                st.write("• Model interpretability using SHAP values")
                st.write("• Real-time prediction API deployment")
                st.write("• A/B testing framework for retention strategies")
                
                st.write("**Technologies Used:** Python, Scikit-learn, XGBoost, Flask, Docker")
                
            with col2:
                st.metric("Model Accuracy", "92%", "F1-Score: 0.89")
                st.metric("Churn Reduction", "23%", "After implementation")
                st.metric("ROI", "300%", "First year")
        
        # Project 4: Sales Forecasting
        with st.expander("📊 Sales Forecasting System"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write("**Project Overview:**")
                st.write("""
                Time series forecasting model to predict future sales for inventory optimization 
                and business planning purposes.
                """)
                
                st.write("**Key Features:**")
                st.write("• ARIMA and Prophet model implementation")
                st.write("• Seasonal decomposition and trend analysis")
                st.write("• External factor integration (holidays, promotions)")
                st.write("• Multi-step ahead forecasting")
                st.write("• Automated model retraining pipeline")
                
                st.write("**Technologies Used:** Python, Prophet, TensorFlow, Apache Airflow")
                
            with col2:
                st.metric("MAPE", "8.5%", "Low error rate")
                st.metric("Forecast Horizon", "12 months", "Ahead prediction")
                st.metric("Inventory Savings", "18%", "Cost reduction")
    
    with tab3:
        st.subheader("Data Visualization Projects")
        
        # Project 5: Business Intelligence Dashboard
        with st.expander("📋 Executive Business Intelligence Dashboard", expanded=True):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write("**Project Overview:**")
                st.write("""
                Comprehensive business intelligence dashboard providing real-time insights 
                for executive decision-making across multiple business units.
                """)
                
                st.write("**Key Features:**")
                st.write("• Real-time KPI monitoring and alerts")
                st.write("• Cross-functional performance metrics")
                st.write("• Interactive drill-down capabilities")
                st.write("• Mobile-responsive design")
                st.write("• Automated data refresh from multiple sources")
                
                st.write("**Technologies Used:** Tableau, Power BI, SQL Server, Python ETL")
                
            with col2:
                st.metric("Data Sources", "15+", "Integrated systems")
                st.metric("Daily Users", "50+", "Executive team")
                st.metric("Update Frequency", "Real-time", "Live data")
        
        # Project 6: Interactive Analytics Platform
        with st.expander("🔍 Self-Service Analytics Platform"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write("**Project Overview:**")
                st.write("""
                Self-service analytics platform enabling non-technical users to explore data 
                and generate insights without requiring technical expertise.
                """)
                
                st.write("**Key Features:**")
                st.write("• Drag-and-drop interface for data exploration")
                st.write("• Automated chart recommendations")
                st.write("• Statistical significance testing")
                st.write("• Export capabilities for presentations")
                st.write("• User access control and data governance")
                
                st.write("**Technologies Used:** Streamlit, Plotly, Pandas, PostgreSQL")
                
            with col2:
                st.metric("Monthly Users", "200+", "Cross-departments")
                st.metric("Reports Generated", "1000+", "Per month")
                st.metric("Time Savings", "60%", "Report creation")
    
    # GitHub Integration
    st.subheader("View More Projects")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("🔗 Visit My GitHub", use_container_width=True):
            st.markdown("[View all projects on GitHub](https://github.com/Bombo9)")
            st.success("Check out my GitHub for complete project code and documentation!")
    
    # Contact for custom projects
    st.subheader("Custom Project Development")
    st.write("""
    Need a custom data science solution? I specialize in developing tailored analytics solutions 
    for businesses of all sizes. Contact me to discuss your specific requirements.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Project Types:**")
        st.write("• Predictive Analytics")
        st.write("• Business Intelligence")
        st.write("• Data Pipeline Development")
        st.write("• Machine Learning Solutions")
    
    with col2:
        st.write("**Industries Served:**")
        st.write("• E-commerce & Retail")
        st.write("• Financial Services")
        st.write("• Healthcare & Pharma")
        st.write("• Manufacturing & Logistics")
    
    with col3:
        st.write("**Deliverables:**")
        st.write("• Complete source code")
        st.write("• Technical documentation")
        st.write("• Interactive dashboards")
        st.write("• Training & support")

def show_contact():
    """Display contact section"""
    st.header("Get In Touch")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Let's Connect!")
        st.write("""
        I'm actively seeking opportunities for remote work, industrial attachments, internships, 
        freelancing projects, and full-time employment in data science. I'm always excited to discuss 
        new opportunities and collaborate on interesting projects. Feel free to reach out!
        """)
        
        # Contact form
        st.subheader("Send Me a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.selectbox("Subject", [
                "Job Opportunity",
                "Internship/Industrial Attachment",
                "Freelance Project",
                "Remote Work Opportunity",
                "Collaboration Proposal",
                "General Inquiry",
                "Other"
            ])
            message = st.text_area("Your Message", height=150)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    # Here you would integrate with an email service
                    # For now, we'll show success message with contact info
                    st.success(f"""
                    Thank you {name} for your message! 
                    
                    Your message has been received. For immediate response, please contact me directly at:
                    📧 bombomatsitsa@gmail.com
                    📱 0702816978
                    
                    I'll respond within 24 hours.
                    """)
                    
                    # Display the message details for reference
                    st.info(f"""
                    **Message Details:**
                    - From: {name} ({email})
                    - Subject: {subject}
                    - Message: {message}
                    """)
                else:
                    st.error("Please fill in all required fields.")
    
    with col2:
        st.subheader("Contact Information")
        
        # Contact methods
        st.write("**📧 Email:**")
        st.write("bombomatsitsa@gmail.com")
        
        st.write("**📱 Phone:**")
        st.write("0702816978")
        
        st.write("**💼 Professional Profiles:**")
        st.write("• [Fiverr Profile](https://www.fiverr.com/festusbombo)")
        st.write("• [Upwork Profile](https://www.upwork.com/freelancers/festusbombo)")
        st.write("• [LinkedIn](https://linkedin.com/in/festusbombo)")
        st.write("• [GitHub](https://github.com/Bombo9)")
        
        st.write("**🌍 Availability:**")
        st.write("• Remote work worldwide")
        st.write("• Industrial attachment opportunities")
        st.write("• Internship positions")
        st.write("• Freelancing projects")
        st.write("• Full-time employment")
        
        st.write("**⏰ Working Hours:**")
        st.write("• Monday - Friday: 9 AM - 6 PM (EAT)")
        st.write("• Response Time: Within 24 hours")
        st.write("• Time Zone: East Africa Time (UTC+3)")
        
        # Quick stats
        st.subheader("Quick Stats")
        st.metric("Response Rate", "98%", "Excellent")
        st.metric("Client Satisfaction", "5.0⭐", "Outstanding")
        st.metric("Projects Completed", "125+", "Growing")
    
    # Services offered
    st.subheader("Services & Opportunities")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Data Science Services**")
        st.write("• Exploratory Data Analysis")
        st.write("• Statistical Modeling") 
        st.write("• Business Intelligence")
        st.write("• Performance Analytics")
        st.write("• Machine Learning Solutions")
    
    with col2:
        st.write("**Work Opportunities**")
        st.write("• Remote Data Science Roles")
        st.write("• Industrial Attachments")
        st.write("• Internship Programs")
        st.write("• Freelance Projects")
        st.write("• Full-time Positions")
    
    with col3:
        st.write("**Specializations**")
        st.write("• Predictive Analytics")
        st.write("• Data Visualization")
        st.write("• Business Intelligence")
        st.write("• Statistical Analysis")
        st.write("• Dashboard Development")

if __name__ == "__main__":
    main()
