from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Saucedemo:
    def test_invalid_username_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        loginBtn = driver.find_element(By.ID,"login-button")
        
        loginBtn.click()
        sleep(3)
        
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(errorMessage.text)
        print(f"TEST SONUCU : {testResult}")
    
    def test_invalid_password_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

        driver.get("https://www.saucedemo.com/")
        sleep(3)
        inputUsername = driver.find_element(By.ID,"user-name")
        loginBtn = driver.find_element(By.ID,"login-button")
        
        inputUsername.send_keys("username")
        sleep(3)
        loginBtn.click()
        sleep(3)
        
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(errorMessage.text)
        print(f"TEST SONUCU : {testResult}")

    def test_locked_user_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

        driver.get("https://www.saucedemo.com/")
        sleep(3)
        inputUsername = driver.find_element(By.ID,"user-name")
        inputPassword = driver.find_element(By.ID,"password")
        loginBtn = driver.find_element(By.ID,"login-button")
        
        inputUsername.send_keys("locked_out_user")
        sleep(3)
        inputPassword.send_keys("secret_sauce")
        sleep(3)
        loginBtn.click()
        sleep(3)

        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(errorMessage.text)
        print(f"TEST SONUCU : {testResult}")

    def test_error_icon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(10)
        errorIcons = driver.find_elements(By.CLASS_NAME,"input_error form_input error")
        print(len(errorIcons))
        sleep(15)
        inputErrorBtn = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorIconsResult = len(errorIcons)
        print(errorIconsResult)
        print(errorIcons)
        inputErrorBtn.click()
        sleep(5)
        if errorIconsResult == 2:
            print("TEST SONUCU : BAŞARISIZ")
        else:
            print("TEST SONUCU : BAŞARILI")

    def test_valid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        inputUsername = driver.find_element(By.ID,"user-name")
        inputPassword = driver.find_element(By.ID,"password")
        loginBtn = driver.find_element(By.ID,"login-button")
        
        inputUsername.send_keys("standard_user")
        sleep(3)
        inputPassword.send_keys("secret_sauce")
        sleep(3)
        loginBtn.click()
        sleep(3)
        testResult = driver.current_url == "https://www.saucedemo.com/inventory.html"
        print(f"TEST SONUCU : {testResult}")
        productsNumber = driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Ürün sayısı : {len(productsNumber)}")
       
test = Test_Saucedemo()
test.test_valid_login()