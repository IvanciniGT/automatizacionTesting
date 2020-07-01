# Siempre en los programas de selenium desde python
import time
from selenium import webdriver # navegador
from selenium.webdriver.firefox.options import Options
import os

def hacer_login(usuario, password, nombre_prueba, carpeta):
    # Configurar el driver
    opciones = Options()
    opciones.headless = True # Haga el trabajo sin mostrar fisicamente la pantalla del navegador
    navegador = webdriver.Firefox(executable_path='./drivers/geckodriver', options=opciones)
    navegador.set_window_position(0, 0)
    navegador.set_window_size(1000, 500)
    # Abrir un navegador en una ruta
    navegador.get('http://testing-ground.scraping.pro/login')
    # Identificaremos elementos y actuaremos sobre ellos
    navegador.find_element_by_xpath("//input[@id='usr']").send_keys(usuario)
    navegador.find_element_by_xpath("//input[@id='pwd']").send_keys(password)
    # Crear carpeta para las fotos
    directorio = carpeta+ '/capturas/' + nombre_prueba
    try:
        os.stat(directorio)
    except:
        os.makedirs(directorio)

    # Pedir foto, con los datos rellenos
    # Hago scroll para asegurarme que sale en la foto
    ubicacion=navegador.find_element_by_xpath("//input[@id='usr']").location_once_scrolled_into_view
    # Poner borde alrededor del formulario
    remarcar_elemento(navegador, "//form")

    navegador.save_screenshot(directorio + '/antes_del_login.png')
    # Havcemo click para probar el login
    navegador.find_element_by_xpath("//input[@type='submit']").click()
    #time.sleep(3) # Espera 3 segundos
    resultado_login=navegador.find_element_by_xpath("//h3[@class='success' or @class='error']").text

    # Hago scroll para asegurarme que sale en la foto
    ubicacion=navegador.find_element_by_xpath("//h3[@class='success' or @class='error']").location_once_scrolled_into_view
    # Hacer borde alrededor del texto
    borde_original = remarcar_elemento(navegador,"//h3[@class='success' or @class='error']")
    navegador.save_screenshot(directorio + '/despues_del_login_con_borde.png')
    # Restituyo el borde original
    remarcar_elemento(navegador, "//h3[@class='success' or @class='error']",borde_original)
    navegador.save_screenshot(directorio + '/despues_del_login.png')
    # Cerrar el navegador
    navegador.quit()
    return resultado_login


def remarcar_elemento(navegador, xpath, estilo='4px solid red'):
    # Buscamos el elemento
    elemento = navegador.find_element_by_xpath(xpath)
    # Recuperamos el borde que tenia
    original=navegador.execute_script("return arguments[0].style.border;",elemento)
    # Ponemos el nuevo borde
    navegador.execute_script("arguments[0].style.border = '" + estilo + "';",elemento)
    return original