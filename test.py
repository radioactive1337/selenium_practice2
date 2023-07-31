import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@pytest.mark.all
class Test:
    def test_SimpleFormDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')
        driver.find_element(By.ID, 'user-message').send_keys('qwe')
        driver.find_element(By.ID,'showInput').click()
        assert driver.find_element(By.ID,'message').text == 'qwe'

        inp1 = 100
        inp2 = 200
        driver.find_element(By.ID,'sum1').send_keys(inp1)
        driver.find_element(By.ID,'sum2').send_keys(inp2)
        ActionChains(driver).scroll_by_amount(0,100).perform()
        driver.find_element(By.XPATH,'//*[@id="gettotal"]/button').click()
        assert driver.find_element(By.ID,'addmessage').text == str(inp1+inp2)

    @pytest.mark.latest
    def test_InputFormSubmit(self):
        driver.get('https://www.lambdatest.com/selenium-playground/input-form-demo')
        driver.find_element(By.ID,'name').send_keys('python')
        driver.find_element(By.ID,'inputEmail4').send_keys('golefi9207@lukaat.com')
        driver.find_element(By.ID,'inputPassword4').send_keys('pass')
        driver.find_element(By.ID,'company').send_keys('company51')
        driver.find_element(By.ID,'websitename').send_keys('https://example.com')
        driver.find_element(By.ID,'seleniumform').click()
        driver.find_element(By.XPATH,'//*[@id="seleniumform"]/div[3]/div[1]/select/option[15]').click()
        driver.find_element(By.ID,'inputCity').send_keys('sydney')
        driver.find_element(By.ID,'inputAddress1').send_keys('address1')
        driver.find_element(By.ID,'inputAddress2').send_keys('address2')
        driver.find_element(By.ID,'inputState').send_keys('state')
        driver.find_element(By.ID,'inputZip').send_keys('1337')
        driver.find_element(By.XPATH,'//*[@id="seleniumform"]/div[6]/button').click()

