from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  browser = p.chromium.launch(
    headless = False,
    slow_mo = 500
  )
  page = browser.new_page()
  page.goto("https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=NKG&c2=SYX&d1=2024-10-24&at=1&ct=0&it=0&b1=NKG&b2=SYX")
  page.wait_for_load_state()
  page.wait_for_timeout(1000)

  for _ in range(3):
    page.locator("input#single-formCity").focus()
    page.locator("input#single-formCity").fill("")
    page.locator("input#single-formCity").press_sequentially("上海", delay=1000)
    page.locator("input#single-toCity").focus()
    page.locator("input#single-toCity").fill("")
    page.locator("input#single-toCity").press_sequentially("重庆", delay=1000)
    page.wait_for_timeout(1000)
    page.locator("button#search-submit").click()
    page.wait_for_timeout(2000)
