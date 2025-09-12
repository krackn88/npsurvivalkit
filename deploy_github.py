#!/usr/bin/env python3
"""
GitHub Pages Deployment Script
Prepares files for free GitHub Pages hosting
"""

import os
import shutil
import subprocess

def setup_github_pages():
    """Set up files for GitHub Pages deployment"""
    
    print("🚀 Setting up NP Survival Toolkit for GitHub Pages...")
    
    # Create deployment directory
    deploy_dir = "github-pages"
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)
    
    # Copy necessary files
    files_to_copy = [
        "index.html",
        "NP_Survival_Toolkit_Professional.pdf"
    ]
    
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, deploy_dir)
            print(f"✅ Copied {file}")
        else:
            print(f"❌ {file} not found")
    
    # Create README for GitHub
    readme_content = """# NP Survival Toolkit

A comprehensive guide for Nurse Practitioner students with affiliate links.

## Live Site
Visit: https://[YOUR_USERNAME].github.io/npsurvivaltoolkit

## Files
- `index.html` - Landing page
- `NP_Survival_Toolkit.pdf` - Downloadable toolkit

## Setup Instructions
1. Create a new GitHub repository named `npsurvivaltoolkit`
2. Upload these files to the repository
3. Enable GitHub Pages in repository settings
4. Your site will be live at: https://[YOUR_USERNAME].github.io/npsurvivaltoolkit
"""
    
    with open(os.path.join(deploy_dir, "README.md"), "w") as f:
        f.write(readme_content)
    
    print(f"\n📁 Files ready in: {deploy_dir}/")
    print("\n🎯 Next Steps:")
    print("1. Create GitHub repository: npsurvivaltoolkit")
    print("2. Upload files from github-pages/ folder")
    print("3. Enable GitHub Pages in Settings > Pages")
    print("4. Your site will be live at: https://[YOUR_USERNAME].github.io/npsurvivaltoolkit")
    
    return True

if __name__ == "__main__":
    setup_github_pages()
