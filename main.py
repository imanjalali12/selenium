from selenium.webdriver import Keys
from web_drivers import driver
from utils.config_loader import read_yaml
from selenium.webdriver.common.by import By
from loguru import logger
from time import sleep

configs = read_yaml('config.yml')
url = configs.get('websites').get('localhost')

driver.get(url)

emoji = driver.find_element(By.XPATH, "/html/body/div/div/div/div").get_attribute("class")
logger.info(emoji)

element = driver.find_element(By.ID, "root").find_element(By.TAG_NAME, "input")

for _ in range(200):
    element.send_keys(Keys.LEFT)

sleep(3)

emoji = driver.find_element(By.XPATH, "/html/body/div/div/div/div").get_attribute("class")
logger.info(emoji)

try:
    assert emoji == "somewhat-dissatisfied"
except Exception:
    logger.debug("test failed")

for _ in range(150):
    element.send_keys(Keys.RIGHT)

sleep(3)

emoji = driver.find_element(By.XPATH, "/html/body/div/div/div/div").get_attribute("class")
logger.info(emoji)

try:
    assert emoji == "somewhat-dissatisfied"
except Exception:
    logger.debug("test failed")

driver.quit()
