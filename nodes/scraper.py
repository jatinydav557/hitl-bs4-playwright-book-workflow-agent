import requests
from bs4 import BeautifulSoup

def scrape_chapter(state):
    """Extract chapter text from URL"""
    url = state['url']
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove navigation and other non-content elements
        for element in soup.find_all(['nav', 'header', 'footer', 'aside', 'script', 'style']):
            element.decompose()
        
        # Try to find main content
        main_content = soup.find('div', class_='mw-parser-output')
        if main_content:
            text = main_content.get_text()
        else:
            text = soup.get_text()
        
        # Clean up text
        text = ' '.join(text.split())
        
        if not text or len(text) < 100:
            return {"url": url, "chapter_text": "No substantial text could be extracted from the URL."}
        
        return {"url": url, "chapter_text": text}
        
    except Exception as e:
        return {"url": url, "chapter_text": f"Failed to scrape URL: {str(e)}"}
