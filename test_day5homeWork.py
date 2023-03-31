from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from pathlib import Path
from datetime import date
from constants import globalConstants

class Test_Day5HomeWork:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalConstants.URL)
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        self.waitForElementVisible((By.ID,globalConstants.LOGINBTN))
    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located((locator)))
        
    def test_invalid_username_login(self):
        loginBtn = self.driver.find_element(By.ID,globalConstants.LOGINBTN)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,globalConstants.ERRORMESSAGE)
        assert  errorMessage.text == "Epic sadface: Username is required"
    @pytest.mark.parametrize("username",["username"])
    def test_invalid_password_login(self,username):
        inputUsername = self.driver.find_element(By.ID,globalConstants.USERNAMEINPUT)
        loginBtn = self.driver.find_element(By.ID,globalConstants.LOGINBTN)
        inputUsername.send_keys(username)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,globalConstants.ERRORMESSAGE)
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login-{username}.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    @pytest.mark.parametrize("username,password",[("locked_out_user","secret_sauce")])
    def test_locked_user_login(self,username,password):
        inputUsername = self.driver.find_element(By.ID,globalConstants.USERNAMEINPUT)
        inputPassword = self.driver.find_element(By.ID,globalConstants.PASSWORDINPUT)
        loginBtn = self.driver.find_element(By.ID,globalConstants.LOGINBTN)
        inputUsername.send_keys(username)
        inputPassword.send_keys(password)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,globalConstants.ERRORMESSAGE)
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-user-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
    
    def test_error_icon(self):
        loginBtn = self.driver.find_element(By.ID,globalConstants.LOGINBTN)
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-error-icon.png")
        inputErrorBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorMassage = self.driver.find_element(By.CLASS_NAME, "error-message-container")
        inputErrorBtn.click()
        assert errorMassage.text == ""

    @pytest.mark.parametrize("username, password", [("standard_user","secret_sauce"), ("performance_glitch_user","secret_sauce"), ("problem_user","secret_sauce")])
    def test_valid_login(self,username,password):
        inputUsername = self.driver.find_element(By.ID,globalConstants.USERNAMEINPUT)
        inputPassword = self.driver.find_element(By.ID,globalConstants.PASSWORDINPUT)
        loginBtn = self.driver.find_element(By.ID,globalConstants.LOGINBTN)
        inputUsername.send_keys(username)
        inputPassword.send_keys(password)
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        testResult = self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        productsNumber = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login-{username}-{password}.png")
        assert 6 == len(productsNumber) and testResult == True

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_add_to_cart(self,username,password):
        inputUsername = self.driver.find_element(By.ID,globalConstants.USERNAMEINPUT)
        inputPassword = self.driver.find_element(By.ID,globalConstants.PASSWORDINPUT)
        loginBtn = self.driver.find_element(By.ID,globalConstants.LOGINBTN)
        inputUsername.send_keys(username)
        inputPassword.send_keys(password)
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        addToCartBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        addToCartBtn.click()
        cartListBtn = self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cartListBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"cart_item"))
        cartProducts = self.driver.find_elements(By.CLASS_NAME,"cart_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login-{username}-{password}.png")
        assert 1 == len(cartProducts)
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_delete_to_cart(self,username,password):
        inputUsername = self.driver.find_element(By.ID,globalConstants.USERNAMEINPUT)
        inputPassword = self.driver.find_element(By.ID,globalConstants.PASSWORDINPUT)
        loginBtn = self.driver.find_element(By.ID,globalConstants.LOGINBTN)
        inputUsername.send_keys(username)
        inputPassword.send_keys(password)
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        addToCartBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        addToCartBtn.click()
        cartListBtn = self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cartListBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"cart_item"))
        removeCartListBtn = self.driver.find_element(By.ID,"remove-sauce-labs-backpack")
        removeCartListBtn.click()
        cartProducts = self.driver.find_elements(By.CLASS_NAME,"cart_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login-{username}-{password}.png")
        assert 0 == len(cartProducts)

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_logout(self,username,password):
        inputUsername = self.driver.find_element(By.ID,globalConstants.USERNAMEINPUT)
        inputPassword = self.driver.find_element(By.ID,globalConstants.PASSWORDINPUT)
        loginBtn = self.driver.find_element(By.ID,globalConstants.LOGINBTN)
        inputUsername.send_keys(username)
        inputPassword.send_keys(password)
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        menuBtn = self.driver.find_element(By.ID,"react-burger-menu-btn")
        menuBtn.click()
        logoutBtn = self.driver.find_element(By.ID,"logout_sidebar_link")
        logoutBtn.click()
        testResult = self.driver.current_url == "https://www.saucedemo.com/"
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login-{username}-{password}.png")
        assert testResult == True
        
        
       

        

        
            



        