from playwright.sync_api import sync_playwright, Page,expect



def test_default_checkbox(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox1 = page.locator("//input[1]")
    checkbox2 = page.locator("//input[2]")

    expect(checkbox1).not_to_be_checked()
    expect(checkbox2).to_be_checked()
    page.wait_for_timeout(3000)
    checkbox1.check()
    checkbox2.uncheck()
    expect(checkbox1).to_be_checked()
    expect(checkbox2).not_to_be_checked()
    page.wait_for_timeout(3000)


def test_all_checkbox(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox1 = page.locator("//input[1]")
    checkbox2 = page.locator("//input[2]")
    page.wait_for_timeout(3000)
    checkbox2.uncheck()

    expect(checkbox1).not_to_be_checked()
    expect(checkbox2).not_to_be_checked()

    page.wait_for_timeout(3000)
    checkbox1.check()
    checkbox2.check()

    expect(checkbox1).to_be_checked()
    expect(checkbox2).to_be_checked()
    page.wait_for_timeout(3000)