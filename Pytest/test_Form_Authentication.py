import pytest
from playwright.sync_api import sync_playwright, expect, Playwright, Page



def test_form_authentication():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,args=['--start-maximized'])
        page = browser.new_page(no_viewport=True)
        page.goto("https://the-internet.herokuapp.com/login")
        expect(page).to_have_url("https://the-internet.herokuapp.com/login")
        expect(page).to_have_title("The Internet")
        expect(page.locator('h2')).to_have_text("Login Page")
        expect(page.locator('id=username')).to_be_visible()
        expect(page.locator('id=password')).to_be_visible()
        expect(page.locator('id=username')).to_be_enabled()
        expect(page.locator('id=password')).to_be_enabled()
       
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

def test_UrlValidation(page: Page):
    #page = playwright.chromium.launch(headless=False).new_page()
    
    page.goto("https://the-internet.herokuapp.com/login")
    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(page).to_have_title("The Internet")
    expect(page.locator('h2')).to_have_text("Login Page")
    expect(page.locator('id=username')).to_be_visible()
    expect(page.locator('id=password')).to_be_visible()
    expect(page.locator('id=username')).to_be_enabled()
    expect(page.locator('id=password')).to_be_enabled()
    page.wait_for_timeout(3000)
