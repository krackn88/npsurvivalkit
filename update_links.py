#!/usr/bin/env python3
"""
Affiliate Link Updater
Updates placeholder affiliate links with real ones
"""

import re

def update_affiliate_links():
    """Update affiliate links in the markdown file"""
    
    # Read the markdown file
    with open('NP_Survival_Toolkit.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔗 NP Survival Toolkit - Affiliate Link Updater")
    print("=" * 50)
    
    # Get user input for affiliate links
    amazon_tag = input("Enter your Amazon Associate tag (e.g., npsurvivalkit-20): ").strip()
    
    print("\n📱 Study Tools Affiliate Links:")
    picmonic_link = input("Picmonic affiliate link: ").strip()
    uworld_link = input("UWorld affiliate link: ").strip()
    quizlet_link = input("Quizlet affiliate link: ").strip()
    
    print("\n✍️ Productivity Tools:")
    grammarly_link = input("Grammarly affiliate link: ").strip()
    canva_link = input("Canva affiliate link: ").strip()
    notion_link = input("Notion affiliate link: ").strip()
    
    # Update Amazon links
    if amazon_tag:
        content = content.replace('[YOUR_AFFILIATE_TAG]', amazon_tag)
        print(f"✅ Updated Amazon links with tag: {amazon_tag}")
    
    # Update study tool links
    if picmonic_link:
        content = content.replace('[YOUR_PICMONIC_LINK]', picmonic_link)
        print("✅ Updated Picmonic link")
    
    if uworld_link:
        content = content.replace('[YOUR_UWORLD_LINK]', uworld_link)
        print("✅ Updated UWorld link")
    
    if quizlet_link:
        content = content.replace('[YOUR_QUIZLET_LINK]', quizlet_link)
        print("✅ Updated Quizlet link")
    
    # Update productivity tool links
    if grammarly_link:
        content = content.replace('[YOUR_GRAMMARLY_LINK]', grammarly_link)
        print("✅ Updated Grammarly link")
    
    if canva_link:
        content = content.replace('[YOUR_CANVA_LINK]', canva_link)
        print("✅ Updated Canva link")
    
    if notion_link:
        content = content.replace('[YOUR_NOTION_LINK]', notion_link)
        print("✅ Updated Notion link")
    
    # Write updated content back to file
    with open('NP_Survival_Toolkit.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n🎉 Affiliate links updated successfully!")
    print("📄 Run 'python create_pdf.py' to regenerate the PDF with new links")
    
    # Show summary
    print("\n📊 Link Summary:")
    print(f"Amazon Tag: {amazon_tag}")
    print(f"Picmonic: {'✅ Set' if picmonic_link else '❌ Not set'}")
    print(f"UWorld: {'✅ Set' if uworld_link else '❌ Not set'}")
    print(f"Quizlet: {'✅ Set' if quizlet_link else '❌ Not set'}")
    print(f"Grammarly: {'✅ Set' if grammarly_link else '❌ Not set'}")
    print(f"Canva: {'✅ Set' if canva_link else '❌ Not set'}")
    print(f"Notion: {'✅ Set' if notion_link else '❌ Not set'}")

if __name__ == "__main__":
    update_affiliate_links()
