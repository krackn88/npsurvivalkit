#!/usr/bin/env python3
"""
NP Survival Toolkit Setup Script
Installs dependencies and creates the PDF
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def create_pdf():
    """Generate the PDF from markdown"""
    print("📄 Creating NP Survival Toolkit PDF...")
    try:
        subprocess.check_call([sys.executable, "create_pdf.py"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating PDF: {e}")
        return False

def main():
    """Main setup function"""
    print("🩺 NP Survival Toolkit Setup")
    print("=" * 40)
    
    # Check if markdown file exists
    if not os.path.exists("NP_Survival_Toolkit.md"):
        print("❌ NP_Survival_Toolkit.md not found!")
        return False
    
    # Install requirements
    if not install_requirements():
        return False
    
    # Create PDF
    if not create_pdf():
        return False
    
    # Check if PDF was created
    if os.path.exists("NP_Survival_Toolkit.pdf"):
        print("\n🎉 Setup Complete!")
        print("📁 Files created:")
        print("   - NP_Survival_Toolkit.pdf (Your toolkit)")
        print("   - web_server.py (Web server for hosting)")
        print("\n🚀 Next steps:")
        print("1. Update affiliate links in NP_Survival_Toolkit.md")
        print("2. Run: python create_pdf.py (to regenerate PDF)")
        print("3. Run: python web_server.py (to host online)")
        print("4. Share the link in your TikTok bio!")
        return True
    else:
        print("❌ PDF creation failed!")
        return False

if __name__ == "__main__":
    main()
