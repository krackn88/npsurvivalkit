-- Database schema for NP Survival Toolkit
-- Run this in your Neon database to create the necessary tables

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