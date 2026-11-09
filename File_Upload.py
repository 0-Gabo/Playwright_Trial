from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    page.wait_for_timeout(3000)

    #No file uploaded
    page.locator('id=file-submit').click(click_count=1)
    page.wait_for_timeout(3000)
    page.get_by_text('Back to the File Uploader', exact=True).click()
    page.wait_for_timeout(3000)

    #Upload a file using button
    page.locator('id=file-upload').set_input_files("D:\Desktop\Gabriel\Work\SelfStudy\Playwright\Test.txt")
    page.wait_for_timeout(3000)
    page.locator('id=file-submit').click(click_count=1)
    page.wait_for_timeout(3000)

    #upload a file using drag and drop
    page.go_back()
    page.wait_for_timeout(3000)
    with page.expect_file_chooser() as fc_info:
        page.locator('id=drag-drop-upload').click()
    file_chooser = fc_info.value
    file_chooser.set_files("D:\Desktop\Gabriel\Work\SelfStudy\Playwright\Test.txt")
    #page.on("filechooser", lambda file_chooser: file_chooser.set_files("D:\Desktop\Gabriel\Work\SelfStudy\Playwright\Test.txt"))
    
    #page.locator('#drag-drop-upload').set_input_files("D:\Desktop\Gabriel\Work\SelfStudy\Playwright\Test.txt")
    page.wait_for_timeout(3000)