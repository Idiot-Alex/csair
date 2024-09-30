from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  browser = p.chromium.launch(
    headless = False,
    slow_mo = 500
  )
  page = browser.new_page()
  page.goto("https://www.csair.com/cn/")
  page.wait_for_load_state()
  page.locator("input#fDepCity").focus()
  page.locator("input#fDepCity").press_sequentially("上海", delay=1000)
  page.locator("input#fArrCity").focus()
  page.locator("input#fArrCity").press_sequentially("重庆", delay=1000)
  page.wait_for_timeout(1000)
  page.locator("a.searchFlight").click()
  page.wait_for_timeout(20000)
  # browser.close()