import time
import os.path
import pytest
import random
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()


@pytest.mark.all
class Test:
    def test_SimpleFormDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/simple-form-demo')
        driver.find_element(by.ID, 'user-message').send_keys('qwe')
        driver.find_element(by.ID, 'showInput').click()

        assert driver.find_element(by.ID, 'message').text == 'qwe'

        inp1 = 100
        inp2 = 200
        driver.find_element(by.ID, 'sum1').send_keys(inp1)
        driver.find_element(by.ID, 'sum2').send_keys(inp2)
        ActionChains(driver).scroll_by_amount(0, 100).perform()
        driver.find_element(by.XPATH, '//*[@id="gettotal"]/button').click()

        assert driver.find_element(by.ID, 'addmessage').text == str(inp1 + inp2)

    def test_InputFormSubmit(self):
        driver.get('https://www.lambdatest.com/selenium-playground/input-form-demo')
        driver.find_element(by.ID, 'name').send_keys('python')
        driver.find_element(by.ID, 'inputEmail4').send_keys('golefi9207@lukaat.com')
        driver.find_element(by.ID, 'inputPassword4').send_keys('pass')
        driver.find_element(by.ID, 'company').send_keys('company51')
        driver.find_element(by.ID, 'websitename').send_keys('https://example.com')
        driver.find_element(by.ID, 'seleniumform').click()
        driver.find_element(by.XPATH, '//*[@id="seleniumform"]/div[3]/div[1]/select/option[15]').click()
        driver.find_element(by.ID, 'inputCity').send_keys('sydney')
        driver.find_element(by.ID, 'inputAddress1').send_keys('address1')
        driver.find_element(by.ID, 'inputAddress2').send_keys('address2')
        driver.find_element(by.ID, 'inputState').send_keys('state')
        driver.find_element(by.ID, 'inputZip').send_keys('1337')
        driver.find_element(by.XPATH, '//*[@id="seleniumform"]/div[6]/button').click()

    def test_UploadFileDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/upload-file-demo')
        driver.find_element(by.ID, 'file').send_keys('C:\\Users\\1chud\\Downloads\\ChatGPTbot.png')

    def test_SliderDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo')
        input_ids = ['range', 'rangePrimary', 'rangeSuccess', 'rangeInfo', 'rangeWarning', 'rangeDanger',
                     'rangeWarning',
                     'rangeDanger']
        output_val = []

        for id in input_ids:
            output_val.append(driver.find_element(by.ID, f'{id}').text)

        for i in range(1, 9):
            for j in range(5):
                driver.find_element(by.XPATH, f'//*[@id="slider{i}"]/div/input').send_keys(Keys.RIGHT)

        for idx, id in enumerate(input_ids):
            assert int(driver.find_element(by.ID, f'{id}').text) == int(output_val[idx]) + 5

    def test_BootstrapProgressBarDialogDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/bootstrap-progress-bar-dialog-demo')
        elems = driver.find_elements(by.XPATH, "//*[contains(text(),'Show dialog')]")
        rand_elem = random.choice(elems)
        rand_elem.click()
        WebDriverWait(driver, 10).until_not(
            ec.text_to_be_present_in_element_attribute((by.XPATH, '/html/body'), 'class', 'modal-open'))

        assert driver.find_element(by.XPATH,
                                   '//*[@id="__next"]/section[3]/div/div/div/h2').text == "waitingDialog.show('Hello Alert !!!');"

    def test_JQueryDatePickerDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/jquery-date-picker-demo')
        driver.find_element(by.ID, 'from').click()
        driver.find_element(by.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select').click()
        driver.find_element(by.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select/option[1]').click()
        driver.find_element(by.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[1]/a').click()
        time.sleep(1)
        driver.find_element(by.ID, 'to').click()
        driver.find_element(by.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select').click()
        driver.find_element(by.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select/option[12]').click()
        driver.find_element(by.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[6]/td[1]/a').click()

        assert driver.find_element(by.ID, 'from').get_attribute('value') == '01/01/2023'
        assert driver.find_element(by.ID, 'to').get_attribute('value') == '12/31/2023'

    def test_TablePaginationDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/table-pagination-demo')
        driver.find_element(by.ID, 'maxRows').click()
        driver.find_element(by.XPATH, '//*[@id="maxRows"]/option[1]').click()
        r11 = driver.find_element(by.XPATH, '//*[@id="table-id"]/tbody/tr[11]').text
        r22 = driver.find_element(by.XPATH, '//*[@id="table-id"]/tbody/tr[22]').text
        r33 = driver.find_element(by.XPATH, '//*[@id="table-id"]/tbody/tr[33]').text

        assert r11 == '11 Abraham Morgan a.morgan@randatmail.com 061-9140-93'
        assert r22 == '22 Heather Fowler h.fowler@randatmail.com 835-5062-15'
        assert r33 == '33 Rebecca Smith r.smith@randatmail.com 627-1702-52'

    def test_DataTableDownload(self):
        driver.get('https://www.lambdatest.com/selenium-playground/table-data-download-demo')
        driver.find_element(by.XPATH, '//*[@id="example_wrapper"]/div[1]/a[2]').click()
        driver.find_element(by.XPATH, '//*[@id="example_wrapper"]/div[1]/a[3]').click()
        driver.find_element(by.XPATH, '//*[@id="example_wrapper"]/div[1]/a[4]').click()
        os.path.exists('C:\\Users\\1chud\\Downloads\\Selenium Grid Online  Run Selenium Test On Cloud.pdf')
        os.path.exists('C:\\Users\\1chud\\Downloads\\Selenium Grid Online  Run Selenium Test On Cloud.csv')
        os.path.exists('C:\\Users\\1chud\\Downloads\\Selenium Grid Online  Run Selenium Test On Cloud.xlsx')

    def test_MouseHover(self):
        driver.get('https://www.lambdatest.com/selenium-playground/hover-demo')
        ActionChains(driver).move_to_element(driver.find_element(by.XPATH,
                                                                 '//*[@id="__next"]/section[3]/div/div/div/div/div/div/div/div[1]/div[1]')).perform()
        time.sleep(1)
        ActionChains(driver).move_to_element(driver.find_element(by.XPATH,
                                                                 '//*[@id="__next"]/section[3]/div/div/div/div/div/div/div/div[1]/div[2]')).perform()
        time.sleep(1)
        ActionChains(driver).move_to_element(driver.find_element(by.XPATH,
                                                                 '//*[@id="__next"]/section[3]/div/div/div/div/div/div/div/div[2]/div[1]')).perform()
        time.sleep(1)
        ActionChains(driver).move_to_element(driver.find_element(by.XPATH,
                                                                 '//*[@id="__next"]/section[3]/div/div/div/div/div/div/div/div[2]/div[2]')).perform()
        time.sleep(1)

        ActionChains(driver).move_to_element(driver.find_element(by.XPATH,
                                                                 '//*[@id="__next"]/section[3]/div/div/div/div/div/div/div/div[3]/img')).perform()
        assert driver.find_element(by.XPATH,
                                   '//*[@id="__next"]/section[3]/div/div/div/div/div/div/div/div[3]/p').is_displayed() == True
        time.sleep(1)
        # zoom

    def test_Redirection(self):
        driver.get('https://www.lambdatest.com/selenium-playground/redirection')
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/p/a').click()
        assert driver.current_url == 'https://www.lambdatest.com/selenium-playground/'

    def test_CheckboxDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/checkbox-demo')
        driver.find_element(by.ID, 'isAgeSelected').click()
        driver.find_element(by.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[2]/div[2]/div[1]/input').click()
        driver.find_element(by.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[2]/div[2]/div[2]/input').click()
        driver.find_element(by.XPATH, '//*[@id="box"]').click()

        assert driver.find_element(by.ID, 'txtAge').text == 'Checked'
        assert driver.find_element(by.XPATH, '//*[@id="ex1-check1"]').is_selected() == True
        assert driver.find_element(by.XPATH, '//*[@id="ex1-check2"]').is_selected() == True
        assert driver.find_element(by.XPATH, '//*[@id="ex1-check3"]').is_selected() == True

    def test_FormSubmitDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo')
        driver.find_element(by.ID, 'title').send_keys('nickname')
        driver.find_element(by.ID, 'description').send_keys('Hello world!')
        driver.find_element(by.ID, 'btn-submit').click()
        assert driver.find_element(by.ID, 'submit-control').text == 'Ajax Request is Processing!'

    def test_DownloadFileDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/download-file-demo')
        driver.find_element(by.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div/a/button').click()
        time.sleep(2)
        assert os.path.exists('C:\\Users\\1chud\\Downloads\\LambdaTest.pdf') == True

    def test_BootstrapAlertMessages(self):
        driver.get('https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo')
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div[1]/button[1]').click()
        assert ('Autocloseable success message. Hide in 5 seconds.' in driver.find_element(by.XPATH,
                                                                                           '//*[@id="__next"]/section[3]/div/div/div/div/div[2]/div[1]').text) == True
        WebDriverWait(driver, 10).until_not(
            ec.visibility_of_element_located((by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div[2]/div[1]')))

        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div[1]/button[2]').click()
        assert ('Normal success message. To close use the close button.' in driver.find_element(by.XPATH,
                                                                                                '//*[@id="__next"]/section[3]/div/div/div/div/div[2]/div[1]').text) == True
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div[2]/div[1]/a').click()

        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div[1]/button[3]').click()
        assert ('Autocloseable info message. Hide in 5 seconds.' in driver.find_element(by.XPATH,
                                                                                        '//*[@id="__next"]/section[3]/div/div/div/div/div[2]/div[1]').text) == True
        WebDriverWait(driver, 10).until_not(
            ec.visibility_of_element_located((by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div[2]/div[1]')))

        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div[1]/button[4]').click()
        assert ('Normal info message.To close use the close button.' in driver.find_element(by.XPATH,
                                                                                            '//*[@id="__next"]/section[3]/div/div/div/div/div[2]/div[1]').text) == True
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div[2]/div[1]/a').click()

    def test_JavascriptAlertBoxDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/javascript-alert-box-demo')
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div[1]/p/button').click()
        alert = Alert(driver)
        assert alert.text == 'Alert box!'
        alert.accept()

        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div[2]/div/p[1]/button').click()
        confirm = Alert(driver)
        assert confirm.text == 'Press a button!'
        confirm.accept()
        # prompt.dismiss()

        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div[3]/p[1]/button').click()
        prompt = Alert(driver)
        prompt.send_keys('Hello')
        prompt.accept()
        assert driver.find_element(by.ID, 'prompt-demo').text == "You have entered 'Hello' !"

    def test_BootstrapDualListDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/bootstrap-dual-list-box-demo')
        driver.find_elements(by.NAME, 'SearchDualList')[0].send_keys('cli')
        driver.find_elements(by.NAME, 'SearchDualList')[0].clear()
        driver.find_elements(by.NAME, 'SearchDualList')[0].send_keys(' ')
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div/div[1]/div/ul/li[1]').click()
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div/div[2]/button[2]').click()
        driver.find_elements(by.NAME, 'SearchDualList')[1].send_keys('yc ')
        driver.find_elements(by.NAME, 'SearchDualList')[1].clear()
        driver.find_elements(by.NAME, 'SearchDualList')[1].send_keys(' ')
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div/div[3]/div/ul/li[2]').click()
        driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div/div[2]/button[1]').click()
        time.sleep(1)
        left_col = driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div/div[1]/div/ul')
        left_col_rows = left_col.find_elements(by.XPATH, './li')
        right_col = driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div/div/div[3]/div/ul')
        right_col_rows = right_col.find_elements(by.XPATH, './li')
        assert len(right_col_rows) == 2
        assert len(left_col_rows) == 4

    @pytest.mark.latest
    def test_TableSearchfilter(self):
        driver.get('https://www.lambdatest.com/selenium-playground/table-search-filter-demo')
        driver.find_element(by.ID, 'task-table-filter').send_keys('completed')
        td1 = driver.find_elements(by.XPATH, "//table[@id='task-table']//tr//td[contains(text(), 'completed')]")
        assert len(td1) == 3

        driver.find_element(by.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[2]/div/div[1]/button').click()
        driver.find_element(by.XPATH,
                            '//*[@id="__next"]/div/section[2]/div/div/div/div[2]/div/div[2]/table/thead/tr/th[4]/input').send_keys(
            'John')
        td2 = driver.find_elements(by.XPATH,
                                   '//*[@id="__next"]/div/section[2]/div/div/div/div[2]/div/div[2]/table//tr//td[contains(text(), "John")]')
        assert len(td2) == 2
        driver.quit()
