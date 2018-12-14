from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains;
import time
from re import sub
from decimal import Decimal
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button




class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 3
        
        FBusername = 'username'
        FBpassword = 'password'

        CHurl = "https://secure01a.chase.com/web/auth/#/logon/logon/chaseOnline?"
        FBurl = "https://web13.secureinternetbank.com/pbi_pbi1151/login/062102221"

        driver = webdriver.Chrome("C:\\Users\\USERNAME\\Desktop\\chromedriver")


        #ChaseBank
        driver.get(CHurl)
        time.sleep(3)
        actions = ActionChains(driver)
        actions.send_keys("Username")
        actions.key_down(Keys.TAB)
        actions.send_keys("Password")
        actions.key_down(Keys.ENTER)
        actions.perform()
        time.sleep(10)

        Credit = driver.find_element_by_xpath("//*[@id='accountAvailableCreditBalanceValue']")
        dollars = (Credit.text)
        value = Decimal(sub(r'[^\d.]', '', dollars))
        CreditAmt = (5500 - value)
        time.sleep(1)

        #Friendbank
        driver.get(FBurl)
        time.sleep(2)
        driver.find_element_by_id('username').send_keys(FBusername)
        driver.find_element_by_id('password').send_keys(FBpassword)
        login = driver.find_element_by_xpath("//*[@id='loginIndex']/form/div[4]/div/button").click()
        time.sleep(5)
        Cash = driver.find_element_by_xpath("//*[@id='account_0']/div[2]/a/div[2]/dl/dd/span")
        value2 = Decimal(sub(r'[^\d.]', '', Cash.text))
        CashAmt = (value2 - CreditAmt)


        self.add_widget(Label(text="Credit owed currently: "+str(CreditAmt)))
        self.add_widget(Label(text="Cash currently in bank: "+str(value2)))
        self.add_widget(Label(text="Cash left to spend: "+str(CashAmt)))

class MyApp(App):

    def build(self):
        return LoginScreen()
    
if __name__ == '__main__':
    MyApp().run()

