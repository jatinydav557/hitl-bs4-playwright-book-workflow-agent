import os
from playwright.sync_api import sync_playwright

def take_screenshot(state):
    url = state['url']
    os.makedirs("screenshots", exist_ok=True)

    # Simple filename from URL
    filename = url.replace('://', '_').replace('/', '_').replace('.', '_') + ".png"
    path = os.path.join("screenshots", filename)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=30000)
        page.screenshot(path=path, full_page=True)
        browser.close()

    return {**state, "screenshot_path": path}
