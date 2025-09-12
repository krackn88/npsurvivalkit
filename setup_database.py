#!/usr/bin/env python3
"""
Database Setup Script for NP Survival Toolkit
This script will create all necessary tables in your Neon database using Python
"""

import psycopg2
import sys

# Your Neon database connection string
CONNECTION_STRING = 'postgresql://neondb_owner:npg_8Mfk3Webygdh@ep-mute-grass-ae40mll3-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require'

def setup_database():
    try:
        print('🔗 Connecting to Neon database...')
        conn = psycopg2.connect(CONNECTION_STRING)
        cur = conn.cursor()
        print('✅ Connected successfully!')

        # SQL schema
        schema_sql = """
-- Email subscribers table
CREATE TABLE IF NOT EXISTS email_subscribers (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    source VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Download tracking table
CREATE TABLE IF NOT EXISTS downloads (
    id SERIAL PRIMARY KEY,
    action VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_agent TEXT,
    ip_address VARCHAR(45),
    referrer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Affiliate click tracking table
CREATE TABLE IF NOT EXISTS affiliate_clicks (
    id SERIAL PRIMARY KEY,
    product VARCHAR(255) NOT NULL,
    link TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Social media click tracking table
CREATE TABLE IF NOT EXISTS social_clicks (
    id SERIAL PRIMARY KEY,
    platform VARCHAR(50) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Analytics summary table (for quick queries)
CREATE TABLE IF NOT EXISTS analytics_summary (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    downloads INTEGER DEFAULT 0,
    email_signups INTEGER DEFAULT 0,
    affiliate_clicks INTEGER DEFAULT 0,
    social_clicks INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(date)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_email_subscribers_email ON email_subscribers(email);
CREATE INDEX IF NOT EXISTS idx_email_subscribers_timestamp ON email_subscribers(timestamp);
CREATE INDEX IF NOT EXISTS idx_downloads_timestamp ON downloads(timestamp);
CREATE INDEX IF NOT EXISTS idx_affiliate_clicks_timestamp ON affiliate_clicks(timestamp);
CREATE INDEX IF NOT EXISTS idx_affiliate_clicks_product ON affiliate_clicks(product);
CREATE INDEX IF NOT EXISTS idx_social_clicks_timestamp ON social_clicks(timestamp);
CREATE INDEX IF NOT EXISTS idx_social_clicks_platform ON social_clicks(platform);
CREATE INDEX IF NOT EXISTS idx_analytics_summary_date ON analytics_summary(date);

-- Insert some sample data for testing
INSERT INTO analytics_summary (date, downloads, email_signups, affiliate_clicks, social_clicks) 
VALUES (CURRENT_DATE, 0, 0, 0, 0)
ON CONFLICT (date) DO NOTHING;
        """

        print('📊 Creating database tables...')
        cur.execute(schema_sql)
        conn.commit()
        print('✅ All tables created successfully!')

        # Verify tables were created
        print('🔍 Verifying tables...')
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)

        tables = cur.fetchall()
        print('📋 Created tables:')
        for table in tables:
            print(f'   ✅ {table[0]}')

        # Test insert some sample data
        print('🧪 Testing with sample data...')
        cur.execute("""
            INSERT INTO email_subscribers (email, source) 
            VALUES ('test@example.com', 'setup_test')
            ON CONFLICT (email) DO NOTHING;
        """)

        cur.execute("""
            INSERT INTO downloads (action, user_agent) 
            VALUES ('test_download', 'setup_test');
        """)

        conn.commit()
        print('✅ Sample data inserted successfully!')
        print('🎉 Database setup complete!')
        print('')
        print('📊 Your NP Survival Toolkit database is ready with:')
        print('   • Email subscriber tracking')
        print('   • Download analytics')
        print('   • Affiliate click tracking')
        print('   • Social media tracking')
        print('   • Performance indexes')
        print('')
        print('🚀 Your Netlify site can now start collecting data!')

    except psycopg2.Error as e:
        print(f'❌ Database setup failed: {e}')
        sys.exit(1)
    except Exception as e:
        print(f'❌ Unexpected error: {e}')
        sys.exit(1)
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()
        print('🔌 Database connection closed.')

if __name__ == '__main__':
    setup_database()

