from selenium import webdriver
from selenium.webdriver.common.by import By
import time, pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get('https://app.jubelio.com/login')
    yield driver
    driver.quit()

# TEST FITUR LOGIN
def test_login(driver):
    driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
    driver.find_element(By.CLASS_NAME, "ladda-label").click()
    time.sleep(2)
    assert 'Jubelio' in driver.title

# TEST FITUR UPDATE STOCK
def test_stock(driver):
    driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
    driver.find_element(By.CLASS_NAME, "ladda-label").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/nav/div/div/ul/li[2]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div[3]/nav/div/div/ul/li[2]/ul/li[2]/a").click()
    time.sleep(2)
    driver.find_element(By.ID, "select-all-checkbox").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "html/body/div/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/span/div/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "html/body/div/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/span/div/ul/li/a").click()
    time.sleep(1)
    assert 'Permintaan upload Stok telah berhasil dikirim' in driver.find_element(By.XPATH, "html/body/div/div/div/li").text