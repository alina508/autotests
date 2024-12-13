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

    # 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
    select_element = Select(driver.find_element(By.CLASS_NAME, "orderby"))
    default_value = select_element.first_selected_option.get_attribute("value")

    if default_value == "menu_order":
        print("Тест пройден: выбран вариант сортировки по умолчанию.")
    else:
        print(f"Тест провален: текущий вариант сортировки - {default_value}.")

    # 5. Отсортируйте товары по цене от большей к меньшей
    select_element.select_by_value("price-desc")  
    print("Товары отсортированы по цене от большей к меньшей.")
    time.sleep(5)

    # 6. Снова объявите переменную с локатором основного селектора сортировки
    sort_selector = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "orderby"))
    ))

    # 7. Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
    sorted_value = sort_selector.first_selected_option.get_attribute("value")
    if sorted_value == "price-desc":
        print("Тест пройден: выбран вариант сортировки от большей к меньшей.")
    else:
        print(f"Тест провален: выбран другой вариант сортировки: {sorted_value}")

finally:
    # Закрытие браузера
    driver.quit()
