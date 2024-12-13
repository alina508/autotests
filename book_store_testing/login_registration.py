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
    # 1.Открытие страницы
    driver.get("http://practice.automationtesting.in/")
    driver.maximize_window()
    time.sleep(5)  # Дайте странице загрузиться

    # 2. Нажмите на вкладку "My Account Menu"
    my_account = driver.find_element(By.CSS_SELECTOR, "a[href='https://practice.automationtesting.in/my-account/']")
    my_account.click()
    time.sleep(5)

    # 3. В разделе "Register" введите email для регистрации
    e_mail_field = driver.find_element(By.ID, "reg_email")
    e_mail_field.send_keys("Test147@mail.ru")
    time.sleep(3)

    # 4. В разделе "Register" введите пароль для регистрации
    password_field = driver.find_element(By.ID, "reg_password")
    password_field.send_keys("Test!159Test")
    time.sleep(3)

    # 5. Нажмите на кнопку "Register"
    register_button = driver.find_element(By.CSS_SELECTOR, "input.woocommerce-Button.button[name='register']")
    register_button.click()
    time.sleep(5)

finally:
    # Закрытие браузера
    driver.quit()