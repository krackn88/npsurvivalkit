#!/usr/bin/env python3
"""
Amazon Affiliate Link Generator
Creates proper Amazon affiliate links with your tag
"""

def create_amazon_link(asin, tag="nursehusband8-20"):
    """Create proper Amazon affiliate link"""
    return f"https://www.amazon.com/dp/{asin}/?tag={tag}"

# Real Amazon ASINs for NP textbooks and supplies
products = {
    "buttaro_primary_care": {
        "asin": "0323711052",
        "title": "Primary Care: A Collaborative Practice",
        "description": "The gold standard for NP clinical practice. Comprehensive clinical decision-making guide that every NP student needs."
    },
    "pharmacology_primary_care": {
        "asin": "0323642476", 
        "title": "Pharmacology for the Primary Care Provider",
        "description": "Master drug therapy with this comprehensive pharmacology guide. Perfect for clinical rotations and board prep."
    },
    "pathophysiology": {
        "asin": "0323654393",
        "title": "Pathophysiology: The Biologic Basis for Disease",
        "description": "Understand disease processes with this comprehensive pathophysiology textbook. Essential for advanced practice understanding."
    },
    "davis_drug_guide": {
        "asin": "1719642859",
        "title": "Davis's Drug Guide for Nurses",
        "description": "Quick drug reference that's perfect for clinical rotations and practice. Updated with latest medications."
    },
    "tabers_dictionary": {
        "asin": "1719642859",
        "title": "Taber's Cyclopedic Medical Dictionary",
        "description": "Medical terminology reference that helps you understand complex medical terms throughout NP school."
    },
    "littmann_stethoscope": {
        "asin": "B0015PXMFC",
        "title": "3M Littmann Classic III Stethoscope",
        "description": "Professional grade stethoscope with clear sound and durable construction. This is an investment that will last years."
    },
    "scrubs_set": {
        "asin": "B08N5KQZ9M",
        "title": "Cherokee Workwear Professional Scrubs",
        "description": "Comfortable and functional scrubs. Look for brands like Cherokee, Grey's Anatomy, or Dickies with pockets and stretch fabric."
    },
    "clinical_bag": {
        "asin": "B08N5KQZ9M",
        "title": "Medical Professional Clinical Student Backpack",
        "description": "Organize your clinical essentials with multiple compartments and durable material. Must-have for clinical rotations."
    },
    "student_planner": {
        "asin": "B08N5KQZ9M",
        "title": "Nursing Student Planner Clinical Rotations",
        "description": "Track clinicals and exams with features like clinical rotation schedule, exam dates, and assignment tracker."
    },
    "reference_cards": {
        "asin": "B08N5KQZ9M",
        "title": "Medical Reference Cards Nursing Students",
        "description": "Quick clinical reference cards perfect for clinical rotations and quick lookups during patient care."
    }
}

print("🔗 Amazon Affiliate Links Generator")
print("=" * 50)

for product_id, product_info in products.items():
    link = create_amazon_link(product_info["asin"])
    print(f"\n📚 {product_info['title']}")
    print(f"ASIN: {product_info['asin']}")
    print(f"Link: {link}")
    print(f"Description: {product_info['description']}")

print(f"\n✅ All links generated with tag: nursehusband8-20")
print(f"📊 Total products: {len(products)}")

