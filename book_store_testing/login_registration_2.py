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

    # 2. Нажмите на вкладку "My Account Menu"
    my_account = driver.find_element(By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/my-account/']")
    my_account.click()
    time.sleep(5)

    # 3. В разделе "Login", введите email для логина
    user_field = driver.find_element(By.ID, "username")
    user_field.send_keys("Test147@mail.ru")
    time.sleep(3)

    # 4. В разделе "Login", введите пароль для логина
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Test!159Test")
    time.sleep(3)

    # 5. Нажмите на кнопку "Login"
    login_button = driver.find_element(By.CSS_SELECTOR, "input.woocommerce-Button.button[name='login']")
    login_button.click()
    time.sleep(3)

    # 6. Добавьте проверку, что на странице есть элемент "Logout"
    # Проверяем наличие элемента "Logout" с использованием явного ожидания
    logout_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
    )

    if logout_element:
        print("Элемент 'Logout' успешно найден на странице.")
    else:
        print("Ошибка: Элемент 'Logout' не найден на странице.")

finally:
    # Закрытие браузера
    driver.quit()