"""
Helper functions for the Streamlit portfolio application
"""

import base64
import streamlit as st
from pathlib import Path

def get_base64_of_file(path):
    """
    Convert a file to base64 encoding
    
    Args:
        path (str): Path to the file
        
    Returns:
        str: Base64 encoded string of the file
    """
    try:
        with open(path, "rb") as file:
            contents = file.read()
        return base64.b64encode(contents).decode()
    except FileNotFoundError:
        st.error(f"File not found: {path}")
        return None

def create_download_link(file_path, download_filename, link_text):
    """
    Create a download link for a file
    
    Args:
        file_path (str): Path to the file to be downloaded
        download_filename (str): Name for the downloaded file
        link_text (str): Text to display for the link
        
    Returns:
        str: HTML string for the download link
    """
    try:
        with open(file_path, "rb") as file:
            contents = file.read()
        
        b64 = base64.b64encode(contents).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{download_filename}">{link_text}</a>'
        return href
    except FileNotFoundError:
        return f"<span style='color: red;'>File not found: {file_path}</span>"

def load_css(css_file):
    """
    Load CSS file for custom styling
    
    Args:
        css_file (str): Path to CSS file
    """
    try:
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file not found: {css_file}")

def display_skill_bar(skill_name, proficiency_level):
    """
    Display a skill with a progress bar
    
    Args:
        skill_name (str): Name of the skill
        proficiency_level (int): Proficiency level (0-100)
    """
    st.write(f"**{skill_name}**")
    st.progress(proficiency_level / 100)
    st.write("")  # Add some spacing

def create_metric_card(title, value, delta=None):
    """
    Create a metric card with title, value, and optional delta
    
    Args:
        title (str): Title of the metric
        value (str): Value to display
        delta (str, optional): Delta value to show change
    """
    if delta:
        st.metric(title, value, delta)
    else:
        st.metric(title, value)

def format_experience_duration(start_date, end_date=None):
    """
    Format experience duration for display
    
    Args:
        start_date (str): Start date of experience
        end_date (str, optional): End date, defaults to "Present"
        
    Returns:
        str: Formatted duration string
    """
    if end_date is None:
        end_date = "Present"
    return f"{start_date} - {end_date}"

def create_contact_info(email=None, phone=None, location=None, linkedin=None, github=None):
    """
    Create formatted contact information
    
    Args:
        email (str, optional): Email address
        phone (str, optional): Phone number
        location (str, optional): Location
        linkedin (str, optional): LinkedIn profile URL
        github (str, optional): GitHub profile URL
    """
    contact_info = []
    
    if email:
        contact_info.append(f"📧 **Email:** {email}")
    if phone:
        contact_info.append(f"📱 **Phone:** {phone}")
    if location:
        contact_info.append(f"📍 **Location:** {location}")
    if linkedin:
        contact_info.append(f"💼 **LinkedIn:** [{linkedin}]({linkedin})")
    if github:
        contact_info.append(f"💻 **GitHub:** [{github}]({github})")
    
    return "\n\n".join(contact_info)

def validate_email(email):
    """
    Simple email validation
    
    Args:
        email (str): Email address to validate
        
    Returns:
        bool: True if email format is valid
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_file_size(file_path):
    """
    Get file size in human readable format
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        str: File size in human readable format
    """
    try:
        size = Path(file_path).stat().st_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
    except FileNotFoundError:
        return "File not found"

# Constants for the application
SKILLS_DATA = {
    "Programming Languages": {
        "Python": 95,
        "R": 80,
        "SQL": 90,
        "JavaScript": 70
    },
    "Data Science Tools": {
        "Pandas": 95,
        "NumPy": 90,
        "Scikit-learn": 85,
        "TensorFlow": 80,
        "Matplotlib": 90,
        "Seaborn": 85
    },
    "Visualization Tools": {
        "Tableau": 85,
        "Power BI": 80,
        "Plotly": 75,
        "Excel": 90
    }
}

SOCIAL_LINKS = {
    "Fiverr": "https://www.fiverr.com/festusbombo",
    "Upwork": "https://www.upwork.com/freelancers/festusbombo", 
    "LinkedIn": "https://linkedin.com/in/festusbombo",
    "GitHub": "https://github.com/festusbombo",
    "Email": "mailto:festus.bombo@example.com"
}

PROJECT_CATEGORIES = [
    "Data Analysis",
    "Machine Learning", 
    "Data Visualization",
    "Business Intelligence",
    "Statistical Modeling",
    "A/B Testing"
]
