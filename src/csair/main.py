from playwright.sync_api import sync_playwright
import csv

def log_request(request):
  print(f">> 请求: {request.url}")
  with open('requests.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([request.method, request.url])

def log_response(response):
  print(f"<< 响应: {response.url}")
  with open('responses.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([response.status, response.url])

with sync_playwright() as p:
  browser = p.chromium.launch(
    headless = False,
    slow_mo = 500
  )
  page = browser.new_page()
  page.on("request", log_request)
  page.on("response", log_response)
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