# Siempre en los programas de selenium desde python
import time
from selenium import webdriver # navegador
from selenium.webdriver.firefox.options import Options

# Configurar el driver
opciones = Options()
opciones.headless = True # Haga el trabajo sin mostrar fisicamente la pantalla del navegador
navegador = webdriver.Firefox(executable_path='./drivers/geckodriver', options=opciones)
navegador.set_window_position(0, 0)
navegador.set_window_size(800, 500)
# Abrir un navegador en una ruta
navegador.get('https://google.es')
# Identificaremos elementos y actuaremos sobre ellos
navegador.find_element_by_xpath("//input[@name='q']").send_keys("Sevilla")
#time.sleep(2) # Espera 2 segundos
navegador.find_element_by_xpath("//input[@name='btnK']").click()
#time.sleep(3) # Espera 3 segundos
estadisticas=navegador.find_element_by_xpath("//div[@id='result-stats']").text
print(estadisticas)
# Cerrar el navegador
navegador.quit()