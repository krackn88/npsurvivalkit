#!/usr/bin/env node
/**
 * Database Setup Script for NP Survival Toolkit
 * This script will create all necessary tables in your Neon database
 */

const { Client } = require('pg');

// Your Neon database connection string
const connectionString = 'postgresql://neondb_owner:npg_8Mfk3Webygdh@ep-mute-grass-ae40mll3-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require';

const client = new Client({
    connectionString: connectionString
});

async function setupDatabase() {
    try {
        console.log('🔗 Connecting to Neon database...');
        await client.connect();
        console.log('✅ Connected successfully!');

        // SQL schema from database_schema.sql
        const schemaSQL = `
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
        `;

        console.log('📊 Creating database tables...');
        await client.query(schemaSQL);
        console.log('✅ All tables created successfully!');

        // Verify tables were created
        console.log('🔍 Verifying tables...');
        const result = await client.query(`
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        `);

        console.log('📋 Created tables:');
        result.rows.forEach(row => {
            console.log(`   ✅ ${row.table_name}`);
        });

        // Test insert some sample data
        console.log('🧪 Testing with sample data...');
        await client.query(`
            INSERT INTO email_subscribers (email, source) 
            VALUES ('test@example.com', 'setup_test')
            ON CONFLICT (email) DO NOTHING;
        `);

        await client.query(`
            INSERT INTO downloads (action, user_agent) 
            VALUES ('test_download', 'setup_test');
        `);

        console.log('✅ Sample data inserted successfully!');
        console.log('🎉 Database setup complete!');
        console.log('');
        console.log('📊 Your NP Survival Toolkit database is ready with:');
        console.log('   • Email subscriber tracking');
        console.log('   • Download analytics');
        console.log('   • Affiliate click tracking');
        console.log('   • Social media tracking');
        console.log('   • Performance indexes');
        console.log('');
        console.log('🚀 Your Netlify site can now start collecting data!');

    } catch (error) {
        console.error('❌ Database setup failed:', error.message);
        process.exit(1);
    } finally {
        await client.end();
        console.log('🔌 Database connection closed.');
    }
}

// Run the setup
setupDatabase();

