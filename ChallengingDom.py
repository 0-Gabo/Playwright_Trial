from playwright.sync_api import sync_playwright




with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    page = browser.new_page(no_viewport=True)
    page.goto("https://the-internet.herokuapp.com/challenging_dom")
    button1 = page.locator("//a[@class='button']")
    button2 = page.locator("//a[@class='button alert']")
    button3 = page.locator("//a[@class='button success']")

    btn1txt = button1.text_content()
    btn2txt = button2.text_content()
    btn3txt = button3.text_content()

    print("Button 1 text: ", btn1txt)
    print("Button 2 text: ", btn2txt)
    print("Button 3 text: ", btn3txt)

    canvas_text = page.locator("#canvas").text_content()

    print("Canvas text: ", canvas_text)


    page.wait_for_timeout(3000)
        
    button1.click()

    btn1txt = button1.text_content()
    btn2txt = button2.text_content()
    btn3txt = button3.text_content()

    print("Button 1 text: ", btn1txt)
    print("Button 2 text: ", btn2txt)
    print("Button 3 text: ", btn3txt)

    canvas_text = page.locator("#canvas").text_content()

    print("Canvas text: ", canvas_text)

    page.wait_for_timeout(3000)

    button2.click()


    btn1txt = button1.text_content()
    btn2txt = button2.text_content()
    btn3txt = button3.text_content()

    print("Button 1 text: ", btn1txt)
    print("Button 2 text: ", btn2txt)
    print("Button 3 text: ", btn3txt)

    canvas_text = page.locator("#canvas").text_content()

    print("Canvas text: ", canvas_text)

    page.wait_for_timeout(3000)

    button3.click()



    btn1txt = button1.text_content()
    btn2txt = button2.text_content()
    btn3txt = button3.text_content()

    print("Button 1 text: ", btn1txt)
    print("Button 2 text: ", btn2txt)
    print("Button 3 text: ", btn3txt)


    canvas_text = page.locator("#canvas").text_content()

    print("Canvas text: ", canvas_text)

    page.wait_for_timeout(3000)

    



