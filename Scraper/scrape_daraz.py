import asyncio
from playwright.async_api import async_playwright
import pandas as pd

async def scrape_mudita_laptops():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
 
        await page.goto("https://mudita.com.np/laptops-nepal.html", timeout=60000)
        products = await page.query_selector_all('.product-item')

        data = []
        for product in products:
            #Extract data title, price, and link
            title = await product.query_selector('.product-item-name')
            price = await product.query_selector('.price')
            link = await product.query_selector('a') 
            
            #get text and link
            title_text = await title.inner_text() if title else 'N/A'
            price_text = await price.inner_text() if price else 'N/A'
            link_href = await link.get_attribute('href') if link else 'N/A'

            # Appending data in list
            data.append({
                'Title': title_text.strip().replace('"', ''),
                'Price': price_text.strip().replace("रू", "").replace(",", "").strip(),
                'Link': link_href.strip()
            })

        next_button = await page.query_selector('mst-scroll__button _next')
        if next_button:
         await next_button.click()
         await page.wait_for_load_state('networkidle')  # Wait for load
         print("✅ Moving to the next page...")
        else:
         print("✅ No more pages to scrape.")
         

        await browser.close()

        # Save to csv
        df = pd.DataFrame(data)
        df.to_csv('mudita_laptops.csv', index=False)
        print("Data saved to mudita_laptops.csv")

# Run the scraper
asyncio.run(scrape_mudita_laptops())
