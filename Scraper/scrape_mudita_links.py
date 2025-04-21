import asyncio
from playwright.async_api import async_playwright
import pandas as pd
links = []
async def scrape_mudita_laptops():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        #set page
        await page.goto("https://mudita.com.np/laptops-nepal.html", timeout=60000)

        while True:
            try:
                # Wait for the button
                await page.wait_for_selector('.action.primary.mst-scroll__button._next', timeout=3000)
                await page.click('.action.primary.mst-scroll__button._next') #Click button
                await page.wait_for_timeout(2000)
            except:
                print("No more button found.")
                break

        products = await page.query_selector_all('.product-item')

       
        for product in products:
            #Extract links
            link = await product.query_selector('a') 
            link_href = await link.get_attribute('href') if link else 'N/A'

            # Appending data in list
            links.append({
                'Link': link_href.strip()
            })

        next_button = await page.query_selector('.mst-scroll__button _next')
        print(next_button)
        await browser.close()
        print("Links extracted successfully")
        #save to csv
        df = pd.DataFrame(links)
        df.to_csv('../Data/Raw/mudita_laptops_links.csv', index=False)
        print("Data saved to mudita_laptops_links.csv")

asyncio.run(scrape_mudita_laptops())

   

