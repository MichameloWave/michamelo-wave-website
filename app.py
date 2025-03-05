from flask import Flask, Response
import datetime

app = Flask(__name__)

@app.route('/sitemap.xml')
def sitemap():
    # List of pages you want to include in your sitemap
    pages = [
        {'loc': 'https://www.michamelowave.com/', 'lastmod': datetime.date(2025, 3, 5)},
        # Add other pages here
        {'loc': 'https://www.michamelowave.com/about', 'lastmod': datetime.date(2025, 3, 5)},
        {'loc': 'https://www.michamelowave.com/music', 'lastmod': datetime.date(2025, 3, 5)},
        {'loc': 'https://www.michamelowave.com/contact', 'lastmod': datetime.date(2025, 3, 5)},
    ]
    
    # Start the XML document
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    
    # Add each page entry to the sitemap
    for page in pages:
        sitemap_xml += f'''
        <url>
            <loc>{page['loc']}</loc>
            <lastmod>{page['lastmod']}</lastmod>
            <changefreq>daily</changefreq>
            <priority>1.0</priority>
        </url>
        '''
    
    # Close the XML document
    sitemap_xml += '</urlset>'
    
    # Return the sitemap XML as a response
    return Response(sitemap_xml, content_type='application/xml')

# Ensure the app runs only when executed directly, not on imports
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # For production deployment, use appropriate host/port
