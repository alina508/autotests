from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Путь к ChromeDriver
driver_path = r"C:\Users\Алина\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"

# Создаем сервис для ChromeDriver
service = Service(driver_path)

# Инициализация веб-драйвера
driver = webdriver.Chrome(service=service)

try:
    # 1. Откройте http://practice.automationtesting.in/
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    time.sleep(5)

    # 2. Нажмите на вкладку "Shop"
    shop_tab = driver.find_element(By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/shop/']")
    shop_tab.click()
    time.sleep(3)

    # 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
    driver.execute_script("window.scrollBy(0, 300);")
    time.sleep(2)
    first_book = driver.find_element(By.CSS_SELECTOR, "a[href='/shop/?add-to-cart=182']")
    first_book.click()
    time.sleep(3)

    second_book = driver.find_element(By.CSS_SELECTOR, "a[href='/shop/?add-to-cart=180']")
    second_book.click()
    time.sleep(3)

    # 4. Перейдите в корзину
    basket_button = driver.find_element(By.CSS_SELECTOR, "i.wpmenucart-icon-shopping-cart-0")
    basket_button.click()
    time.sleep(3)

    # 5. Удалите первую книгу
    remove_first_book = driver.find_element(By.CSS_SELECTOR, "a[data-product_id='182']")
    time.sleep(2)
    remove_first_book.click()
    time.sleep(3)

    # 6. Нажмите на Undo (отмена удаления)
    undo_button = driver.find_element(By.CSS_SELECTOR, "div > div.woocommerce-message > a")
    undo_button.click()
    time.sleep(3)

    # 7. В Quantity увеличьте количество товара до 3 шт. для "JS Data Structures and Algorithm"
    quantity_field = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty.text")
    quantity_field.clear()
    quantity_field.send_keys("3")
    time.sleep(3)

    # 8. Нажмите на кнопку "UPDATE BASKET"
    update_button = driver.find_element(By.CSS_SELECTOR, ".button[name='update_cart']")
    update_button.click()
    time.sleep(3)

    # 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
    quantity_field = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty.text")  # Найдите элемент заново
    updated_quantity = quantity_field.get_attribute("value")
    assert updated_quantity == "3", f"Ожидалось значение '3', но получено '{updated_quantity}'"
    print("Тест 9: Количество товара корректное.")

    # 10. Нажмите на кнопку "APPLY COUPON"
    apply_coupon_button = driver.find_element(By.CSS_SELECTOR, ".button[name='apply_coupon']")
    apply_coupon_button.click()
    time.sleep(3)

    # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
    error_message = driver.find_element(By.CSS_SELECTOR, "ul.woocommerce-error li").text
    assert error_message == "Please enter a coupon code.", f"Ожидалось сообщение 'Please enter a coupon code.', но получено '{error_message}'"
    print("Тест 11: Сообщение о пустом купоне отображается корректно.")

finally:
    # Закрытие браузера
    driver.quit()
