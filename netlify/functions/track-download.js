// netlify/functions/track-download.js
import { neon } from '@netlify/neon';

const sql = neon();

export async function handler(event, context) {
    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            body: JSON.stringify({ error: 'Method not allowed' })
        };
    }

    try {
        const data = JSON.parse(event.body);
        
        // Insert download tracking data
        await sql`
            INSERT INTO downloads (action, timestamp, user_agent, ip_address)
            VALUES (${data.action}, ${data.timestamp}, ${data.userAgent}, ${event.headers['x-forwarded-for'] || 'unknown'})
        `;
        
        return {
            statusCode: 200,
            headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            body: JSON.stringify({ success: true })
        };
    } catch (error) {
        console.error('Download tracking error:', error);
        return {
            statusCode: 500,
            body: JSON.stringify({ error: 'Internal server error' })
        };
    }
}