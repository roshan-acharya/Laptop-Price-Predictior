import asyncio
from playwright.async_api import async_playwright
import pandas as pd
async def scrape_mudita_laptops_details():
        
        all_laptops = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            #set page
            #Extracting links from csv file
            df = pd.read_csv('../Data/Raw/mudita_laptops_links.csv')
            df['Link'] = df['Link'].astype(str)
            print(df['Link'].dtypes)
            for link in df['Link']:

                Info={}
             
                await page.goto(link,wait_until='load', timeout=60000)
                print("Page loaded")

                #Extracting laptop info from table
                table = await page.query_selector("table:nth-of-type(1)")
               
                if table is None:
                    print("Table not found")
                    continue
                else:
                 rows = await table.query_selector_all("tr")  
                 for row in rows:
                     cells = await row.query_selector_all("td")
                     col_list=['Brand','Series']
                        #select brandname and series
                     if len(cells) == 2:
                         key = await cells[0].inner_text()
                         value = await cells[1].inner_text()
                         # add info in dict
                         for col in col_list:
                             if key == col:
                                 Info[key] = value
                                 break
                
               
                         

                # Extracting laptop specs from page title of h1 inside span class name base
                title = await page.query_selector("h1 span.base")
                title = await title.inner_text() if title else 'N/A'
                Info['Title'] = title
               
                #Extracting laptop price
                price = await page.query_selector(".price")
                price = await price.inner_text() if price else 'N/A'
                Info['Price'] = price 
                all_laptops.append(Info)

                        
            print("Laptop details extracted successfully")
        #save to csv
        df = pd.DataFrame(all_laptops)
        df.to_csv('../Data/Raw/mudita_laptops_details.csv', index=False)
        print("Data saved to mudita_laptops_details.csv")
        await browser.close()

asyncio.run(scrape_mudita_laptops_details())

