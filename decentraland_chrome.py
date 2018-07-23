import time
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def waitFunction(timeout, driver,path):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, path.text)))

    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()

#Variables
i = 0
j = 1
password = 'rupek987'
coins = 0
#Define Webdriver and setting browser
options = Options()
options.add_argument(r"user-data-dir=C:/Users/Dariusz/AppData/Local/Google/Chrome/User Data");
options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(executable_path="C:/Users/Dariusz/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=options)

#Login to MetaMask
driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/popup.html')
waitFunction(20,driver,"//button[@class='primary cursor-pointer']")
password_input = driver.find_element_by_id('password-box')
password_input.send_keys(password)
driver.find_element_by_xpath("//button[@class='primary cursor-pointer']").click()
waitFunction(20,driver."//div[@class='ether-balance ether-balance-amount']")

#Opening decentraland
driver.execute_script("window.open('','_blank');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://market.decentraland.org/marketplace?page=1&sort_by=price&sort_order=asc')
waitFunction(20,driver,"//i[@class='pull-left Icon Icon-decentraland']")

while True:
    #Refresh webpages
    driver.refresh()
    
    #GetCurrentWallet
    driver.switch_to.window(driver.window_handles[0])
    coins = driver.find_elements_by_xpath("//div[@class='tooltip-inner']")
    coins = float(coins)
    
    #Switch to decentraland
    driver.switch_to.window(driver.window_handles[1])
    
    #Find all parcels on this page
    price_element = driver.find_elements_by_xpath("//div[@class='description']")
    prices = [x.text.split("\n")[1].replace(' ','') for x in price_element]
    print('prices:')
    print(prices, '\n')

    #Find all coords of those parcels
    coords_element = driver.find_elements_by_xpath("//div[@class='coords']")
    coords = [x.text for x in coords_element]
    print('coords:')
    print(coords,'\n')

    #Find targeted parcels
    for x in prices:
        if(float(x) <= coins):
        
            driver.execute_script("window.open('','_blank');")
            url = 'https://market.decentraland.org/' + coords[i].split(",")[0] + '/' + coords[i].split(",")[1] + '/buy'
            i+=1
            j+=1
        
            driver.switch_to.window(driver.window_handles[j])
            driver.get(url)
            waitFunction(20,driver,"//button[@class='ui-button']")
            
            driver.find_elements_by_xpath("//button[@class='ui button']").click()
        
        else:
            time.sleep(1)