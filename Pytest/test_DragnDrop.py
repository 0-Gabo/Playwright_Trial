from playwright.sync_api import sync_playwright, Page, expect





def test_DragnDrop(page:Page):
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    column_a = page.locator("id=column-a")
    column_b = page.locator("id=column-b")
    expect(column_a).to_have_attribute(name='draggable')
    expect(column_b).to_have_attribute(name='draggable')
    page.wait_for_timeout(3000)
    column_a.drag_to(column_b)
    page.wait_for_timeout(3000)
    column_b.drag_to(column_a)
    page.wait_for_timeout(3000)