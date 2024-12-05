from playwright.sync_api import sync_playwright

def scrape_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        url = "https://example.com"
        page.goto(url)

        title = page.title()
        print("Page Title:", title)
        links = page.eval_on_selector_all("a", "elements => elements.map(a => a.href)")
        print("Links:", links)

        browser.close()

scrape_page()
