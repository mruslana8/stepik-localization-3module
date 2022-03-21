import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_button_available(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector(".btn-add-to-basket")
    print('Text ' + button[0].text)
    assert button is not None, 'Кнопка не найдена'
