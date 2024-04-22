from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    print("\nstart chrome browser for test..")
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
