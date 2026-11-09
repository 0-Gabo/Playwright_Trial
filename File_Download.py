from playwright.sync_api import sync_playwright, expect, Page



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    page = browser.new_page(no_viewport=True)
    page.goto("https://the-internet.herokuapp.com/download")
    page.wait_for_timeout(5000)
    LinkCount = page.get_by_role("link").count()
    print("Total number of links on the page: ", LinkCount)
    cnt = 0
    for link in range(LinkCount):
        link_text = page.get_by_role("link").nth(link).text_content()
       # print("Link text: ", link_text)
        link_href = page.get_by_role("link").nth(link).get_attribute("href")
        #print("Link href: ", link_href)
        print("-----------------------------")
        if link_href.endswith(".txt") or link_href.endswith(".pdf") or link_href.endswith(".png") or link_href.endswith(".csv") or link_href.endswith(".jpg") or link_href.endswith(".html")\
            or link_href.endswith(".md") or link_href.endswith(".json") or link_href.endswith(".bin") or link_href.endswith(".xml")\
            or link_href.endswith(".xlsx") or link_href.endswith(".docx") or link_href.endswith("txt_1104-0853146qu-c001"):
            
            cnt+=1
            print("Link is downloadable: ", link_href)
            print(cnt)
            with page.expect_download() as download_info:
                page.get_by_role("link").nth(link).click()
            download = download_info.value
            print("Downloaded file name: ", download.suggested_filename)
            download.save_as("D:/Desktop/Gabriel/Work/SelfStudy/Playwright/Download_Test/" + download.suggested_filename)



