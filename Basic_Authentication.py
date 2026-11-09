from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    page = browser.new_page(no_viewport=True)
    #page.goto("https://the-internet.herokuapp.com/basic_auth", wait_until="load")
    #page.wait_for_timeout(3000)
    #dialog.close()
    #page.once("dialog", lambda dialog: dialog.accept())

    page.get_by_role("button", name="Prompt Popup").click()
    context = browser.new_context(http_credentials={"username": "admin", "password": "admin"})
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth", wait_until="load")
