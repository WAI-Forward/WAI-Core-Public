import os
import subprocess
import sys
import venv
from pathlib import Path

VENV_DIR = Path("venv")
PYTHON = VENV_DIR / "Scripts" / "python.exe" if os.name == "nt" else VENV_DIR / "bin" / "python"

def create_venv():
    if not VENV_DIR.exists():
        print("🔧 Creating virtual environment...")
        venv.create(VENV_DIR, with_pip=True)
    else:
        print("✅ Virtual environment already exists.")

def install_requirements():
    print("📦 Installing dependencies...")
    subprocess.check_call([str(PYTHON), "-m", "pip", "install", "-r", "requirements.txt"])

def run_app():
    print("🚀 Launching Flask app at http://localhost:5000")
    subprocess.call([str(PYTHON), "src/main.py"])

if __name__ == "__main__":
    create_venv()
    install_requirements()
    run_app()
