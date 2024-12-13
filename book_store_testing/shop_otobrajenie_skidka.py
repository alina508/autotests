from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

# Путь к ChromeDriver
driver_path = r"C:\Users\Алина\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"

# Создаем сервис для ChromeDriver
service = Service(driver_path)

# Инициализация веб-драйвера
driver = webdriver.Chrome(service=service)

try:
    # 1.Открытие страницы
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    time.sleep(5)

    # 2. Залогиньтесь
    my_account = driver.find_element(By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/my-account/']")
    my_account.click()
    time.sleep(5)

    user_field = driver.find_element(By.ID, "username")
    user_field.send_keys("Test147@mail.ru")
    time.sleep(3)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Test!159Test")
    time.sleep(3)

    login_button = driver.find_element(By.CSS_SELECTOR, "input.woocommerce-Button.button[name='login']")
    login_button.click()
    time.sleep(3)

    # 3. Нажмите на вкладку "Shop"
    shop = driver.find_element(By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/shop/']")
    shop.click()
    time.sleep(5)

    # 4. Откройте книгу "Android Quick Start Guide"
    android_book = driver.find_element(By.XPATH, "//h3[text()='Android Quick Start Guide']")
    android_book.click()
    time.sleep(5)

    # 5. Добавьте тест, что содержимое старой цены = "₹600.00"
    old_price_element = driver.find_element(By.CSS_SELECTOR, "del .woocommerce-Price-amount")
    old_price = old_price_element.text
    assert old_price == "₹600.00", f"Тест провален: старая цена = {old_price}, ожидалось '₹600.00'"
    print("Тест пройден: старая цена = ₹600.00")

    # 6. Добавьте тест, что содержимое новой цены = "₹450.00"
    new_price_element = driver.find_element(By.CSS_SELECTOR, "ins .woocommerce-Price-amount")
    new_price = new_price_element.text
    assert new_price == "₹450.00", f"Тест провален: новая цена = {new_price}, ожидалось '₹450.00'"
    print("Тест пройден: новая цена = ₹450.00")

    # 7. Добавьте явное ожидание и нажмите на обложку книги
    cover_image = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img.attachment-shop_single.size-shop_single.wp-post-image"))
    )
    cover_image.click()
    print("Обложка книги успешно нажата.")
    time.sleep(5)

    # 8. Добавьте явное ожидание и закройте предпросмотр, нажав на крестик
    close_preview = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close"))
    )
    close_preview.click()
    print("Окно предпросмотра успешно закрыто.")

finally:
    # Закрытие браузера
    driver.quit()
