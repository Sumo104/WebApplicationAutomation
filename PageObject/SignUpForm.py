from selenium.webdriver.common.by import By


class SignUpForm:
    def __init__(self,driver):
        self.driver=driver

    username=(By.CSS_SELECTOR,"#user-name")
    pwd=(By.ID,"password")
    loginbtn=(By.CSS_SELECTOR,"#login-button")
    webtitle=(By.XPATH,"//a[@id='item_4_title_link']/div[@class='inventory_item_name']")
    errortext=(By.XPATH,"//h3")

    def user_name(self):
        return self.driver.find_element(*SignUpForm.username)

    def password(self):
        return self.driver.find_element(*SignUpForm.pwd)

    def login_btn(self):
        return self.driver.find_element(*SignUpForm.loginbtn)

    def web_title(self):
        return self.driver.find_element(*SignUpForm.webtitle)

    def error_text(self):
        return self.driver.find_element(*SignUpForm.errortext)




