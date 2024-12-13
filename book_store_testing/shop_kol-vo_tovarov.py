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
    # 1.Открытие страницы
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    time.sleep(5)  # Дайте странице загрузиться

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

    # 4. Откройте категорию "HTML"
    html_category = driver.find_element(By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/product-category/html/']")
    html_category.click()
    time.sleep(5)

    # 5. Добавьте тест, что отображается три товара
    # Используем явное ожидание, чтобы убедиться, что товары загрузились
    products = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.products.masonry-done li"))
    )

    # Проверяем количество отображаемых товаров
    if len(products) == 3:
        print("Тест пройден: отображается 3 товара.")
    else:
        print(f"Тест провален: отображается {len(products)} товаров вместо 3.")

finally:
    # Закрытие браузера
    driver.quit()
