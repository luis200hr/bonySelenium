from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



from selenium.webdriver.common.keys import Keys
import time
#driver = webdriver.Chrome(executable_path=r'C:/Users/luisi/Videos/AnyDesk/web/chromedriver.exe')
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

driver.get("https://app.bony.chat/")

#usuario  = driver.find_element_by_id("input-30")
usuario = driver.find_element(By.ID, "input-30")
usuario.send_keys("correo")

clave = driver.find_element(By.ID,  "input-35")
clave.send_keys("contraseña")
clave.send_keys(Keys.ENTER)
time.sleep(10)
BuscarEspacio = driver.find_element(By.CLASS_NAME, 'v-btn.v-btn--icon.v-btn--round.v-btn--text.theme--light.v-size--default')
BuscarEspacio.click()
time.sleep(2)
#div_contenedor = driver.find_element(By.CLASS_NAME, 'v-menu__content theme--light v-menu__content--fixed menuable__content__active space-switcher-menu')
#selecBusqueda = div_contenedor.find_element(By.ID, "input-597")
#v-text-field__slot
selecBusqueda = driver.find_element(By.CLASS_NAME, "v-text-field__slot")
selecBusqueda.click()
time.sleep(1)
elemento = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Buscar área de trabajo"]')

#Variable nombre del 
espacioNombre= "ReclutamientoIT"
elemento.send_keys(espacioNombre)
time.sleep(3)
selecSpace = driver.find_element(By.CSS_SELECTOR, 'div.caption.grey--text.text--darken-2.fill-width')
selecSpace.click()
time.sleep(5)
#selecConfig = driver.find_element_by_xpath('//a[@data-pendo="nav-settings"]')
#selecConfig.click()
# Esperar hasta que el elemento esté visible
selecConfig = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//a[@data-pendo="nav-settings"]'))
)
# Hacer clic en el elemento
selecConfig.click()
time.sleep(5)
#selecUsers = WebDriverWait(driver, 30).until(
#    EC.visibility_of_element_located((By.XPATH, '//a[@data-pendo="subnav-settings_space_users"]'))
#)
#selecUsers = driver.find_element_by_xpath('//a[@data-pw="usuarios"]')
#selecUsers.click()
#nameSpace = driver.find_element(By.CLASS_NAME, "space-search")
#campo_busqueda = driver.find_element_by_css_selector('input[type="text"]')

#driver.execute_script("arguments[0].focus();", nameSpace)
#campo_busqueda.send_keys("ReclutamientoIT")

#nameSpace.send_keys("ReclutamientoIT")
time.sleep(2)
#selectSpace = driver.find_element(By.CLASS_NAME, 'text-break content-to-ltr text-truncate')
#selectSpace.click()
time.sleep(3)

driver.close()
