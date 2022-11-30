import time
import math
from gettext import gettext

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    url = "http://suninjuly.github.io/explicit_wait2.html"
    driver.get(url)

    if WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '100')):
        book_btn = driver.find_element(By.XPATH, "//button[@id='book']").click()

    x = int(driver.find_element(By.XPATH, "//span[@id='input_value']").text)
    def func():
        return str(math.log(abs(12 * math.sin(int(x)))))

    answer_area = driver.find_element(By.XPATH, "//input[@id='answer']").send_keys(f"{func()}")
    submit_btn = driver.find_element(By.XPATH, "//button[@id='solve']").click()

finally:
    time.sleep(15)
    driver.quit()