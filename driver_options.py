from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless=new')
options.page_load_strategy = 'none'

chromeDriver = ChromeDriverManager().install()
service = ChromeService(chromeDriver)
