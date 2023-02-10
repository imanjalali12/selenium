from web_drivers.chrome_driver.chrome import ChromeDriver


driver = ChromeDriver("normal").get_driver()
driver.set_page_load_timeout(30)

