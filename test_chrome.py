import unittest
import HtmlTestRunner
from time import sleep
# import pyautogui
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

class automationChromeTest(unittest.TestCase):
    def setUp(self):
        self.service = Service('D:/University/Testing/sources/chromedriver/chromedriver.exe')
        self.driver = WebDriver(service=self.service)
        self.driver.maximize_window()
        sleep(2)
        
    def tearDown(self):
        self.driver.quit()

    # test login with account
    def testLogin(self):
        self.driver.get("https://www.w3schools.com/")
        sleep(2)
        login_web = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/a")
        login_web.click()
        sleep(2)

        # username = pyautogui.prompt(text='Enter your username:', title='Login', default='') # tạo khung input username
        # password = pyautogui.password(text='Enter your password:', title='Login', default='') # tạo khung input password
        username_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/div[2]/input")
        password_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[2]/div[2]/input")
        # username_field.clear()
        username_field.send_keys("p.t.q.duy192002@gmail.com")
        # password_field.clear()
        password_field.send_keys("Duycuti@2002")

        login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[4]/div[1]/button")
        login_button.click()
        sleep(15) # có thể thay đổi thời gian tùy thuộc vào tốc độ load page

        # Kiểm tra xem có hiển thị thông báo lỗi hay không
        # error_message_usrname = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/span")
        # error_message_pass = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[3]/div")

        # if error_message_usrname:
        #     # Thông báo lỗi được hiển thị, xác nhận rằng nó là thông báo lỗi mật khẩu
        #     print(error_message_usrname[0].text)
        #     self.fail("Failed to login with username: %s and password: %s" % (username_field, password_field))

        # elif error_message_pass:
        #     # Thông báo lỗi được hiển thị, xác nhận rằng nó là thông báo lỗi mật khẩu
        #     print(error_message_pass[0].text)
        #     self.fail("Failed to login with username: %s and password: %s" % (username_field, password_field))
        # else:
        # Không có thông báo lỗi được hiển thị, xác nhận rằng người dùng đã đăng nhập thành công
        expected_title = "My learning | W3Schools"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title)


    def testLoginUsernameError(self):
        self.driver.get("https://www.w3schools.com/")
        sleep(2)
        login_web = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/a")
        login_web.click()
        sleep(2)

        for i in range(3):
            input_str = ["fwenvwvoi", "12456134", "12ca23dfsat1@.com", "darkdảkbruhrbuh123@", "luliliivevun@gm", "!@#$%^&*()"]
            # username = pyautogui.prompt(text='Enter your username:', title='Login', default='') # tạo khung input username
            # password = pyautogui.password(text='Enter your password:', title='Login', default='') # tạo khung input password
            username_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/div[2]/input")
            password_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[2]/div[2]/input")
            # username_field.clear()
            username_field.send_keys(random.choice(input_str))
            # password_field.clear()
            password_field.send_keys("Duycuti@2002")


            login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[4]/div[1]/button")
            login_button.click()
            sleep(15) # có thể thay đổi thời gian tùy thuộc vào tốc độ load page

            # Kiểm tra xem có hiển thị thông báo lỗi hay không
            error_message_usrname = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/span")
        
            if error_message_usrname:
                # Thông báo lỗi được hiển thị, xác nhận rằng nó là thông báo lỗi mật khẩu
                failed_username = username_field.get_attribute("value")
                print("Failed to login with username: %s " % failed_username)
                self.fail("Failed to login with username: %s " % failed_username)


            else:
                # Không có thông báo lỗi được hiển thị, xác nhận rằng người dùng đã đăng nhập thành công
                expected_title = "My learning | W3Schools"
                actual_title = self.driver.title
                self.assertEqual(expected_title, actual_title)
                self.assertTrue(True, "Login successful with username: %s and password: %s" % (username_field.get_attribute("value"), password_field.get_attribute("value")))


    def testLoginDifMethod(self):
        self.driver.get("https://www.w3schools.com/")
        sleep(2)
        login_web = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/a")
        login_web.click()
        sleep(2)

        login_method = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[4]/div[2]/button[2]")
        login_method.click()
        sleep(5)

        email_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/form/input[2]")
        email_field.send_keys("QuocDuuy")
        sleep(1)

        pass_field = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[1]")
        pass_field.send_keys("Duycuti@2002")
        sleep(1)
        submit_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[11]")
        submit_btn.click()
        sleep(15)

        # authorize = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div[2]/div[1]/div[2]/div[1]/form/div/button[2]")
        # authorize.click()
        


    # test searching
    def testSearching(self):
        self.driver.get("https://www.w3schools.com/")
        sleep(2)


        content = ["html", "css", "javascript tutorial", "python", "pandas tut", "numpy tuto"]
        # tìm thanh search
        # search_bar = pyautogui.prompt(text='Enter your username:', title='Searching', default='')
        search_bar_field = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/form/input")
        sleep(1)
        search_bar_field.send_keys(random.choice(content))

        # search button
        search_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/form/button")
        sleep(1)
        search_button.click()

        sleep(1.5)
        # Kiểm tra xem có hiển thị element có XPATH "/html/body/div[1]/div/div/div/div[1]/div[6]/div[2]/div/div/div[1]/div[1]/div" hay không
        # error_element = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[6]/div[2]/div/div/div[1]/div[1]/div/div")
        # if error_element:
        #     # Element được hiển thị, test fail
        #     self.fail(error_element[0].text)



    def testSearchingError(self):
        self.driver.get("https://www.w3schools.com/")
        sleep(2)
        content = ["vfdbvieunviouwernv", "12432531513", "!@#$%^&*()"]
        # tìm thanh search
        # search_bar = pyautogui.prompt(text='Enter your username:', title='Searching', default='')
        search_bar_field = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/form/input")
        sleep(1)
        search_bar_field.send_keys(random.choice(content))

        # search button
        search_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/form/button")
        sleep(1)
        search_button.click()
        sleep(1.5)
        # Kiểm tra xem có hiển thị element có XPATH "/html/body/div[1]/div/div/div/div[1]/div[6]/div[2]/div/div/div[1]/div[1]/div" hay không
        error_element = self.driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[6]/div[2]/div/div/div[1]/div[1]/div/div")
        if error_element:
            # Element được hiển thị, test fail
            self.fail(error_element[0].text)

        # test checkbox
    def testCheckBox(self):
        self.driver.get("https://www.w3schools.com/")
        sleep(2)

        # tìm thanh search
        
        theme_icon = self.driver.find_element(By.CSS_SELECTOR, "#main > div:nth-child(1) > div > a:nth-child(3)") #/html/body/div[6]/div[1]/div/a[3]
        theme_icon.click()
        sleep(2)

        # Kiểm tra trạng thái ban đầu của checkbox
        checkbox1 = self.driver.find_element(By.CSS_SELECTOR, "#radio_darkpage")
        checkbox2 = self.driver.find_element(By.CSS_SELECTOR, "#radio_darkcode")
        self.assertTrue(checkbox1.is_selected())
        self.assertTrue(checkbox2.is_selected())

        # Chọn checkbox 1 và kiểm tra kết quả
        checkbox1.click()
        self.assertFalse(checkbox1.is_selected())
        sleep(0.75)
        checkbox2.click()
        self.assertFalse(checkbox2.is_selected())
        sleep(1)

        checkbox1.click()
        self.assertTrue(checkbox1.is_selected())
        sleep(0.75)
        checkbox2.click()
        self.assertTrue(checkbox2.is_selected())
        sleep(1)