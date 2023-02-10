from web_drivers import driver
from utils.config_loader import read_yaml
from selenium.webdriver.common.by import By
from loguru import logger
from time import sleep

configs = read_yaml('config.yml')
url = configs.get('websites').get('calculater')

driver.get(url)
sleep(2)

### Button ###
Button1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/div[1]")
Button2 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/div[2]")
Button4 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/div[1]")
Button8 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]")

### Operators ###
multiplication = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[4]")
sum1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[4]/div[4]")
division = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[4]")
equal = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[5]/div[3]")


try:
    Button4.click()
    sleep(2)
    multiplication.click()
    sleep(2)
    Button2.click()
    sleep(2)
    equal.click()
    result = driver.find_element(By.XPATH, "/html/body/div/div/div[1]").text
    assert result == "8"
except Exception:
    logger.debug("test failed")


try:
    Button8.click()
    sleep(2)
    sum1.click()
    sleep(2)
    Button2.click()
    sleep(2)
    equal.click()
    result = driver.find_element(By.XPATH, "/html/body/div/div/div[1]").text
    assert result == "10"
except Exception:
    logger.debug("test failed")


try:
    Button8.click()
    sleep(2)
    division.click()
    sleep(2)
    Button2.click()
    sleep(2)
    equal.click()
    result = driver.find_element(By.XPATH, "/html/body/div/div/div[1]").text
    assert result == "4"
except Exception:
    logger.debug("test failed")


