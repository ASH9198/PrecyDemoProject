from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from percy import percy_snapshot
 
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
pagetitle = driver.title
print(pagetitle)
percy_snapshot(driver=driver, name='Demo Page')
driver.close()