from selenium.common.exceptions import NoSuchElementException
from pages.swag_labs import SwagLabs

#driver.get("https://saucedemo.com/")
#icon = driver.find_element(By.CSS_SELECTOR, "div.login_logo")
#    if icon is None:
#         print("Элемент не найден")
#    else:
#         print("Элемент найден")
def exist_icon(self):
    try:
        self.icon.find_element()
    except NoSuchElementException:
        return False
    return True

def exist_login(self):
    try:
        self.login.find_element()
    except NoSuchElementException:
        return False
    return True

def exist_password(self):
    try:
        self.login.find_element()
    except NoSuchElementException:
        return False
    return True
