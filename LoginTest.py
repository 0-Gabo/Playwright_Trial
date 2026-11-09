from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=['--start-maximized'])
        page = await browser.new_page(no_viewport=True)
        await page.goto("https://the-internet.herokuapp.com/login")
        #await page.wait_for_timeout(3000)
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        #await page.wait_for_timeout(2000)
        await page.locator('id=username').fill('tomsmith')
        await page.locator('id=password').fill('SuperSecretPassword!')
        #await page.getByText('Login', { exact: true }).click()
        #await page.getByRole('button', { name: 'Login' }).click()
        await page.get_by_text('Login', exact=True).click()
        await browser.close()

asyncio.run(main())
