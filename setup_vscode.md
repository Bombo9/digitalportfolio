# VS Code Setup Guide for Streamlit Portfolio

## Quick Start

1. **Open VS Code**
   - Open the portfolio folder in VS Code
   - File > Open Folder > Select your portfolio directory

2. **Install Python Extension**
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Python" by Microsoft
   - Click Install

3. **Set Up Python Environment**
   - Open Command Palette (Ctrl+Shift+P)
   - Type "Python: Select Interpreter"
   - Choose your Python installation (3.7+ required)

4. **Install Dependencies**
   ```bash
   pip install -r requirements_deployment.txt
   ```

5. **Run the Portfolio**
   Choose one of these methods:

   **Method A: Using Terminal**
   - Open Terminal (Ctrl+` or Terminal > New Terminal)
   - Run: `streamlit run app.py`

   **Method B: Using Run Script**
   - Run: `python run_portfolio.py`
   
   **Method C: With Custom Port**
   - Run: `streamlit run app.py --server.port 5000`

## VS Code Extensions (Recommended)

- **Python** by Microsoft - Essential for Python development
- **Python Docstring Generator** - For documentation
- **Pylance** - Enhanced Python language support
- **GitLens** - Git integration (if using version control)

## Configuration

### Launch Configuration (Optional)
Create `.vscode/launch.json` for debugging:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run Streamlit Portfolio",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "args": [
                "run",
                "app.py",
                "--server.port",
                "8501"
            ],
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

### Workspace Settings
Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "python",
    "python.terminal.activateEnvironment": true,
    "files.associations": {
        "*.py": "python"
    }
}
```

## Troubleshooting

### Common Issues

1. **Python not found**
   - Ensure Python is installed and in PATH
   - Restart VS Code after Python installation

2. **Streamlit command not found**
   - Run: `pip install streamlit>=1.28.0`
   - Check if pip is using correct Python version

3. **Port already in use**
   - Use different port: `streamlit run app.py --server.port 8502`
   - Or kill existing process

4. **Assets not loading**
   - Ensure `assets/` folder contains:
     - `profile_picture.jpg`
     - `resume.pdf`

### Performance Tips

- Close unused browser tabs
- Use VS Code integrated terminal
- Install extensions only as needed
- Use Python virtual environment for isolation

## Development Workflow

1. **Edit Code**
   - Make changes to `app.py` or other files
   - Streamlit auto-reloads on file changes

2. **View Changes**
   - Browser automatically refreshes
   - Check terminal for any error messages

3. **Debug Issues**
   - Use VS Code debugger with launch configuration
   - Check Streamlit logs in terminal

## Deployment Preparation

Before deploying to Streamlit Cloud:

1. **Test Locally**
   - Ensure everything works in VS Code
   - Test all navigation and features

2. **Check Files**
   - Verify all required files are present
   - Ensure `requirements.txt` is up to date

3. **Git Repository**
   - Initialize git if needed: `git init`
   - Add files: `git add .`
   - Commit: `git commit -m "Initial portfolio commit"`
   - Push to GitHub for Streamlit Cloud deployment

## Quick Commands Reference

```bash
# Run portfolio (default port 8501)
streamlit run app.py

# Run with specific port
streamlit run app.py --server.port 5000

# Run with external access
streamlit run app.py --server.address 0.0.0.0

# Install dependencies
pip install -r requirements_deployment.txt

# Check Streamlit version
streamlit version

# Using the run script
python run_portfolio.py
python run_portfolio.py 5000  # Custom port
```