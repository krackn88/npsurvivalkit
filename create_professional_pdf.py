#!/usr/bin/env python3
"""
Professional NP Survival Toolkit PDF Generator
Creates a clean, professional PDF with proper formatting
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import re

def create_professional_pdf():
    """Create a professional PDF from the clean markdown content"""
    
    # Create PDF document
    doc = SimpleDocTemplate(
        "NP_Survival_Toolkit_Professional.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=HexColor('#2EC4B6'),
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=18,
        spaceAfter=20,
        textColor=HexColor('#0F1A2B'),
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'CustomSection',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=12,
        textColor=HexColor('#6C5CE7'),
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    link_style = ParagraphStyle(
        'CustomLink',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        textColor=HexColor('#2EC4B6'),
        leftIndent=20,
        fontName='Helvetica'
    )
    
    # Read clean markdown content
    with open('NP_Survival_Toolkit_Clean.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse content into elements
    elements = []
    
    # Split content into sections
    sections = content.split('\n---\n')
    
    for i, section in enumerate(sections):
        if i == 0:  # Title section
            lines = section.strip().split('\n')
            title = lines[0].replace('# ', '')
            subtitle = lines[1].replace('## ', '')
            
            elements.append(Paragraph(title, title_style))
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(subtitle, subtitle_style))
            elements.append(Spacer(1, 20))
            
            # Add the description
            if len(lines) > 2:
                desc = lines[2].replace('*', '').strip()
                elements.append(Paragraph(desc, body_style))
                elements.append(Spacer(1, 30))
        
        else:
            # Process other sections
            lines = section.strip().split('\n')
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Handle different line types
                if line.startswith('## '):
                    # Main section heading
                    heading = line.replace('## ', '')
                    elements.append(Spacer(1, 20))
                    elements.append(Paragraph(heading, subtitle_style))
                    elements.append(Spacer(1, 12))
                
                elif line.startswith('### '):
                    # Subsection heading
                    heading = line.replace('### ', '')
                    elements.append(Paragraph(heading, section_style))
                    elements.append(Spacer(1, 8))
                
                elif line.startswith('- **'):
                    # Bold item with description
                    item = line.replace('- **', '').replace('**', '')
                    elements.append(Paragraph(f"• {item}", body_style))
                
                elif line.startswith('  - *'):
                    # Affiliate link or description
                    desc = line.replace('  - *', '').replace('*', '')
                    if 'amazon.com' in desc.lower():
                        # Make Amazon links stand out
                        link_style.textColor = HexColor('#FF9900')
                    else:
                        link_style.textColor = HexColor('#2EC4B6')
                    elements.append(Paragraph(desc, link_style))
                
                elif line.startswith('- *'):
                    # Description line
                    desc = line.replace('- *', '').replace('*', '')
                    elements.append(Paragraph(desc, body_style))
                
                elif line.startswith('*'):
                    # Italic text
                    text = line.replace('*', '')
                    elements.append(Paragraph(text, body_style))
                
                elif line.startswith('**'):
                    # Bold text
                    text = line.replace('**', '')
                    elements.append(Paragraph(text, body_style))
                
                elif line.startswith('- [ ]'):
                    # Checklist item
                    item = line.replace('- [ ]', '☐')
                    elements.append(Paragraph(item, body_style))
                
                elif line.startswith('- [x]'):
                    # Checked checklist item
                    item = line.replace('- [x]', '☑')
                    elements.append(Paragraph(item, body_style))
                
                elif line.startswith('1. **'):
                    # Numbered list with bold
                    item = line.replace('1. **', '1. ').replace('**', '')
                    elements.append(Paragraph(item, body_style))
                
                elif line.startswith('1. '):
                    # Numbered list
                    elements.append(Paragraph(line, body_style))
                
                else:
                    # Regular paragraph
                    if line:
                        elements.append(Paragraph(line, body_style))
    
    # Build PDF
    doc.build(elements)
    print("✅ Professional NP Survival Toolkit PDF created successfully!")
    print("📁 File: NP_Survival_Toolkit_Professional.pdf")

if __name__ == "__main__":
    create_professional_pdf()
