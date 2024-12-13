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

    # 2. Нажмите на вкладку "Shop"
    shop = driver.find_element(By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/shop/']")
    shop.click()
    time.sleep(3)

    # 3. Добавьте в корзину книгу "HTML5 WebApp Development"
    book_add_to_basket = driver.find_element(By.CSS_SELECTOR, "a[href='/shop/?add-to-cart=182']")
    book_add_to_basket.click()
    time.sleep(3)

    # 4. Добавьте тест, что в возле корзины (вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
    basket_info = driver.find_element(By.CSS_SELECTOR, "span.cartcontents").text
    basket_price = driver.find_element(By.CSS_SELECTOR, "span.amount").text

    # Проверка с использованием assert
    assert basket_info == "1 Item", f"Ожидалось '1 Item', но получено '{basket_info}'"
    assert basket_price == "₹180.00", f"Ожидалось '₹180.00', но получено '{basket_price}'"
    print("Тест 4: Количество товаров и цена в корзине отображаются корректно.")

    # 5. Перейдите в корзину
    basket_button = driver.find_element(By.CSS_SELECTOR, "i.wpmenucart-icon-shopping-cart-0")
    basket_button.click()
    time.sleep(3)

    # 6. Используя явное ожидание, проверьте, что в Subtotal отобразилась стоимость
    subtotal_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td[data-title='Subtotal'] span.woocommerce-Price-amount"))
    )
    subtotal_price = subtotal_element.text
    print(f"Subtotal найден: {subtotal_price}")

    # 7. Используя явное ожидание, проверьте, что в Total отобразилась стоимость
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td[data-title='Total'] span.woocommerce-Price-amount"))
    )
    total_price = total_element.text
    print(f"Total найден: {total_price}")

finally:
    # Закрытие браузера
    driver.quit()
