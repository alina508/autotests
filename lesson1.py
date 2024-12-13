from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Путь к ChromeDriver
driver_path = r"C:\Users\Алина\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"

# Инициализация веб-драйвера
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # 1. Откройте страницу
    driver.get("https://demo.automationtesting.in/WebTable.html")
    driver.maximize_window()
    print("1. Открыта страница: https://demo.automationtesting.in/WebTable.html.")

    # 2. Реализуйте неявное ожидание поиска элементов
    driver.implicitly_wait(10)
    print("2. Неявное ожидание установлено.")

    # 3. Перейдите в раздел "Switch to" -> "Windows"
    switch_to_menu = driver.find_element(By.LINK_TEXT, "SwitchTo")
    switch_to_menu.click()
    print("3. Открыто меню 'Switch to'.")

    windows_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Windows"))
    )
    windows_option.click()
    print("3. Открыт раздел 'Windows'.")

    # 4. В разделе "Open New Tabbed Windows" нажмите кнопку "click"
    new_tab_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-info"))
    )
    new_tab_button.click()
    print("4. Нажата кнопка 'click' для открытия новой вкладки.")

    # 5. Переключите драйвер на вторую вкладку -> закройте её -> переключитесь обратно на первую вкладку
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[1])
    print("Переключено на вторую вкладку.")
    driver.close()
    print("Вторая вкладка закрыта.")
    driver.switch_to.window(window_handles[0])
    print("Переключено обратно на первую вкладку.")

    # 6. Перейдите в раздел "Separate Multiple Windows" и нажмите "click"
    separate_windows_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#Multiple']"))
    )
    separate_windows_option.click()
    print("6. Перешли в раздел 'Separate Multiple Windows'.")
    separate_click_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-info[onclick='multiwindow()']"))
    )
    separate_click_button.click()
    print("6. Нажата кнопка 'click'.")
    # 7. Переключите драйвер на вторую вкладку
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[2])
    print("7. Переключено на вторую вкладку.")

    # 8. Проверьте, что ссылка = "https://demo.automationtesting.in/Index.html"
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://demo.automationtesting.in/Index.html")
    )
    print("8. Проверка: ссылка равна 'https://demo.automationtesting.in/Index.html'.")
    time.sleep(3)
    # 9. Проверьте, что в браузере открыто 3 вкладки, выведите результат проверки
    print(f"9. Проверка: открыто ли 3 вкладки? {'True' if len(driver.window_handles) == 3 else 'False'}.")

    # 10. В поле "email" напишите любую почту и нажмите кнопку ">"
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_field.send_keys("test@example.com")
    email_button = driver.find_element(By.ID, "enterimg")
    email_button.click()
    print("10. Введена почта и нажата кнопка '>'.")

    # 11. Проверьте, что ссылка = "https://demo.automationtesting.in/Register.html"
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://demo.automationtesting.in/Register.html")
    )
    print("11. Проверка: ссылка равна 'https://demo.automationtesting.in/Register.html'.")

finally:
    driver.quit()
    print("Браузер закрыт.")
