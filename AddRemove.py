from playwright.async_api import async_playwright, dialog
import asyncio, pytest





@pytest.mark.asyncio
async def main():
    async with async_playwright() as p: 
        browser = await p.chromium.launch(headless=False, args=['--start-maximized'])
        page = await browser.new_page(no_viewport=True)
        await page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
        await page.get_by_text('Add Element', exact=True).click(click_count=5)
        ButtonCount = await page.get_by_text("Delete", exact=True).count()
        print("Total number of buttons on the page: ", ButtonCount)  

        for i in range(ButtonCount+1):
            #await page.get_by_role("button",name="Delete", exact=True).nth(i).click()
            btnvisible = await page.get_by_text("Delete", exact=True).nth(i).is_visible()
            if btnvisible:
                print("Button is visible: ", i)
                await page.get_by_text("Delete", exact=True).nth(i).wait_for(state="visible")
                await page.locator(".added-manually").nth(i).click()
       
        #await page.get_by_text('Delete', exact=True).click(click_count=3)



asyncio.run(main())