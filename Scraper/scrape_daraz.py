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
    
async def scrape_mudita_laptops_details():
        all_laptops = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            #set page
            for link in links:
                Info={}
                await page.goto(link['Link'], timeout=60000)
                print(f"Scraping {link['Link']}")
                print("Page loaded")

                #Extracting laptop info from table
                table = await page.query_selector("table:nth-of-type(1)")
                rows = await table.query_selector_all("tr")
                if table is None:
                    print("Table not found")
                    continue
                else:
                    
                 for row in rows:
                     cells = await row.query_selector_all("td")
                        #select brandname and series
                     if len(cells) == 2:
                         key = await cells[0].inner_text()
                         value = await cells[1].inner_text()
                         # add info in dict
                         Info[key] = value

                    # Extracting laptop specs from table
                table = await page.query_selector("table:nth-of-type(2)")
                if table is None:
                    print("Table not found")
                    continue
                else:
                    rows = await table.query_selector_all("tr")
                    keys_to_extract = [
                    "RAM / Memory", "Storage", "Graphics Card", "Display",
                    "Keyboard", "Weight / Dimension (HxWxD)", "Battery", "Warranty","CPU"]
                    for row in rows:
                     columns = await row.query_selector_all("td")
                     if len(columns) == 2:
                        key = (await columns[0].inner_text()).strip()
                        value = (await columns[1].inner_text()).strip()
                     if key in keys_to_extract:
                        Info[key] = value
                #Extracting laptop price
                    price = await page.query_selector(".price")
                    price = await price.inner_text() if price else 'N/A'
                    Info['Price'] = price 
                    all_laptops.append(Info)

                        
            print("Laptop details extracted successfully")
        #save to csv
        df = pd.DataFrame(all_laptops)
        df.reindex(columns=['Link', 'Brand Name', 'Series', 'CPU', 'RAM / Memory', 'Storage', 'Graphics Card',
                        'Display', 'Keyboard', 'Weight / Dimension (HxWxD)', 'Battery', 'Warranty', 'Price'])
        df.to_csv('../Data/Raw/mudita_laptops_details.csv', index=False)
        print("Data saved to mudita_laptops_details.csv")
        await browser.close()

asyncio.run(scrape_mudita_laptops())
asyncio.run(scrape_mudita_laptops_details())
   

