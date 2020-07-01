import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# CheatSheet XPATH: https://devhints.io/xpath

def do_login(user,password):

    ######################## PREPARACION DEL ENTORNO ############################
    # Opciones de ejecución del navegador
    options = Options()
    # Modo hearless... Muestra u oculta el navegador
    options.headless = False
    # Arranca un navegador firefox
    browser = webdriver.Firefox(
        executable_path='/home/usuario/proyectos/python/drivers/geckodriver' ,
        options=options)


    ######################## TRABAJAMOS EN LA PAGINA ############################
    # Vamos a una página web
    browser.get('http://testing-ground.scraping.pro/login')
    # Buscamos un elemento de la web y escribimos un texto en él
    browser.find_element_by_xpath("//input[@id='usr']").send_keys(user )
    # Buscamos un elemento de la web y escribimos un texto en él
    browser.find_element_by_xpath("//input[@id='pwd']").send_keys(password)
    # Buscamos un elemento de la web y hacemos click en el
    browser.find_element_by_xpath("//input[@type='submit']").click()

    # Esperamos para asegurarnos que haya cargado bien
    time.sleep(2)

    # Tomamos el título de la página y lo imprimos
    titulo = browser.title
    print(titulo)

    ######################## CERRAMOS DEL ENTORNO ############################
    # Esperamos otro poco de tiempo para verlo todo por pantalla
    time.sleep(3)

    # Cerramos el navegador. IMPORTANTE!!!
    browser.quit()

do_login('admin','12345')