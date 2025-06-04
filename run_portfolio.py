#!/usr/bin/env python3
"""
Streamlit Portfolio Runner
Easy way to run the portfolio application
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import PIL
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_deployment.txt"])
        return True

def run_portfolio(port=8501):
    """Run the Streamlit portfolio application"""
    if not os.path.exists("app.py"):
        print("✗ app.py not found in current directory")
        return False
    
    print(f"🚀 Starting portfolio on port {port}")
    print(f"📱 Open your browser to: http://localhost:{port}")
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", str(port),
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 Portfolio application stopped")
    except Exception as e:
        print(f"✗ Error running portfolio: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("🎯 Festus Matsitsa Bombo - Data Scientist Portfolio")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Get port from command line or use default
    port = 8501
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number, using default 8501")
    
    # Run the portfolio
    run_portfolio(port)