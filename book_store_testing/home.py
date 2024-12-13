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

    # 2. Прокрутите страницу вниз на 600 пикселей
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(2)

    # 3. Нажмите на название книги "Selenium Ruby"
    book_name = driver.find_element(By.XPATH, "//h3[text()='Selenium Ruby']")
    book_name.click()
    time.sleep(5)

    # 4. Нажмите на вкладку "REVIEWS"
    review_element = driver.find_element(By.CSS_SELECTOR, "a[href='#tab-reviews']")
    review_element.click()
    time.sleep(5)

    # 5. Поставьте 5 звёзд
    five_stars = driver.find_element(By.CSS_SELECTOR, ".star-5")
    five_stars.click()
    time.sleep(5)

    # 6. Заполните поле "Review" сообщением: "Nice book!"
    review_field = driver.find_element(By.ID, "comment")
    review_field.send_keys("Nice book!")
    time.sleep(3)

    # 7. Заполните поле "Name"
    name_field = driver.find_element(By.ID, "author")
    name_field.send_keys("Test")
    time.sleep(3)

    # 8. Заполните поле "Email"
    e_mail_field = driver.find_element(By.ID, "email")
    e_mail_field.send_keys("Test@mail.ru")
    time.sleep(3)

    # 9. Нажмите на кнопку "SUBMIT"
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(5)

finally:
    # Закрытие браузера
    driver.quit()