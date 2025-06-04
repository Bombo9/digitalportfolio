# Festus Matsitsa Bombo - Data Scientist Portfolio

A professional Streamlit portfolio website showcasing data science skills, projects, and experience.

## Features

- Professional portfolio layout with navigation
- Resume download functionality
- Skills showcase with progress indicators
- Detailed project portfolio
- Contact form with direct contact information
- Responsive design optimized for all devices

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd portfolio-streamlit
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements_deployment.txt
   ```
   
   Or using the project file:
   ```bash
   pip install -e .
   ```

3. **Ensure assets are in place**
   - Profile picture: `assets/profile_picture.jpg`
   - Resume PDF: `assets/resume.pdf`

### Running Locally

#### Method 1: Command Line
```bash
streamlit run app.py
```

#### Method 2: VS Code
1. Open the project folder in VS Code
2. Open terminal in VS Code (Terminal > New Terminal)
3. Run the command:
   ```bash
   streamlit run app.py
   ```
4. The application will open in your default browser at `http://localhost:8501`

#### Method 3: VS Code with specific port
```bash
streamlit run app.py --server.port 5000
```

### VS Code Setup

1. **Install Python Extension**
   - Install the Python extension by Microsoft in VS Code

2. **Select Python Interpreter**
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
   - Type "Python: Select Interpreter"
   - Choose your Python installation

3. **Install Dependencies**
   - Open terminal in VS Code
   - Run: `pip install -r requirements_deployment.txt`

4. **Run the Application**
   - Open terminal in VS Code
   - Run: `streamlit run app.py`

## Deployment

### Streamlit Community Cloud

1. **Prepare Repository**
   - Push code to GitHub repository
   - Ensure `requirements_deployment.txt` is in root directory (rename to `requirements.txt` for deployment)
   - Ensure all assets are included
   - Main file can be either `app.py` or `streamlit_app.py`

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Choose `app.py` as the main file
   - Click "Deploy"

3. **Configuration**
   - The app uses the configuration in `.streamlit/config.toml`
   - No additional setup required for basic deployment

### Other Deployment Options

- **Heroku**: Use the included configuration files
- **AWS/GCP**: Deploy using container services
- **Local Network**: Run with `--server.address 0.0.0.0`

## File Structure

```
portfolio-streamlit/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── assets/
│   ├── profile_picture.jpg # Your profile photo
│   └── resume.pdf        # Your resume PDF
└── utils/
    └── helpers.py        # Helper functions
```

## Customization

### Personal Information
- Update contact details in `utils/helpers.py`
- Modify personal information in `app.py`

### Profile Assets
- Replace `assets/profile_picture.jpg` with your photo
- Replace `assets/resume.pdf` with your resume

### Content
- Edit sections in `app.py` for different content
- Modify projects, skills, and experience sections

## Contact Information

- **Email**: bombomatsitsa@gmail.com
- **Phone**: 0702816978
- **GitHub**: https://github.com/Bombo9

## License

This project is open source and available under the MIT License.