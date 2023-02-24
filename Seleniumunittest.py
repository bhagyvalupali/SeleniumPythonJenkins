import unittest
from selenium import webdriver
import time
class SeleniumTest(unittest.TestCase):
 def test01_launch_app(self):
     filePath = "C:\\Users\\bhagyasr\\PycharmProjects\\Seleniumpythonproject\\Drivers\\chromedriver.exe"

# 1. Launch the chrome browser
     driver = webdriver.Chrome(filePath)
  # Set the wait for 1sec
     time.sleep(1)

# 2. Launch the parabank app
     driver.get("https://parabank.parasoft.com/parabank/index.htm")
     time.sleep(1)

# 3. Validate the page title
     expectedResult = "ParaBank | Welcome | Online Banking"
     actualResult = driver.title
     print(actualResult)
     '''        if (expectedResult == actualResult):            
                   print("Test is passed")       
                else:            
                   print("Test is failed")        '''

     assert expectedResult == actualResult
     time.sleep(1)

# 4. Close the chrome browser
     driver.quit()
if __name__ == '__main__':
 unittest.main()

