from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.wait_for_timeout(3000)
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000)
    page.locator('id=username').fill('tomsmith')
    page.wait_for_timeout(3000)
    page.locator('id=username').clear()
    page.wait_for_timeout(3000)
    page.locator('id=username').fill('tomsmith')
    page.wait_for_timeout(3000)
    page.locator('id=password').fill('SuperSecretPassword!')
    page.wait_for_timeout(3000)
    page.locator('id=password').clear()
    page.wait_for_timeout(3000)
    page.locator('id=password').fill('SuperSecretPassword!')
    page.wait_for_timeout(3000)
    #page.getByText('Login', { exact: true }).click()
    #page.getByRole('button', { name: 'Login' }).click()
    #page.getByRole('button').click()
    #page.getByRole("button", name="Login", exact=True).click()
    #page.locator('i:has-text("Login")').click(click_count=1)
    #page.get_by_role('button', name='Login').click()
    page.get_by_text('Login', exact=True).click()
    #page.getByText('Login', exact=True ).click()
    page.wait_for_timeout(3000)

    browser.close()
