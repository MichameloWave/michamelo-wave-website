from flask import Flask, Response
import datetime

app = Flask(__name__)

@app.route('/sitemap.xml')
def sitemap():
    pages = [
        {'loc': 'https://www.michamelowave.com/', 'lastmod': datetime.date(2025, 3, 5)},
        # Add other pages here
    ]
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    for page in pages:
        sitemap_xml += f'''
        <url>
            <loc>{page['loc']}</loc>
            <lastmod>{page['lastmod']}</lastmod>
            <changefreq>daily</changefreq>
            <priority>1.0</priority>
        </url>
        '''
    sitemap_xml += '</urlset>'
    return Response(sitemap_xml, content_type='application/xml')

if __name__ == '__main__':
    app.run()
