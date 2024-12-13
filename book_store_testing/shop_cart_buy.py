from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Путь к ChromeDriver
driver_path = r"C:\Users\Алина\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"

# Создаем сервис для ChromeDriver
service = Service(driver_path)

# Инициализация веб-драйвера
driver = webdriver.Chrome(service=service)

try:
    # 1. Откройте сайт
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()

    # 2. Нажмите на вкладку "Shop" и прокрутите на 300 пикселей вниз
    shop_tab = driver.find_element(By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/shop/']")
    shop_tab.click()
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(3)

    # 3. Добавьте в корзину книгу "HTML5 WebApp Development"
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "a[href='/shop/?add-to-cart=182']")
    add_to_cart_button.click()
    time.sleep(3)

    # 4. Перейдите в корзину
    basket_button = driver.find_element(By.CSS_SELECTOR, "i.wpmenucart-icon-shopping-cart-0")
    basket_button.click()
    time.sleep(3)

    # 5. Нажмите "PROCEED TO CHECKOUT"
    proceed_to_checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.checkout-button"))
    )
    proceed_to_checkout_button.click()

    # 6. Заполните все обязательные поля
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "billing_first_name"))
    )
    first_name = driver.find_element(By.ID, "billing_first_name")
    first_name.send_keys("Алина")

    last_name = driver.find_element(By.ID, "billing_last_name")
    last_name.send_keys("Макеева")

    email = driver.find_element(By.ID, "billing_email")
    email.send_keys("test@test.com")

    phone = driver.find_element(By.ID, "billing_phone")
    phone.send_keys("1234567890")

    # Заполнение страны
    # Клик на раскрывающийся список
    country_dropdown = driver.find_element(By.CSS_SELECTOR, "div#s2id_billing_country")
    country_dropdown.click()
    time.sleep(1)

    # Ввод текста в поле поиска
    search_box = driver.find_element(By.ID, "s2id_autogen1_search")
    search_box.send_keys("Russia")
    time.sleep(2)

# СДАЮСЬ! ДАЛЬШЕ КОД НЕ РАБОТАЕТ И, ГДЕ ОШИБКА, НЕ ПОНИМАЮ............

    # Поиск и выбор элемента из выпадающего списка
    russia_option = driver.find_element(By.XPATH, "//*[@id='billing_country']/option[183]")
    russia_option.click()

    address = driver.find_element(By.ID, "billing_address_1")
    address.send_keys("Test address")

    city = driver.find_element(By.ID, "billing_city")
    city.send_keys("Moscow")

    state = driver.find_element(By.ID, "billing_state")
    state.send_keys("Moscow")

    postcode = driver.find_element(By.ID, "billing_postcode")
    postcode.send_keys("123456")

    # 7. Выберите способ оплаты "Check Payments"
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(3)
    check_payments = driver.find_element(By.ID, "payment_method_cheque")
    check_payments.click()

    # 8. Нажмите PLACE ORDER
    place_order_button = driver.find_element(By.ID, "place_order")
    place_order_button.click()

    # 9. Проверьте, что отображается надпись "Thank you. Your order has been received."
    thank_you_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"))
    )
    assert thank_you_message.text == "Thank you. Your order has been received.", "Неверное сообщение после оформления заказа."

    # 10. Проверьте, что в Payment Method отображается текст "Check Payments"
    payment_method = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table.shop_table.order_details tfoot tr:nth-child(3) td"))
    )
    assert payment_method.text == "Check Payments", "Неверный способ оплаты."

finally:
    # Закрытие браузера
    driver.quit()
