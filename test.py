import time
import os.path
import pytest
import random

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome()


# driver = webdriver.Chrome(options=chrome_options)


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
        driver.find_element(by.XPATH, '//button[contains(text(), "Get Sum")]').click()

        assert driver.find_element(by.ID, 'addmessage').text == str(inp1 + inp2)

    def test_InputFormSubmit(self):
        driver.get('https://www.lambdatest.com/selenium-playground/input-form-demo')
        driver.find_element(by.ID, 'name').send_keys('python')
        driver.find_element(by.ID, 'inputEmail4').send_keys('golefi9207@lukaat.com')
        driver.find_element(by.ID, 'inputPassword4').send_keys('pass')
        driver.find_element(by.ID, 'company').send_keys('company51')
        driver.find_element(by.ID, 'websitename').send_keys('https://example.com')
        driver.find_element(by.ID, 'seleniumform').click()
        driver.find_element(by.XPATH, '//option[@value="AU"]').click()
        driver.find_element(by.ID, 'inputCity').send_keys('sydney')
        driver.find_element(by.ID, 'inputAddress1').send_keys('address1')
        driver.find_element(by.ID, 'inputAddress2').send_keys('address2')
        driver.find_element(by.ID, 'inputState').send_keys('state')
        driver.find_element(by.ID, 'inputZip').send_keys('1337')
        driver.find_element(by.XPATH, '//button[contains(text(), "Submit")]').click()

    def test_UploadFileDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/upload-file-demo')
        driver.find_element(by.ID, 'file').send_keys('C:\\Users\\1chud\\Downloads\\ChatGPTbot.png')

    def test_SliderDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/drag-drop-range-sliders-demo')
        input_ids = ['range', 'rangePrimary', 'rangeSuccess', 'rangeInfo', 'rangeWarning', 'rangeDanger',
                     'rangeWarning',
                     'rangeDanger']
        output_val = []

        for idx in input_ids:
            output_val.append(driver.find_element(by.ID, f'{idx}').text)

        for i in range(0, 8):
            for j in range(5):
                driver.find_elements(by.XPATH, '//input[@type="range"]')[i].send_keys(Keys.RIGHT)

        for ids, idx in enumerate(input_ids):
            assert int(driver.find_element(by.ID, f'{idx}').text) == int(output_val[ids]) + 5
        time.sleep(3)

    def test_BootstrapProgressBarDialogDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/bootstrap-progress-bar-dialog-demo')
        elems = driver.find_elements(by.XPATH, "//*[contains(text(),'Show dialog')]")
        rand_elem = random.choice(elems)
        rand_elem.click()
        WebDriverWait(driver, 10).until_not(
            ec.text_to_be_present_in_element_attribute((by.XPATH, '/html/body'), 'class', 'modal-open'))

        assert driver.find_element(by.XPATH,
                                   '//section[@class="mt-50"]//h2').text == "waitingDialog.show('Hello Alert !!!');"

    def test_JQueryDatePickerDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/jquery-date-picker-demo')
        driver.find_element(by.XPATH, '//input[@id="from"]').click()
        driver.find_element(by.XPATH, "//select[@class='ui-datepicker-month']//option[1]").click()
        driver.find_element(by.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[1]/a').click()
        time.sleep(1)
        driver.find_element(by.XPATH, '//input[@id="to"]').click()
        driver.find_element(by.XPATH, '//select[@class="ui-datepicker-month"]//option[12]').click()
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

    def test_BrokenImages(self):
        driver.get('https://www.lambdatest.com/selenium-playground/broken-image')
        img_div = driver.find_element(by.XPATH, '//*[@id="__next"]/section[3]/div/div/div/div')
        images = img_div.find_elements(by.TAG_NAME, 'img')
        k = 0
        for img in images:
            src = img.get_attribute('src')
            r = requests.get(src)
            if r != 200:
                k += 1
        # print(f'{k} broken images')
        assert k == 2

    def test_GeolocationTesting(self):
        # driver.get('https://www.lambdatest.com/selenium-playground/geolocation-testing')
        pass

    def test_RadiobuttonDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/radiobutton-demo')
        driver.find_element(by.XPATH, '//*[@id="__next"]/div/section[2]/div/div/div/div[1]/div/label[1]/input').click()
        driver.find_element(by.XPATH, '//*[@id="buttoncheck"]').click()
        assert ('Male' in driver.find_element(by.XPATH,
                                              '//*[@id="__next"]/div/section[2]/div/div/div/div[1]/div/p[2]').text) == True

        driver.find_element(by.XPATH,
                            '//*[@id="__next"]/div/section[2]/div/div/div/div[2]/div/div/div/div[2]/label/input').click()
        assert driver.find_element(by.XPATH,
                                   '//*[@id="__next"]/div/section[2]/div/div/div/div[2]/div/div/div/div[2]/label/input').is_selected() == True

        driver.find_elements(by.XPATH, "//input[@name='gender']")[2].click()
        driver.find_elements(by.XPATH, "//input[@name='ageGroup']")[0].click()
        driver.find_element(by.XPATH, '//button[contains(text(),"Get values")]').click()
        assert ('Other' in driver.find_element(by.XPATH, '//p[@class="mb-20 font-medium"]').text) == True
        assert ('0 - 5' in driver.find_element(by.XPATH, '//p[@class="font-medium"]').text) == True

    def test_JqueryDropdownSearchDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
        driver.find_elements(by.XPATH, '//span[@class="selection"]')[0].click()
        driver.find_element(by.XPATH, '//li[contains(text(),"United States")]').click()
        driver.find_elements(by.XPATH, '//span[@class="selection"]')[1].click()
        driver.find_element(by.XPATH, '//li[contains(text(),"Hawaii")]').click()
        driver.find_elements(by.XPATH, '//span[@class="selection"]')[1].click()
        driver.find_element(by.XPATH, '//li[contains(text(),"California")]').click()
        driver.find_elements(by.XPATH, '//span[@class="selection"]')[2].click()
        driver.find_element(by.XPATH, '//li[contains(text(),"Virgin Islands")]').click()
        driver.find_element(by.XPATH, '//select[@name="files"]').click()
        driver.find_element(by.XPATH, '//option[contains(text(),"Python")]').click()

    def test_JqueryDownloadProgressBarDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/jquery-download-progress-bar-demo')
        driver.find_element(by.XPATH, '//button[@id="downloadButton"]').click()
        WebDriverWait(driver, 10).until(
            ec.text_to_be_present_in_element((by.XPATH, '//div[@class="progress-label"]'), 'Complete!'))
        driver.find_element(by.XPATH, '//button[contains(text(),"Close")]')
        assert (driver.find_element(by.XPATH, '//div[@role="dialog"]').get_attribute('display') == 'none') == False

    def test_BootstrapModal(self):
        driver.get('https://www.lambdatest.com/selenium-playground/bootstrap-modal-demo')
        # Single Modal
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[0].is_displayed() == False
        driver.find_elements(by.XPATH, '//button[contains(text(),"Launch Modal")]')[0].click()
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[0].is_displayed() == True
        driver.find_element(by.XPATH, '//button[contains(text(),"Save Changes")]').click()
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[0].is_displayed() == False
        # Multiple Modal
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[1].is_displayed() == False
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[2].is_displayed() == False
        driver.find_elements(by.XPATH, '//button[contains(text(),"Launch Modal")]')[1].click()
        driver.find_elements(by.XPATH, '//button[contains(text(),"Launch Modal")]')[2].click()
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[1].is_displayed() == True
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[2].is_displayed() == True
        driver.find_elements(by.XPATH, '//button[contains(text(),"Save Changes")]')[2].click()
        driver.find_elements(by.XPATH, '//button[contains(text(),"Save Changes")]')[1].click()
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[1].is_displayed() == False
        assert driver.find_elements(by.XPATH, '//div[@class="modal-dialog"]')[2].is_displayed() == False

    def test_FileDownloadDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/generate-file-to-download-demo')
        driver.find_element(by.XPATH, '//textarea[@id="textbox"]').send_keys('some text!:)')
        driver.find_element(by.XPATH, '//button[@id="create"]').click()
        driver.find_element(by.XPATH, '//a[@id="link-to-download"]').click()
        time.sleep(1)
        assert os.path.exists('C:\\Users\\1chud\\Downloads\\Lambdainfo.txt') == True

    def test_JQueryDualListBox(self):
        driver.get('https://www.lambdatest.com/selenium-playground/jquery-dual-list-box-demo')
        names = ['Andrea', 'Newbry', 'West', 'Gibbs', 'Una', 'Liam', 'Talisman', 'Brooks', 'McDonald', 'Hamilton',
                 'Portland', 'Wakeman', 'Zak', 'Tackett', 'Tebbit']
        driver.find_element(by.XPATH, '//button[contains(text(),"Add All")]').click()
        select2 = driver.find_element(by.XPATH, '//select[contains(@class,"pickListResult")]')
        options2 = select2.find_elements(by.XPATH, './option')
        actual_names_count = 0
        expected_names_count = len(names)
        for option in options2:
            if option.text in names:
                actual_names_count += 1
        assert expected_names_count == actual_names_count

        opt1 = driver.find_element(by.XPATH, '//option[contains(text(),"Talisman")]')
        opt1.click()
        driver.find_element(by.XPATH, '//button[contains(text(),"Remove")]').click()
        select1 = driver.find_element(by.XPATH, '//select[contains(@class,"pickData")]')
        options1 = select1.find_elements(by.XPATH, './option')
        actual_names_count = 0
        for option in options1:
            if option.text in 'Talisman':
                actual_names_count += 1
        assert actual_names_count == 1

    @pytest.mark.latest
    def test_TableilterDemo(self):
        driver.get('https://www.lambdatest.com/selenium-playground/table-records-filter-demo')
        # HyperExecute rows
        driver.find_element(by.XPATH, '//button[@data-target="pagado"]').click()
        actual_rows = 0
        expected_rows = len(
            driver.find_elements(by.XPATH, '//table[@class="table table-filter"]/tbody/tr[@data-status="pagado"]'))
        for row in driver.find_elements(by.XPATH, '//table[@class="table table-filter"]/tbody/tr'):
            if 'HyperExecute' in row.text:
                actual_rows += 1
        assert actual_rows == expected_rows

        # Selenium Testing rows
        driver.find_element(by.XPATH, '//button[@data-target="pendiente"]').click()
        actual_rows = 0
        expected_rows = len(
            driver.find_elements(by.XPATH, '//table[@class="table table-filter"]/tbody/tr[@data-status="pendiente"]'))
        for row in driver.find_elements(by.XPATH, '//table[@class="table table-filter"]/tbody/tr'):
            if 'Selenium Testing' in row.text:
                actual_rows += 1
        assert actual_rows == expected_rows

        # Cypress Testing rows
        driver.find_element(by.XPATH, '//button[@data-target="cancelado"]').click()
        actual_rows = 0
        expected_rows = len(
            driver.find_elements(by.XPATH, '//table[@class="table table-filter"]/tbody/tr[@data-status="cancelado"]'))
        for row in driver.find_elements(by.XPATH, '//table[@class="table table-filter"]/tbody/tr'):
            if 'Cypress Testing' in row.text:
                actual_rows += 1
        assert actual_rows == expected_rows

        # All rows
        driver.find_element(by.XPATH, '//button[@data-target="all"]').click()
        actual_rows = 0
        expected_rows = len(
            driver.find_elements(by.XPATH, '//table[@class="table table-filter"]/tbody/tr[@data-status="all"]'))
        for row in driver.find_elements(by.XPATH, '//table[@class="table table-filter"]/tbody/tr'):
            if 'Cypress Testing' in row.text or 'Cypress Testing' in row.text or 'Selenium Testing' in row.text or 'HyperExecute' in row.text:
                actual_rows += 1
        assert actual_rows == expected_rows
        driver.quit()
