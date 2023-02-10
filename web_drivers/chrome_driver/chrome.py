import undetected_chromedriver as uc
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.config_loader import read_yaml



class ChromeDriver:

    def __init__(self, strategy):
        self.driver = None
        self.capabilities = None
        self.configs = read_yaml('config.yml')
        self.options = self.configs.get('web_drivers').get('chrome').get('options')
        self.driver_options = uc.ChromeOptions()
        self.strategy = strategy
        self.proxy = None
        self.prepare_driver(proxy=self.proxy, strategy=self.strategy)

    def set_options(self, proxy, strategy):
        for option in self.options:
            self.driver_options.add_argument(option)
            self.driver_options.page_load_strategy = strategy
            self.capabilities = DesiredCapabilities.CHROME.copy()
            self.capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        if proxy:
            self.driver_options.add_argument(f"--proxy-server={proxy}")

    def set_driver(self):
        self.driver = uc.Chrome(options=self.driver_options, desired_capabilities=self.capabilities)

    def prepare_driver(self, proxy, strategy):
        self.set_options(proxy, strategy)
        self.set_driver()

    def get_driver(self):
        return self.driver


