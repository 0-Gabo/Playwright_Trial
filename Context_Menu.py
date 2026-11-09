from playwright.sync_api import sync_playwright, expect, Page



def handle_dialog(dialog):

    assert dialog.message == "You selected a contex t menu"
    page.wait_for_timeout(3000)
    dialog.accept()
    print("Dialog message: ", dialog.message)
    
    #if dialog.message == "You selected a context menu":
    #    page.wait_for_timeout(3000)
    #    print("Dialog message: ", dialog.message)
    #    dialog.accept()
        
    #else:
    #    dialog.dismiss()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    page = browser.new_page(no_viewport=True)
    page.goto("https://the-internet.herokuapp.com/context_menu")
    page.once("dialog", handle_dialog)
    #dialog = dialog_info.value
    #assert dialog.message == "You selected a context menu"

    page.locator("id=hot-spot").click(button="right")
    page.wait_for_timeout(3000)