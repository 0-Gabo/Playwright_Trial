from playwright.sync_api import sync_playwright, expect, Page
import re



def test_Dynamic_Table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    rows = page.locator("table[id='taskTable'] tbody tr").all()
    row_content= page.locator("table.table.table-striped tbody").all_inner_texts()
    
    print(row_content)


    Chrome_Cpu=""
    Chrome_Disk= ""
    Chrome_Memory=""
    Chrome_Network=""
    Firefox_Cpu=""
    Firefox_Disk= ""
    Firefox_Memory=""
    Firefox_Network=""
    for row in rows:
        Name = row.locator("td").nth(0).inner_text()
        print(Name)


        if Name == "Chrome":

            Chrome_Cpu = row.locator("td", has_text="%").inner_text()
            Chrome_Disk = row.locator("td", has_text="MB/s").inner_text()
            #Memory = row.locator("td", has_text=re.compile(r"MB$")).inner_text()
            Chrome_Memory = row.locator("td:text-matches('MB$', 'i')").inner_text()
            Chrome_Network = row.locator("td", has_text="Mbps").inner_text()
            print(Name ,Chrome_Cpu,Chrome_Disk,Chrome_Memory,Chrome_Network)
            break
        if Name == "Firefox":
            Firefox_Cpu = row.locator("td", has_text="%").inner_text()
            Firefox_Disk = row.locator("td", has_text="MB/s").inner_text()
            #Memory = row.locator("td", has_text=re.compile(r"MB$")).inner_text()
            Firefox_Memory = row.locator("td:text-matches('MB$', 'i')").inner_text()
            Firefox_Network = row.locator("td", has_text="Mbps").inner_text()
            print(Name ,Firefox_Cpu,Firefox_Disk,Firefox_Memory,Firefox_Network)
            

    expect(page.locator(".chrome-cpu")).to_contain_text(Chrome_Cpu)
    expect(page.locator(".firefox-memory")).to_contain_text(Firefox_Memory)
    expect(page.locator(".chrome-network")).to_contain_text(Chrome_Network)
    expect(page.locator(".firefox-disk")).to_contain_text(Firefox_Disk)