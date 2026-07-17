from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.maximize_window()

driver.get("https://networkmangement.netlify.app/app.html#dashboard")
time.sleep(10)
driver.find_element(By.XPATH, "//input[@placeholder='Enter username']").send_keys("admin")


driver.find_element(By.XPATH, "//input[@placeholder='Enter password']").send_keys("admin123")


driver.find_element(By.XPATH, "//button[text()='Login']").click()
time.sleep(2)
driver.get("https://networkmangement.netlify.app/app.html#device-config")
time.sleep(2)
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH,"//label[contains(text(),'Config name')]/following::input[1]")
    )
).send_keys("set_hostname_core")

driver.find_element(
    By.XPATH,
    "//label[contains(text(),'Description')]/following::textarea[1]"
).send_keys(
    "This configuration is used to set hostname on core devices."
)

driver.find_element(By.XPATH,'//*[@id="cfgNext"]').click()


time.sleep(5)
 # Select the registered device 'router_core_01'
# Wait for the device radio button to be clickable
device_name = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="cfgDeviceName"]')
    )
)

device_name.send_keys("router-core-01")
time.sleep(10)

# 2. Interact with the 'Connect protocol' dropdown
# Wait for the dropdown and click it to open
protocol_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cfgPlatform"]'))
)
protocol_dropdown.click()

# 3. Select 'SSH' from the options
ssh_option = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="cfgProtocol"]'))
)
ssh_option.click()

# 4. Click the 'Next' button (represented by the green button at the bottom)
next_button = driver.find_element(By.XPATH, '//*[@id="cfgNext"]')
next_button.click()

# Wait briefly to observe result
time.sleep(10)


config_textarea = driver.find_element(By.XPATH, '//*[@id="cfgScript"]')
config_script = """hostname=router-core-01
domain-name=example.com
ssh-enable=yes
telnet-enable=no
interface_g0_0_ip=192.168.1.1
default_gateway=192.168.1.254
dns_server=8.8.8.8
snmp_community=public"""
config_textarea.send_keys(config_script)

# Locate and click the 'Next' button
# Assuming the button has text 'Next' as seen in the bottom right
next_button = driver.find_element(By.XPATH, '//*[@id="cfgNext"]')
next_button.click()

# Keep browser open for a few seconds to verify
time.sleep(5)

push_button = driver.find_element(By.XPATH, '//*[@id="cfgSave"]')
push_button.click()
time.sleep(5)

ok_button = driver.find_element(By.XPATH, '//*[@id="configPushSuccessOk"]')
ok_button.click()
time.sleep(5)
driver.close()
