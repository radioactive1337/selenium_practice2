import time

import pytest
from numpy.random import random
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@pytest.mark.all
class Test:
    def test_SimpleFormDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')
        driver.find_element(By.ID, 'user-message').send_keys('qwe')
        driver.find_element(By.ID, 'showInput').click()
        assert driver.find_element(By.ID, 'message').text == 'qwe'

        inp1 = 100
        inp2 = 200
        driver.find_element(By.ID, 'sum1').send_keys(inp1)
        driver.find_element(By.ID, 'sum2').send_keys(inp2)
        ActionChains(driver).scroll_by_amount(0, 100).perform()
        driver.find_element(By.XPATH, '//*[@id="gettotal"]/button').click()
        assert driver.find_element(By.ID, 'addmessage').text == str(inp1 + inp2)

    def test_InputFormSubmit(self):
        driver.get('https://www.lambdatest.com/selenium-playground/input-form-demo')
        driver.find_element(By.ID, 'name').send_keys('python')
        driver.find_element(By.ID, 'inputEmail4').send_keys('golefi9207@lukaat.com')
        driver.find_element(By.ID, 'inputPassword4').send_keys('pass')
        driver.find_element(By.ID, 'company').send_keys('company51')
        driver.find_element(By.ID, 'websitename').send_keys('https://example.com')
        driver.find_element(By.ID, 'seleniumform').click()
        driver.find_element(By.XPATH, '//*[@id="seleniumform"]/div[3]/div[1]/select/option[15]').click()
        driver.find_element(By.ID, 'inputCity').send_keys('sydney')
        driver.find_element(By.ID, 'inputAddress1').send_keys('address1')
        driver.find_element(By.ID, 'inputAddress2').send_keys('address2')
        driver.find_element(By.ID, 'inputState').send_keys('state')
        driver.find_element(By.ID, 'inputZip').send_keys('1337')
        driver.find_element(By.XPATH, '//*[@id="seleniumform"]/div[6]/button').click()

    def test_UploadFileDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/upload-file-demo')
        driver.find_element(By.ID, 'file').send_keys('C:\\Users\\1chud\\Downloads\\ChatGPTbot.png')

    @pytest.mark.latest
    def test_SliderDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo')
        input_ids = ['range', 'rangePrimary', 'rangeSuccess', 'rangeInfo', 'rangeWarning', 'rangeDanger', 'rangeWarning',
               'rangeDanger']
        output_val = []
        for id in input_ids:
            output_val.append(driver.find_element(By.ID, f'{id}').text)
        for i in range(1, 9):
            for j in range(5):
                driver.find_element(By.XPATH, f'//*[@id="slider{i}"]/div/input').send_keys(Keys.RIGHT)
        for idx, id in enumerate(input_ids):
            assert int(driver.find_element(By.ID, f'{id}').text) == int(output_val[idx]) + 5
        time.sleep(2)
