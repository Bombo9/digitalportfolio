# Deployment Instructions

## For Streamlit Cloud Deployment

### Step 1: Prepare Files
1. Rename `requirements_deployment.txt` to `requirements.txt`
2. Upload your project to GitHub
3. Ensure these files are in your repository:
   - `app.py` (main application)
   - `requirements.txt` (dependencies)
   - `.streamlit/config.toml` (configuration)
   - `assets/profile_picture.jpg` (your photo)
   - `assets/resume.pdf` (your resume)

### Step 2: Deploy
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Choose `app.py` as main file
6. Click "Deploy"

### Step 3: Verify
- Check all sections load properly
- Test resume download
- Verify contact form functionality

## For VS Code Development

### Quick Setup Commands
```bash
# Install dependencies
pip install streamlit>=1.28.0 Pillow>=9.0.0

# Run locally
streamlit run app.py

# Or use the runner script
python run_portfolio.py
```

### File Structure
```
portfolio/
├── app.py                    # Main application
├── streamlit_app.py         # Alternative entry point
├── requirements_deployment.txt # Dependencies for local dev
├── pyproject.toml           # Project configuration
├── .streamlit/
│   └── config.toml         # Streamlit settings
├── assets/
│   ├── profile_picture.jpg # Your photo
│   └── resume.pdf         # Your resume
└── utils/
    └── helpers.py         # Helper functions
```

## Troubleshooting

### Common Issues
1. **Missing assets**: Ensure profile picture and resume are in `assets/` folder
2. **Import errors**: Install Pillow: `pip install Pillow>=9.0.0`
3. **Port conflicts**: Use different port: `streamlit run app.py --server.port 8502`

### For Deployment
- Streamlit Cloud requires `requirements.txt` (not `requirements_deployment.txt`)
- Ensure all files are committed to Git
- Public repositories work best for free tier