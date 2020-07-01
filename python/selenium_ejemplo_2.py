import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium_utils import sacar_foto_elemento, remarcar_elemento


def do_login(user,password):

    ######################## PREPARACION DEL ENTORNO ############################
    # Opciones de ejecución del navegador
    options = Options()
    # Modo hearless... Muestra u oculta el navegador
    options.headless = False
    # Arranca un navegador firefox
    navegador = webdriver.Firefox(
        executable_path='/home/usuario/proyectos/python/drivers/geckodriver' ,
        options=options)
    navegador.set_window_position(0, 0)
    navegador.set_window_size(1200, 1000)

    ######################## TRABAJAMOS EN LA PAGINA ############################
    # Vamos a una página web
    navegador.get('http://testing-ground.scraping.pro/login')
    # Buscamos un elemento de la web y escribimos un texto en él
    navegador.find_element_by_xpath("//input[@id='usr']").send_keys(user )
    # Buscamos un elemento de la web y escribimos un texto en él
    navegador.find_element_by_xpath("//input[@id='pwd']").send_keys(password)

    # Capturas de pantalla
    navegador.save_screenshot("capturas/captura_antes_borde.png")
    borde_anterior=remarcar_elemento(navegador,"//form" )
    navegador.save_screenshot("capturas/captura_despues_borde.png")
    sacar_foto_elemento(navegador,"//form",'capturas/formulario.png' )
    remarcar_elemento(navegador,"//form", borde_anterior)
    navegador.save_screenshot("capturas/captura_reestablecido_borde.png")

    # Buscamos un elemento de la web y hacemos click en el

    navegador.find_element_by_xpath("//input[@type='submit']").click()
    # Esperamos para asegurarnos que haya cargado bien
    time.sleep(2)

    # Tomamos el título de la página y lo imprimos
    titulo = navegador.title
    print(titulo)
    navegador.save_screenshot("capturas/captura1.png")
    
    ######################## CERRAMOS DEL ENTORNO ############################
    # Esperamos otro poco de tiempo para verlo todo por pantalla
    time.sleep(0)

    # Cerramos el navegador. IMPORTANTE!!!
    navegador.quit()

do_login('admin','12345')