#!/usr/bin/env python3
"""
NP Survival Toolkit PDF Generator
Converts markdown content to a professional PDF with affiliate links
"""

import markdown
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, blue
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import re

def create_pdf_from_markdown():
    """Create a professional PDF from the NP Survival Toolkit markdown"""
    
    # Create PDF document
    doc = SimpleDocTemplate(
        "NP_Survival_Toolkit.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18
    )
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=HexColor('#2EC4B6')  # Teal color
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=20,
        textColor=HexColor('#0F1A2B')  # Navy color
    )
    
    section_style = ParagraphStyle(
        'CustomSection',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=12,
        textColor=HexColor('#6C5CE7')  # Purple color
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )
    
    link_style = ParagraphStyle(
        'CustomLink',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        textColor=HexColor('#2EC4B6'),
        leftIndent=20
    )
    
    # Read markdown content
    with open('NP_Survival_Toolkit.md', 'r', encoding='utf-8') as f:
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
                elements.append(Spacer(1, 20))
        
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
                    elements.append(Paragraph(desc, link_style))
                
                elif line.startswith('- *'):
                    # Description line
                    desc = line.replace('- *', '').replace('*', '')
                    elements.append(Paragraph(desc, body_style))
                
                elif line.startswith('*'):
                    # Italic text
                    text = line.replace('*', '')
                    elements.append(Paragraph(text, body_style))
                
                elif line.startswith('### '):
                    # Subsection
                    heading = line.replace('### ', '')
                    elements.append(Paragraph(heading, section_style))
                
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
                
                elif line.startswith('**'):
                    # Bold text
                    text = line.replace('**', '')
                    elements.append(Paragraph(text, body_style))
                
                else:
                    # Regular paragraph
                    if line:
                        elements.append(Paragraph(line, body_style))
    
    # Add page breaks between major sections
    final_elements = []
    for i, element in enumerate(elements):
        final_elements.append(element)
        # Add page break after title section
        if i == 3:  # After title, subtitle, description
            final_elements.append(PageBreak())
    
    # Build PDF
    doc.build(final_elements)
    print("✅ NP Survival Toolkit PDF created successfully!")
    print("📁 File: NP_Survival_Toolkit.pdf")

if __name__ == "__main__":
    create_pdf_from_markdown()
