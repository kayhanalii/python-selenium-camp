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
class Test_Day6HomeWork:
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

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_buy_invalid_name(self,username,password):
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
        checkOutBtn = self.driver.find_element(By.ID,"checkout")
        checkOutBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"checkout_info"))
        continueBtn = self.driver.find_element(By.ID,"continue")
        continueBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]")
        assert errorMessage.text == "Error: First Name is required"

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_buy_invalid_lastName(self,username,password):
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
        checkOutBtn = self.driver.find_element(By.ID,"checkout")
        checkOutBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"checkout_info"))
        inputFirstName = self.driver.find_element(By.ID,"first-name")
        inputFirstName.send_keys(username)
        continueBtn = self.driver.find_element(By.ID,"continue")
        continueBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]")
        assert errorMessage.text == "Error: Last Name is required"

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_buy_invalid_zipCode(self,username,password):
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
        checkOutBtn = self.driver.find_element(By.ID,"checkout")
        checkOutBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"checkout_info"))
        inputFirstName = self.driver.find_element(By.ID,"first-name")
        inputFirstName.send_keys(username)
        inputLastName = self.driver.find_element(By.ID,"last-name")
        inputLastName.send_keys("lastname")
        continueBtn = self.driver.find_element(By.ID,"continue")
        continueBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]")
        assert errorMessage.text == "Error: Postal Code is required"

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_buy_valid(self,username,password):
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
        checkOutBtn = self.driver.find_element(By.ID,"checkout")
        checkOutBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"checkout_info"))
        inputFirstName = self.driver.find_element(By.ID,"first-name")
        inputFirstName.send_keys(username)
        inputLastName = self.driver.find_element(By.ID,"last-name")
        inputLastName.send_keys("lastname")
        inputZipCode = self.driver.find_element(By.ID,"postal-code")
        inputZipCode.send_keys("16")
        continueBtn = self.driver.find_element(By.ID,"continue")
        continueBtn.click()
        testResult = self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"
        assert testResult == True

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_buy_finish(self,username,password):
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
        checkOutBtn = self.driver.find_element(By.ID,"checkout")
        checkOutBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"checkout_info"))
        inputFirstName = self.driver.find_element(By.ID,"first-name")
        inputFirstName.send_keys(username)
        inputLastName = self.driver.find_element(By.ID,"last-name")
        inputLastName.send_keys("lastname")
        inputZipCode = self.driver.find_element(By.ID,"postal-code")
        inputZipCode.send_keys("16")
        continueBtn = self.driver.find_element(By.ID,"continue")
        continueBtn.click()
        finishBtn = self.driver.find_element(By.ID,"finish")
        finishBtn.click()
        testResult = self.driver.current_url == "https://www.saucedemo.com/checkout-complete.html"
        assert testResult == True