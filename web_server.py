#!/usr/bin/env python3
"""
NP Survival Toolkit Web Server
Simple Flask app to host the PDF and track downloads
"""

from flask import Flask, send_file, render_template_string, request, redirect, url_for
import os
from datetime import datetime
import json

app = Flask(__name__)

# Track downloads
download_stats = {
    'total_downloads': 0,
    'downloads_by_date': {},
    'referrers': {}
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NP Survival Toolkit - Free Download</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            margin-top: 50px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo {
            width: 80px;
            height: 80px;
            background: #2EC4B6;
            border-radius: 50%;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: white;
            font-weight: bold;
        }
        h1 {
            color: #0F1A2B;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #666;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .description {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #2EC4B6;
        }
        .download-btn {
            background: linear-gradient(45deg, #2EC4B6, #6C5CE7);
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 25px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin: 20px 0;
            transition: transform 0.3s ease;
        }
        .download-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .feature {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .feature-icon {
            font-size: 30px;
            margin-bottom: 10px;
        }
        .social-links {
            text-align: center;
            margin-top: 30px;
        }
        .social-links a {
            color: #2EC4B6;
            text-decoration: none;
            margin: 0 10px;
            font-weight: bold;
        }
        .disclaimer {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
            font-size: 14px;
            color: #856404;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">🩺</div>
            <h1>NP Survival Toolkit</h1>
            <p class="subtitle">The Complete Guide to Thriving in Nurse Practitioner School</p>
        </div>
        
        <div class="description">
            <p><strong>Based on real NP school experience</strong> - This comprehensive toolkit contains everything you need to succeed in NP school, from essential textbooks and study tools to clinical supplies and productivity apps.</p>
            
            <p>Created by someone who's been through the NP journey, this toolkit includes:</p>
            <ul>
                <li>📚 Essential textbooks with direct Amazon links</li>
                <li>🧠 Study tools and exam prep resources</li>
                <li>👩‍⚕️ Clinical supplies and equipment</li>
                <li>💡 Proven study strategies and tips</li>
                <li>📱 Digital resources and apps</li>
            </ul>
        </div>
        
        <div style="text-align: center;">
            <a href="/download" class="download-btn">📥 Download Free Toolkit</a>
        </div>
        
        <div class="features">
            <div class="feature">
                <div class="feature-icon">📖</div>
                <h3>Essential Textbooks</h3>
                <p>Curated list of must-have NP textbooks with direct purchase links</p>
            </div>
            <div class="feature">
                <div class="feature-icon">🎯</div>
                <h3>Study Tools</h3>
                <p>UWorld, Picmonic, Quizlet and other proven study resources</p>
            </div>
            <div class="feature">
                <div class="feature-icon">🩺</div>
                <h3>Clinical Supplies</h3>
                <p>Professional equipment and supplies for clinical rotations</p>
            </div>
            <div class="feature">
                <div class="feature-icon">💡</div>
                <h3>Study Strategies</h3>
                <p>Proven methods for time management and exam preparation</p>
            </div>
        </div>
        
        <div class="social-links">
            <p>Follow us for more NP school tips:</p>
            <a href="https://tiktok.com/@npsurvivalkit" target="_blank">TikTok</a>
            <a href="https://instagram.com/npsurvivalkit" target="_blank">Instagram</a>
        </div>
        
        <div class="disclaimer">
            <strong>Affiliate Disclosure:</strong> This toolkit contains affiliate links. When you purchase through these links, we may earn a small commission at no extra cost to you. This helps us continue providing valuable resources to NP students.
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """Main landing page"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/download')
def download_pdf():
    """Download the PDF and track statistics"""
    # Track download
    download_stats['total_downloads'] += 1
    
    # Track by date
    today = datetime.now().strftime('%Y-%m-%d')
    if today not in download_stats['downloads_by_date']:
        download_stats['downloads_by_date'][today] = 0
    download_stats['downloads_by_date'][today] += 1
    
    # Track referrer
    referrer = request.headers.get('Referer', 'Direct')
    if referrer not in download_stats['referrers']:
        download_stats['referrers'][referrer] = 0
    download_stats['referrers'][referrer] += 1
    
    # Save stats
    with open('download_stats.json', 'w') as f:
        json.dump(download_stats, f, indent=2)
    
    # Serve the PDF
    pdf_path = 'NP_Survival_Toolkit_Professional.pdf'
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True, download_name='NP_Survival_Toolkit.pdf')
    else:
        return "PDF not found. Please run create_pdf.py first.", 404

@app.route('/stats')
def stats():
    """View download statistics (for admin use)"""
    return f"""
    <h1>Download Statistics</h1>
    <p><strong>Total Downloads:</strong> {download_stats['total_downloads']}</p>
    <h2>Downloads by Date:</h2>
    <pre>{json.dumps(download_stats['downloads_by_date'], indent=2)}</pre>
    <h2>Top Referrers:</h2>
    <pre>{json.dumps(download_stats['referrers'], indent=2)}</pre>
    """

if __name__ == '__main__':
    print("🚀 Starting NP Survival Toolkit Web Server...")
    print("📱 Access your toolkit at: http://localhost:5000")
    print("📊 View stats at: http://localhost:5000/stats")
    app.run(debug=True, host='0.0.0.0', port=5000)
