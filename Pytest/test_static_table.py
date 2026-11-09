from playwright.sync_api import sync_playwright, expect, Page




def test_static_table(page: Page):
    page.goto("https://the-internet.herokuapp.com/tables")
    page.wait_for_timeout(2000)


    #Print All the headers of the table
    headers = page.locator("table[id='table1'] thead tr th ")
    all_header_text = headers.all_inner_texts()
    #all_header = headers.all()

    print("Header: ", all_header_text)
    expect(headers).to_have_count(6)
    expect(headers).to_have_text(["Last Name", "First Name", "Email", "Due", "Web Site", "Action"])


    rows = page.locator("table[id='table1' ] tbody tr")
    first_row = rows.nth(0).inner_text()
    all_row = rows.all_inner_texts()
    print("First Row: ", first_row)
    print("Rows: ", rows.all_inner_texts())


    for header in all_header_text:
        print(header)

    for row in all_row:
        #All_Rows = row.nth(0).locator('tr').nth(0).inner_text()
        print(row)


    all_row_data = rows.all()

    
    first = headers.locator('span').nth(0).inner_text()
    print(first)


    for row_data in all_row_data:
        Last_Name = row_data.locator('td').nth(0).inner_text()
        print(Last_Name)



    
    third = headers.locator('span').nth(3).inner_text()
    print(third)

    all_sum = 0.0
    for row_data in all_row_data:
        Due = row_data.locator('td').nth(3).inner_text()

        all_sum = all_sum + float(Due[1:])
        print(float(Due[1:]))
    
    print("Total Sum Due: ", all_sum)


def test_due(page:Page):
    page.goto("https://the-internet.herokuapp.com/tables")
    page.wait_for_timeout(2000)

    headers = page.locator("table[id='table1'] thead tr th")


    header_due = headers.locator('span').nth(3)
    header_due_conent = header_due.inner_text()
    expect(header_due).to_have_text("Due")

    rows = page.locator("table[id='table1'] tbody tr ")
    all_rows = rows.all()
    print("\n")
    print(header_due_conent)


    sum = 0.00

    row_test=['$50.00', '$51.00', '$100.00', '$50.00']
    
    for row in all_rows:
        due = row.locator('td').nth(3)
        due_content = due.inner_text()
        sum = sum + float(due_content[1:])
        if due_content == row_test:
            print(due_content)   
        #print(due)
    
        #print(due_content)
    print(f"Total Sum Due: ${sum}")
    assert sum == 251.00
    
    
      
  
    